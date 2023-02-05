
from django.urls import path
from .views import *
# from .views import 
urlpatterns = [
    path('users/',UserList.as_view()),
    path('users/<int:pk>/',UserDetails.as_view()),
    path('products/',ProductList.as_view()),
    path('products/<int:pk>/',ProductDetails.as_view()),
]