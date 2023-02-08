from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('__all__')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('__all__')

class BundleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BundleProducts
        fields = ('__all__')

class ProductBundleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBundles
        fields = ('__all__')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ('__all__')

class SentimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sentiment
        fields = ('__all__')
