from rest_framework import generics
from .models import *
from .serializers import *

class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
        

class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class ProductList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        queryset = Products.objects.all()
        user = self.request.query_params.get('users')
        if user is not None:
            queryset = queryset.filter(sellerID=user)
        return queryset

class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Products.objects.all()
