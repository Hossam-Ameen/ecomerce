from .models import Brand
from .serializers import BrandSerializer
from rest_framework.response import Response
from rest_framework import status, viewsets


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    
    def create(self, request, *args, **kwargs):
        request.data._mutable = True
        request.data.update({'user': request.user.id})
        brand_serializer = self.serializer_class(data=request.data)
        brand_serializer.is_valid(raise_exception=True)
        brand_serializer.save()
        return Response(brand_serializer.data, status=status.HTTP_201_CREATED)
        
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        request.data._mutable = True
        request.data.update({'user': instance.user.id})
        brand_serializer = self.serializer_class(instance, data=request.data)
        brand_serializer.is_valid(raise_exception=True)
        brand_serializer.save()
        return Response(brand_serializer.data, status=status.HTTP_200_OK)
