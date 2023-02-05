from rest_framework import generics
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tools import sentiment_scores
from .models import *
from .serializers import *

class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    # queryset = User.objects.all()
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
    autoSave = True if request.query_params.get('autosave')=='true' else False
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
