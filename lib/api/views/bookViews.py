from rest_framework import status


from django.contrib.auth.models import Permission
from rest_framework.response import Response
from api.models import *
from api.serializers import SignupSerializer,CreateUserSerializer
from rest_framework.views import APIView

from rest_framework.permissions import AllowAny


from api.services.bookService import *

book_service = BookSerivce()


class CreateBookView(APIView):

    def post (self,request,format=None):
        result = book_service.create_book_entry(request,format=None)
        return Response(result,status=result["code"])

class UpdateBookView(APIView):
    def put(self,request,pk,format=None):
        result = book_service.update_book(request,pk,format=None)
        return Response(result,status=result["code"])

class DeleteBookView(APIView):
    def delete(self, request, pk, format=None):
        result = book_service.delete_book(request, pk, format=None)
        return Response(result, status=status.HTTP_200_OK)

class GetAllBookView(APIView):
    def get(self,request,format=None):
        result=book_service.get_all_book(request,format=None)
        return Response(result,status=result["code"])

