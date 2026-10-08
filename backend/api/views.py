from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import isAuthenticated, AllowAny

class CreateUserView(generics.CreateAPIView):
  # 
  # this specify the list of all the defirents objects that we will be loking at when 
  # a new one is created to make use that we don't create a user that already exist
  queryset = User.objects.all() 
  # this class tells us what kind of data we need to accept when creating a new user.
  serializer_class = User 
  # this class specifies who can call this view, in this case, we want to allow anyone 
  # to create a new user, so we use AllowAny permission class.
  permission_classes = [AllowAny] 
