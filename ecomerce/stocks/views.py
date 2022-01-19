from .models import Stock
from .serializers import StockSerializer
from rest_framework.response import Response
<<<<<<< HEAD
from django.http import HttpResponse
=======
>>>>>>> main
from rest_framework import status, viewsets


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    
<<<<<<< HEAD
    def create(self, request, * args, ** kwargs):
        request.data.update({'user': request.user.id})
        # request.data['user'] =  request.user.id
=======
    def create(self, request, *args, **kwargs):
        request.data._mutable = True
        request.data.update({'user': request.user.id})
>>>>>>> main
        stock_serializer = self.serializer_class(data=request.data)
        stock_serializer.is_valid(raise_exception=True)
        stock_serializer.save()
        return Response(stock_serializer.data, status=status.HTTP_201_CREATED)
        
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
<<<<<<< HEAD
=======
        request.data._mutable = True
>>>>>>> main
        request.data.update({'user': instance.user.id})
        stock_serializer = self.serializer_class(instance, data=request.data)
        stock_serializer.is_valid(raise_exception=True)
        stock_serializer.save()
        return Response(stock_serializer.data, status=status.HTTP_200_OK)
