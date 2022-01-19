from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status, viewsets


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def create(self, request, *args, **kwargs):
        request.data._mutable = True
        request.data.update({'user': request.user.id})
        product_serializer = self.serializer_class(data=request.data)
        product_serializer.is_valid(raise_exception=True)
        product_serializer.save()
        return Response(product_serializer.data, status=status.HTTP_201_CREATED)
        
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        request.data._mutable = True
        request.data.update({'user': instance.user.id})
        product_serializer = self.serializer_class(instance, data=request.data)
        product_serializer.is_valid(raise_exception=True)
        product_serializer.save()
        return Response(product_serializer.data, status=status.HTTP_200_OK)
