from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.conf import settings





class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = Userlogin
        fields = "__all__"
        
        
class blogserializer(serializers.ModelSerializer):
  
    class Meta:
        model = blog
        fields = "__all__"
        
class UserBookMarkSerializer(serializers.ModelSerializer): 
    class Meta:
        fields=("__all__")
        model=BookMark
        
        
class commentserializer(serializers.ModelSerializer):
     class Meta:
        fields=("__all__")
        model= Comment
        
        
class CategoryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryType
        fields = "__all__"
        

                
        
        