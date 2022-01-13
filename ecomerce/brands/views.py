from rest_framework import generics
from .models import Brand
from .serializers import BrandSerializer
from rest_framework.response import Response
from rest_framework import status,viewsets


class ListBrands(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class CreateBrand(generics.CreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    
    def create(self, request, * args, ** kwargs):
        request.data.update({'user': request.user.id})
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else :
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
class GetBrand(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class UpdateBrand(generics.UpdateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        request.data.update({'user': instance.user.id})
        serializer = self.serializer_class(instance, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        else :
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        

class DeleteBrand(generics.DestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer