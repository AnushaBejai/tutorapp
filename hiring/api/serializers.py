from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate 
from rest_framework.authtoken.models import Token 
from hiring.models import *




# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')


class RegisterSerializer(serializers.ModelSerializer):
    
    confirm_password = serializers.CharField(style={'input_type':'password'}, write_only = True)
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'confirm_password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        tutor=User(
            username=self.validated_data['username']
        )
        password=self.validated_data['password']
        confirm_password=self.validated_data['confirm_password']
        if password != confirm_password:
            raise serializers.ValidationError({'password':'Passwords do not match.'})
        tutor.set_password(validated_data['password'])
        tutor.save()
        return tutor 

class TutorPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutorPost
        fields="__all__"

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields="__all__"

class StudentrequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentpost
        fields="__all__"

    