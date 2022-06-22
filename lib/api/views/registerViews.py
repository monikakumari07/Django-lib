from rest_framework import status

from django.contrib.auth.models import Permission
from rest_framework.response import Response
from api.models import *
from api.serializers import RegisterSerializer
from rest_framework.views import APIView


from api.services.registerService import *

register_service = RegisterSerivce()

class CreateRegisterView(APIView):

    def post (self,request,format=None):
        result = register_service.create_Register(request,format=None)
        return Response(result,status=result["code"])

class UpdateRegisterView(APIView):
    def put(Self,request,pk,formate=None):
        result = register_service.update_Register(request,pk,format=None)
        return Response(result,status=result["code"])

class DeleteRegisterView(APIView):
    def delete(self, request, pk, format=None):
        result = register_service.delete_Register(request, pk, format=None)
        return Response(result, status=status.HTTP_200_OK)

class getall_Register(APIView):

    def get(self,request,format=None):
        result=register_service.get_all_Register(request,format=None)
        return Response(result,status=result["code"])
