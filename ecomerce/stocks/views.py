from .models import Stock
from .serializers import StockSerializer
from rest_framework.response import Response
from rest_framework import status,viewsets


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    
    def create(self, request, * args, ** kwargs):
        request.data.update({'user': request.user.id})
        stock_serializer = self.serializer_class(data=request.data)
        if stock_serializer.is_valid(raise_exception=True):
            stock_serializer.save()
            return Response(stock_serializer.data, status=status.HTTP_201_CREATED)
        
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        request.data.update({'user': instance.user.id})
        stock_serializer = self.serializer_class(instance, data=request.data)
        if stock_serializer.is_valid(raise_exception=True):
            stock_serializer.save()
            return Response(stock_serializer.data, status=status.HTTP_200_OK)
