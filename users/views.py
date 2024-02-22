from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import (AllowAny)
from rest_framework.authentication import BasicAuthentication,SessionAuthentication


from utils.utils import ResponseUtils
from .serializers import LoginSerializer,RegisterSerializer


class RegisterAPIView(generics.GenericAPIView):
    # authentication: basic , sessionauthentication
    authentication_classes = [BasicAuthentication,SessionAuthentication,]
    # permissions: allowany 
    permission_classes = [AllowAny]
    # serializer:
    #   -email: must be a valid email format and must be uniqe because is the username also
    #       *ideas: email otp can be added to validate if the email is real or not
    #   -password: basic django validation is fine
    #       *ideas: the default validator for password can be customized
    #   -name & family: must be a valid string 
    #   -status:must be of 3 choices (admin,operator,user<default>)
    #       *ideas: for now we can change this with a simple api 
    #       ~must be done: status should be updated with a condition like purchasing a plan to be of a higher status
    serializer_class = RegisterSerializer
    def post(self,request,*args,**kwargs):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if not serializer.is_valid():
            return Response(ResponseUtils.error_serializer(serializer_errors=serializer.errors))
        else:
            user_data,token = serializer.save()
            data = {
                'user':user_data,
                'token':token
            }
            return Response(ResponseUtils.ok_context(data=data))

class LoginAPIView(generics.GenericAPIView):
    # authentication: basic , sessionauthentication
    authentication_classes = [BasicAuthentication,SessionAuthentication,]
    # permissions: allowany 
    permission_classes = [AllowAny]
    # serializer: 
    #   -must be the correct enterys so we search the database for the credentials
    #   -after finding the correct user we return user info and a token using django restframework's basic token authentication with code 200
    #   -wrong credentials and we return an error message in response with code 404
    serializer_class = LoginSerializer
    def post(self,request,*args,**kwargs):
        data = request.data
        serializer = LoginSerializer(data=data,context={'request':request})
        if not serializer.is_valid():
            return Response(ResponseUtils.error_serializer(serializer_errors=serializer.errors))
        else:
            user_data,token = serializer.save()
            data = {
                'user':user_data,
                'token':token
            }
            return Response(ResponseUtils.ok_context(data=data))



