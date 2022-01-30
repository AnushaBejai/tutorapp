from rest_framework import viewsets, status 
from rest_framework.decorators import action
from django.contrib.auth.models import User, update_last_login
from rest_framework.response import Response 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from hiring.models import *
from hiring.api.serializers import UserSerializer, RegisterSerializer, TutorPostSerializer, StudentSerializer, StudentrequirementSerializer
from django.contrib.auth.models import User 
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from django.contrib.auth import login,logout,authenticate 
from rest_framework.authtoken.views import ObtainAuthToken
from django.shortcuts import render 
from rest_framework.views import APIView 
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework.pagination import PageNumberPagination 
from rest_framework.generics import ListAPIView
from rest_framework import filters
import json    
import pdb

@api_view(['POST', ])
def registration_view(request):
    if request.method == 'POST':
        serializer=RegisterSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            tutor = serializer.save()
            Tutor.objects.create(user=tutor, name=tutor.username)
            data['response'] = "Successfully registered a new user"
            data['username']=tutor.username 
            #token=Token.objects.get(user=tutor).key
            #data['token']=token
            
        else:
            data=serializer.errors 
        return Response(data)  


class UserLogin(APIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer 
    def post(self, request, format='json'):
        username=request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(self, username=username, password=password)
        if user:
            id=user.id
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token":token.key, 'username':token.user.username}, status=status.HTTP_201_CREATED)
        else:
            return Response("Unable to Log in. Please check the username and password.", status = status.HTTP_400_BAD_REQUEST) 



class UserLogout(APIView):
    permission_classes = [permissions.IsAuthenticated,]
    def post(self, request, format=None):
        request.user.auth_token.delete()
        logout(request)
        return Response(status=status.HTTP_200_OK) 




@api_view(['POST', ])
@permission_classes((IsAuthenticated, TokenHasReadWriteScope))
def TutorPosts(request):
    if request.method == 'POST':
        serializer=TutorPostSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            serializer.save()
            
            data['response'] = "Successfully Posted"
           
            
        else:
            data=serializer.errors 
        return Response(data)  


@api_view(['POST', ])
def StudentApplication(request):
    if request.method == 'POST':
        serializer=StudentSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            serializer.save()
            
            data['response'] = "Successfully Applied"
           
            
        else:
            data=serializer.errors 
        return Response(data)  

@api_view(['POST', ])
def Studentrequirement(request):
    if request.method == 'POST':
        serializer=StudentrequirementSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            serializer.save()
            
            data['response'] = "Successfully Posted"
           
            
        else:
            data=serializer.errors 
        return Response(data)  




class TutorPostList(ListAPIView):
    queryset = TutorPost.objects.all()
    serializer_class = TutorPostSerializer
    pagination_class= PageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['subject','tutor__name']
   

class StudentList(APIView):
    permission_classes = [permissions.IsAuthenticated,]
    
    def get(self, request):
        if request.user.is_authenticated:
            students=Students.objects.filter(tutor__name=request.user.username)
            serializer=StudentSerializer(students, many=True)
            return Response(serializer.data)


        