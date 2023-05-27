from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<pk>/', UserDetails.as_view()),
    path('products/', ProductList.as_view()),
    path('products/<pk>/', ProductDetails.as_view()),
    path('orders/', OrderList.as_view()),
    path('orders/<pk>/', OrderDetails.as_view()),
    path('bundleproducts/', BundleProductList.as_view()),
    path('bundleproducts/<pk>/', BundleProductDetails.as_view()),
    path('productbundle/', ProductBundleList.as_view()),
    path('productbundle/<pk>/', ProductBundleDetails.as_view()),
    path('reviews/', ReviewList.as_view()),
    path('reviews/<pk>/', ReviewDetails.as_view()),
    path('sentiments/', SentimentList.as_view()),
    path('sentiments/<pk>/', SentimentDetails.as_view()),
    path('analizeproductreviews/', analizeProductReviews),
    path('generatebundle/', generateBundle),
    path('getanalytics/', getAnalytics)
]