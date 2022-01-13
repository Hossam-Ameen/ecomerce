from .models import Module
from .serializers import ModuleSerializer
from rest_framework.response import Response
from rest_framework import status,viewsets


class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    
    def create(self, request, * args, ** kwargs):
        request.data.update({'user': request.user.id})
        module_serializer = self.serializer_class(data=request.data)
        if module_serializer.is_valid(raise_exception=True):
            module_serializer.save()
            return Response(module_serializer.data, status=status.HTTP_201_CREATED)
           
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        request.data.update({'user': instance.user.id})
        module_serializer = self.serializer_class(instance, data=request.data)
        if module_serializer.is_valid(raise_exception=True):
            module_serializer.save()
            return Response(module_serializer.data, status=status.HTTP_200_OK)
