import jwt
from django.conf import Settings
from rest_framework import status
from rest_framework.response import Response
from api.models.userModel import *

from api.serializers import SignupSerializer,CreateUserSerializer,LoginSerializer
from rest_framework_jwt.settings import api_settings

from lib import settings
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER



class UserService():
   

    def __init__(self):
        pass

#SIGNUP

    def createsignup(self,request,format=None):

            a=User.objects.filter(email=request.data["email"])
            if len(a) > 0 :
                
                return ({"data":None, "code":status.HTTP_400_BAD_REQUEST,"message":"already register"})
            else:

                serializer=CreateUserSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return ({"data":serializer.data,"code":status.HTTP_201_CREATED,"message":"OK"})
                else:
                    return ({"data":serializer.errors,"code":status.HTTP_400_BAD_REQUEST,"message":"error"})

#LOGIN
    def createlogin(self,request,format=None):
        validated_data=self.validate_auth_data(request)
        email = request.data['email']
        email = email.lower()
        password = request.data['password']
        user = self.user_authenticate(email, password)
        

        if user is not None:
             login(request, user)
             print("###########################")
             serializer = LoginSerializer(user)
             
             payload = jwt_payload_handler(user)
             print("------------------------")
             token = jwt.encode(payload,settings.SECRET_KEY)
             signupdetails = serializer.data
             signupdetails['token']=token
             user_obj = User.objects.get(email=email)
             user_obj.token = token
            #  user_obj.save()
            #  otp = random.randint (100000, 999999)
            #  self.send_factor_otp(user,otp)
            #  self.send_mobile_otp(user, otp)
           

             return({"data":signupdetails,"code":status.HTTP_200_OK,"message":"Login successfull"})
        else:
            return({"data":None,"code":status.HTTP_400_BAD_REQUEST,"message":"An account with this email id doesnot exist"})


    def validate_auth_data(self,request):
        error = {}
        if not request.data.get('email'):
            error.update({'email':"FIELD_REQUIRED"})

        if not request.data.get('password'):
            error.update({'password':"FIELD_REQUIRED"})
    
        if error:
            raise ValidationError(error)


    def user_authenticate(self,email,password):
        try:
            
            data=User.objects.get(email=email)
            if data.check_password(password):
                return data
        except User.DoesNotExist:
            return None                    

