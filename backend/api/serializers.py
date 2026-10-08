from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User # the user model is buildt-in django model for user authentication and authorization
    # the fields that we want to serialize went we're accepting a new user and returning a new one
    fields = ["id", "username", "email", "password"] 
    # this tell Django that we want to accept a password when a new user is created. 
    # We don;t wanna return the password when giving info about the user. 
    # So 'write_only' means no one can read the password when we return the user info.
    extra_kwargs = {"password" : {"write_only": True}} 

  # this method is called when we create a new user. It takes the validated data and creates a new user using 
  # the create_user method provided by Django's User model. This method automatically hashes the password 
  # before saving it to the database. this '**' is used to unpack the validated data and passes them in as a dictionary
  def create(self, validated_data):
    user = User.objects.create_user(**validated_data)
    return user