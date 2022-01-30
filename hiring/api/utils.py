from django.contrib.auth import authenticate
from rest_framework import serializers


def get_and_authenticate_user(username, password):
    tutor = authenticate(username=username, password=password)
    if tutor is None:
        raise serializers.ValidationError("Invalid username/password. Please try again!")
    return tutor