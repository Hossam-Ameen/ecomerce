from rest_framework import generics
from .models import Module
from .serializers import ModuleSerializer
from rest_framework.response import Response
from rest_framework import status,viewsets


class ListModules(generics.ListCreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

    
class CreateModule(generics.CreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    
    def create(self, request, * args, ** kwargs):
        request.data._mutable = True
        request.data.update({'user': request.user.id})
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else :
          
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        
class GetModule(generics.RetrieveAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class UpdateModule(generics.UpdateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        request.data.update({'user': instance.user.id})
        serializer = self.serializer_class(instance, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        else :
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class DeleteModule(generics.DestroyAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer