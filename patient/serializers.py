

from rest_framework import serializers
from . import models
from django.contrib.auth.models import User


class PatientSerialaizers(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
         model=models.Patient
         fields='__all__'

class RegistrationSerialaizers(serializers.ModelSerializer):
   confirm_password = serializers.CharField(required=True)

   class Meta:
      model = User
      fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']

   def save(self):
      # Retrieve validated data
      username = self.validated_data['username']
      first_name = self.validated_data['first_name']
      last_name = self.validated_data['last_name']
      email = self.validated_data['email']
      password = self.validated_data['password']
      confirm_password = self.validated_data['confirm_password']

      # Validate that the passwords match
      if password != confirm_password:
         raise serializers.ValidationError({'error': "Passwords don't match"})

      # Check if the email already exists
      if User.objects.filter(email=email).exists():
         raise serializers.ValidationError({'error': "Email already exists"})

      # Create the User instance, but don't pass confirm_password
      user = User(username=username, email=email, first_name=first_name, last_name=last_name)
      user.set_password(password)  # Ensure the password is hashed before saving
      user.is_active=False
      user.save()

      return user

class UserLogInSerializers(serializers.Serializer):
   username=serializers.CharField(required=True)
   password=serializers.CharField(required=True)
