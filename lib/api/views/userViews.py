from rest_framework import status


from django.contrib.auth.models import Permission
from rest_framework.response import Response
from api.models import *
from api.serializers import SignupSerializer,CreateUserSerializer
from rest_framework.views import APIView

from rest_framework.permissions import AllowAny

from api.services.userService import *

user_service_obj = UserService()


class CreateSignupView(APIView):
    permission_classes = (AllowAny,)
    def post (self,request,format=None):
        result = user_service_obj.createsignup(request,format=None)
        return Response(result,status=result["code"])

#LOGIN
class loginView(APIView):

    def post(self, request, format=None):
        result = user_service_obj.createlogin(request, format=None)
        return Response(result, status=result["code"])
