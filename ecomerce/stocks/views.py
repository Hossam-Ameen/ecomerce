from rest_framework import generics
from .models import Stock
from .serializers import StockSerializer
from rest_framework.response import Response
from rest_framework import status,viewsets

class ListStocks(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    
class CreateStock(generics.CreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    
    def create(self, request, * args, ** kwargs):
        request.data._mutable = True
        request.data.update({'user': request.user.id})
        # request.data.update
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else :
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        
class GetStock(generics.RetrieveAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class UpdateStock(generics.UpdateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

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


class DeleteStock(generics.DestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer