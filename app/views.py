from django.shortcuts import render
from app.serializers import Product_Serializer
from app.models import Product , Product_category
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response 


# Create your views here.
@permission_classes([IsAuthenticated])
class ProductData(APIView):
    
    def get(self,request,id):
        
        PQS = Product.objects.all()
        PMS = Product_Serializer(PQS,many = True)
        return Response(PMS.data)
    
    
    def post(self,request,id):
        PMSD = Product_Serializer(data=request.data)
        if PMSD.is_valid():
            SPO = PMSD.save()
            return Response({"message":f"product is created"})
        else:
            return Response({"message":"product creation is failed"})
    
    
    def put(self,request,id):
        id = request.data['id']
        Po = Product.objects.get(id=id)
        PMSD = Product_Serializer(Po,data = request.data)
        if PMSD.is_valid():
            SPO = PMSD.save()
            return Response({"message":f" product is  updated"})
        else:
            return Response({"message":"product details is not updated"})
    
    
    def patch(self,request,id):
        id = request.data['id']
        Po = Product.objects.get(id=id)
        Po.pname = request.data['pname']
        Po.save()
        return Response({"Success":"data is partially updated"})
    
    def delete(self,request,id):
        obj = Product.objects.get(id = id).delete()
        if obj == None:
            return Response({'details':"product is a not available"},
                            status= status.HTTP_204_NO_CONTENT) 
        return Response({"success":"Product is deleted"})