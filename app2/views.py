from django.shortcuts import render 
from app2.models import Product
from app2.serializers import *
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class ProductCrud(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = Product_Serializer
    
    

