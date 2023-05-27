from rest_framework import generics
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tools import sentiment_scores
from .models import *
from .serializers import *
import requests
import numpy as np
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
from itertools import permutations
from collections import Counter
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    
    def get_queryset(self):
        queryset = User.objects.all()
        id = self.request.query_params.get('id')
        
        if id is not None:
            queryset = queryset.filter(id=id)
            
        return queryset        

class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class ProductList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        queryset = Products.objects.all()
        user = self.request.query_params.get('seller')
        
        if user is not None:
            queryset = queryset.filter(sellerID=user)
            
        productName = self.request.query_params.get('name')
        
        if productName is not None:
            queryset = queryset.filter(name=productName)
            
        return queryset

class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Products.objects.all()

class OrderList(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    
    def get_queryset(self):
        queryset = Orders.objects.all()
        user = self.request.query_params.get('seller')
        
        if user is not None:
            queryset = queryset.filter(sellerID=user)
            
        return queryset

class OrderDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Orders.objects.all()

class BundleProductList(generics.ListCreateAPIView):
    serializer_class = BundleProductSerializer
    
    def get_queryset(self):
        queryset = BundleProducts.objects.all()
        user = self.request.query_params.get('seller')
        
        if user is not None:
            queryset = queryset.filter(sellerID=user)
            
        return queryset

class BundleProductDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BundleProductSerializer
    queryset = BundleProducts.objects.all()

class ProductBundleList(generics.ListCreateAPIView):
    serializer_class = ProductBundleSerializer
    
    def get_queryset(self):
        queryset = ProductBundles.objects.all()
        bundleProduct = self.request.query_params.get('bundleproduct')
        product = self.request.query_params.get('product')
        
        if bundleProduct is not None:
            queryset = queryset.filter(bundleProductID=bundleProduct)
            
        if product is not None:
            queryset = queryset.filter(productID=product)
            
        return queryset

class ProductBundleDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BundleProductSerializer
    queryset = BundleProducts.objects.all()

class ReviewList(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        queryset = Reviews.objects.all()
        product = self.request.query_params.get('product')
        
        if product is not None:
            queryset = queryset.filter(productID=product)
            
        return queryset

class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    queryset = Reviews.objects.all()

class SentimentList(generics.ListCreateAPIView):
    serializer_class = SentimentSerializer
    
    def get_queryset(self):
        queryset = Sentiment.objects.all()
        review = self.request.query_params.get('review')
        
        if review is not None:
            queryset = queryset.filter(reviewID=review)
            
        return queryset

class SentimentDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SentimentSerializer
    queryset = Sentiment.objects.all()


@api_view(['GET'])
def analizeProductReviews(request):
    serializer_class = SentimentSerializer
    reviews = Reviews.objects.all()
    product = request.query_params.get('product')
    autoSave = True if request.query_params.get('autosave') == 'true' else False
    
    if product is not None:
        reviews = reviews.filter(productID=product)
        
    reviewsList = reviews.all()
    sentiments = []
    
    for review in reviewsList:
        sentiment = sentiment_scores(review.textContent)
        data = {
            'positiveRate':sentiment['positive'],
            'negativeRate':sentiment['negative'],
            'neutralRate':sentiment['neutral'],
            'overallSentiment':sentiment['overall'],
            'reviewID':review.id
        }
        
        if autoSave:
            sentimentModel = SentimentSerializer(data=data)
            
            if sentimentModel.is_valid():
                sentimentModel.save()
                
            else:
                print("AHHHHHHHHHH")
                
        sentiments.append(data)
        
    return Response(sentiments)

def zhangs_rule(rules):
    rule_support = rules['support'].copy()
    rule_ante = rules['antecedent support'].copy()
    rule_conseq = rules['consequent support'].copy()
    num = rule_support - (rule_ante * rule_conseq)
    denom = np.max((rule_support * (1 - rule_ante).values, rule_ante * (rule_conseq - rule_support).values), axis = 0)
    return num / denom

def load():
    orders = Orders.objects.all()
    orders = orders.filter(sellerID='3324')#in production it will load all the registered user order datas for faster bundle generation
    newOrders = []
    
    for order in orders:
        date = str(order.date).split('-')
        dateObject = datetime. strptime(str(order.date), '%Y-%m-%d')
        newOrders.append({
            'Member_number':order.orderID,
            'Date':order.date,
            'itemDescription':order.productID.id,
            'year':date[0],
            'month':date[1],
            'day':date[2],
            'day_of_week':dateObject.weekday()
        })
        
    newOrders = pd.DataFrame(newOrders)
    freq_items = newOrders['itemDescription'].value_counts()
    user_id = newOrders['Member_number'].unique()
    items = [list(newOrders.loc[newOrders['Member_number'] == id, 'itemDescription']) for id in user_id]

    TE = TransactionEncoder()
    TE.fit(items)
    item_transformed = TE.transform(items)
    item_matrix = pd.DataFrame(item_transformed, columns = TE.columns_)
    freq_items = apriori(item_matrix, min_support=0.01, use_colnames=True, max_len=2)
    freq_items.sort_values(by = "support", ascending = False)
    rules = association_rules(freq_items, metric = "confidence", min_threshold = 0)
    rules_zhangs_list = zhangs_rule(rules)
    rules = rules.assign(zhang = rules_zhangs_list)
    
    return rules

rules = load()
@api_view(['GET'])
def generateBundle(request):
    
    try:
        product = request.query_params.get('product')
        print(product)
        rules_sel = rules[rules["antecedents"].apply(lambda x:product in x)]
        rules_sel.sort_values('confidence', ascending=False)
        rules_support = rules_sel['support'] >= rules_sel['support'].quantile(q = 0.95)# get the most important 5 items that customers would buy after purchasing whole milk 
        rules_confi = rules_sel['confidence'] >= rules_sel['confidence'].quantile(q = 0.95)
        rules_lift = rules_sel['lift'] > 1
        rules_zhang = rules_sel['zhang'] > 0
        rules_best = rules_sel[rules_support & rules_confi & rules_lift & rules_zhang]
        print(rules_best)
        
        if len(rules_best)<=0:return Response({
            'error':'Can\'t generate bundle'
        })
        
        returned_targets = {
            'antecedents':product,
            'consequents':[]
        }
    
        for target in rules_best.iloc:
            conseq = str(target["consequents"]).split("frozenset({'")[1].replace("'})","")
            returned_targets['consequents'].append(conseq)
            
        print(returned_targets)        
        return Response(returned_targets)
    
    except:
        return Response({
            'error':'bad request'
        })

@api_view(['GET'])
def getAnalytics(request):
    orders = Orders.objects.all()
    orders = orders.filter(sellerID='3324')
    months = {
        '1':0,
        '2':0,
        '3':0,
        '4':0,
        '5':0,
        '6':0,
        '7':0,
        '8':0,
        '9':0,
        '10':0,
        '11':0,
        '12':0,
    }
    years = {
        '2014':0,
        '2015':0,
        '2016':0,
        '2017':0,
        '2018':0,
        '2019':0,
        '2020':0,
        '2021':0,
        '2022':0,
        '2023':0,
        
    }
    
    for order in orders:
        mont = order.date.month
        months[str(mont)]+=(order.quantity*order.unitPrice)
        yer = order.date.year
        years[str(yer)]+=(order.quantity*order.unitPrice)

    return Response([months,years])