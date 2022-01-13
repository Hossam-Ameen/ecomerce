from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status,viewsets


class ListProducts(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CreateProduct(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def create(self, request, * args, ** kwargs):
        request.data._mutable = True
        
        request.data.update({'user': request.user.id})
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else :
            
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
class GetProduct(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UpdateProduct(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        request.data._mutable = True
        request.data.update({'user': instance.user.id})
        serializer = self.serializer_class(instance, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        else :
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        

class DeleteProduct(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer