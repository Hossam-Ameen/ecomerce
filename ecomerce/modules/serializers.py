from rest_framework import serializers
from .models import Module

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id','name' , 'brand','user']
        model = Module
        
    