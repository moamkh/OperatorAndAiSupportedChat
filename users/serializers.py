from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from .models import User




class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only = True , required = True)
    password = serializers.CharField(write_only = True,required=True)
    token = serializers.CharField(read_only=True)

    def validate(self, attrs):
        request = self.context['request']
        email = attrs['email']
        password = attrs['password']
        try:
            user_obj = User.objects.get(email = email)
        except:
            raise serializers.ValidationError("No user found with this email")
        user_obj = authenticate(request=request,email=email,password=password)
        if not user_obj:
            raise serializers.ValidationError("Login credentials are Wrong.")
        self.user_object = user_obj
        return attrs
    
    def create(self, validated_data):
        user_obj:User = self.user_object
        token,created = Token.objects.get_or_create(user = user_obj)
        user_data = {
            'email':user_obj.email,
            'name':user_obj.name,
            'family':user_obj.family,
            'status':user_obj.status,
        }
        token_key = token.key
        return user_data,token_key

        

class RegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(write_only = True , required = True)
    password = serializers.CharField(write_only = True,required=True,validators = [validate_password])
    password2 = serializers.CharField(write_only = True,required=True)
    name = serializers.CharField(write_only = True,required=True)
    family = serializers.CharField(write_only = True,required=True)
    class Meta:
        model = User
        fields= [ 
            'email',
            'password',
            'password2',
            'name',
            'family',
        ]

    def validate(self, attrs):
        email = attrs['email']
        password = attrs['password']
        password2 = attrs['password2']

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        if password != password2:
            raise serializers.ValidationError("Password fields do not match")
        return attrs
    
    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']
        name = validated_data['name']
        family = validated_data['family']
        user_obj = User.objects.create(
            name=name,
            family=family,
            email=email
        )
        user_obj.set_password(password)
        user_obj.save()
        user_data = {
            'email':user_obj.email,
            'name':user_obj.name,
            'family':user_obj.family,
            'status':user_obj.status,
        }
        token,created = Token.objects.get_or_create(user=user_obj)
        token_key = token.key
        return user_data,token_key