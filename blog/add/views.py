from django.shortcuts import render
import datetime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import  get_object_or_404, render
from django.urls import reverse
from django.views import View
from .models import *
from django.contrib.auth import authenticate
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
import jwt
from datetime import datetime
from rest_framework import status
from rest_framework import serializers,generics
from rest_framework.views import APIView  

# Create your views here.
@api_view(['POST'])

def login(request):
    data =Userserializer(request.data)
    data=request.data
    user_checklist = Userlogin.objects.filter(email=data['email'],password=data['password'])
    if user_checklist:
        token = jwt.encode({'user_id':'1','exp':datetime.datetime.utcnow()+datetime.timedelta(hours=1)},(data['email']+data['password']),'HS256')
        context={
            "data":data,"Meta":{"api": "v.1.0","url": "https://rentdev.space-iz.com/api/v1/user/register","message": "Login Succefully",'auth_token':str(token)}}
      
        return Response(context)                                                          #({'auth_token':str(token)})
    return Response({"message":"Invalid user!!"})

@api_view(['POST'])
def Add(request):
    serializer = blogserializer(data=request.data)
    if serializer.is_valid():
        serializer.save() 
    return Response(serializer.data)  

@api_view(['GET'])
def Show(self):
    queryset=blog.objects.all()
    serializer=blogserializer(queryset, many=True)
    context={
            "data":serializer.data,
            }
    return JsonResponse(context,status=status.HTTP_200_OK)


@api_view(['PUT'])
def update(request, pk):
    event=blog.objects.get(pk=pk)
    serializer=blogserializer(instance=event,data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)       


@api_view(['DELETE'])
def delete_items(request, pk):
    item = blog.objects.get(pk=pk)
    item.delete()
    context={
            "message":"Delete is Succefuley",
            }
    return Response( context,status=status.HTTP_202_ACCEPTED)

#---------------------------------------------------------Bookmark---------------------------------------------------------
class UserAddBookMark(generics.GenericAPIView):
    serializer_class = UserBookMarkSerializer

    # @verify_token
    def post(self, request, *args, **kwargs):
        try:
            data=request.data
            serializer = UserBookMarkSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"status": "success", "message": serializer.data}, status=status.HTTP_202_ACCEPTED)
            else:
                return JsonResponse({"status": "error", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
        	return JsonResponse({"status": "error", "message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class UserRemoveBookMark(generics.GenericAPIView):

    # @verify_token
    def delete(self, request, bookmark_id):
        
        try:
            bookmark=BookMark.objects.get(id=bookmark_id)
            bookmark.delete()
            return JsonResponse({"status": "success", "message": "Bookmark removed"}, status=status.HTTP_200_OK)
        except Exception as e:
        	return JsonResponse({"status": "error", "message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class UserViewBookMark(APIView):

    # @verify_token
    def get(self, request, user_id):
        try:
            bookmark=BookMark.objects.filter(user=user_id)
            serializer = UserBookMarkSerializer(bookmark,many=True)
            return JsonResponse({"status": "success", "message": serializer.data}, status=status.HTTP_202_ACCEPTED)
        except Exception as e:
        	return JsonResponse({"status": "error", "message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

     
@api_view(['GET'])
def Show1(self):
    queryset=BookMark.objects.all()
    serializer=UserBookMarkSerializer(queryset, many=True)
    context={
            "data":serializer.data,
            }
    return JsonResponse(context,status=status.HTTP_200_OK)

#-------------------------------------------------comment----------------------------------------------------------------------------------
class Usercomment(generics.GenericAPIView):
    serializer_class = commentserializer

    # @verify_token
    def post(self, request, *args, **kwargs):
        try:
            data=request.data
            serializer = commentserializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"status": "success", "message": serializer.data}, status=status.HTTP_202_ACCEPTED)
            else:
                return JsonResponse({"status": "error", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
        	return JsonResponse({"status": "error", "message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class  Usercomment1(APIView):

    # @verify_token
    def get(self, request,id):
        try:
            comment=Comment.objects.filter(user=id)
            serializer = commentserializer(comment,many=True)
            return JsonResponse({"status": "success", "message": serializer.data}, status=status.HTTP_202_ACCEPTED)
        except Exception as e:
        	return JsonResponse({"status": "error", "message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

     
@api_view(['GET'])
def Show2(self):
    queryset=Comment.objects.all()
    serializer=commentserializer(queryset, many=True)
    context={
            "data":serializer.data,
            }
    return JsonResponse(context,status=status.HTTP_200_OK)

#---------------------------------------------------------category-----------------------------------------------------------------------------------------

class AddCategoryTypeView(generics.ListCreateAPIView):
    queryset=CategoryType.objects.all()
    serializer_class=CategoryTypeSerializer

    def post(self, request, *args, **kwargs):
        serializer = CategoryTypeSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            serializer = CategoryTypeSerializer(user)
            context={
                "data":serializer.data,
                "Meta":{"message": "Category Added Successfully",
                "api": "v.1.0","url": "http://127.0.0.1:8000/rentapp/add-category"}
                }
            return JsonResponse(context, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryTypeView(generics.ListCreateAPIView):

    def get(self, request, *args, **kwargs):
        queryset=CategoryType.objects.all()
        serializer=CategoryTypeSerializer(queryset, many=True)
        context={
            "data":serializer.data,
            "Meta":{"message": "Category List Fetched Successfully",
            "api": "v.1.0","url": "http://127.0.0.1:8000/rentapp/get/category-type"}
            }
        return JsonResponse(context,status=status.HTTP_200_OK)
    
#------------------------------------------------------Tag---------------------------------------------------------------------------------------
