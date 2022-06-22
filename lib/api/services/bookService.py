from rest_framework import status
from rest_framework.response import Response
from api.models.bookModel import *
from api.serializers import BookSerializer

class BookSerivce():
    def __int__(self):
        pass

#Create an entry for Books.

    def create_book_entry(self,request,format=None):

            serializer=BookSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return({"data":serializer.data, "code":status.HTTP_200_OK, "message":"BOOK_CREATED"})
            else:
                return ({"data":serializer.errors, "code":status.HTTP_400_BAD_REQUEST, "message":"BAD_REQUEST"})
        
#Update a book
       
    def update_book(Self, request, pk, format=None):
        try:
            subscription = Book.objects.get(id=pk)
            serializer = BookSerializer(subscription,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return ({"data":serializer.data, "code":status.HTTP_200_OK, "message":"OK"})
            return ({"data":serializer.data, "code":status.HTTP_400_BAD_REQUEST,"message":"Bad Request"}) 
        except Book.DoesNotExist:
            return ({"data":None, "code":status.HTTP_400_BAD_REQUEST,"message":"Record Not Found"})

#Delete a book.

    def delete_book(self, request, pk, format=None):
        try:
            subscription = Book.objects.get(id=pk)
            subscription.delete()
            return({"data":None, "code":status.HTTP_200_OK, "message":" Deleted Successfully!!"})
        except Book.DoesNotExist:
            return ({"data":None, "code":status.HTTP_404_BAD_REQUEST, "message":"Does not Exist"})  

#Retrieve all the books.

    def get_all_book(self,request,format=None):
        
        data = Book.objects.all()
        serializer = BookSerializer(data, many=True)
        return ({"data":serializer.data,"code":status.HTTP_200_OK,"message":"OK"})
        
