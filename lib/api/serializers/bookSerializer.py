from rest_framework import serializers
from api.models.bookModel import *




class BookSerializer(serializers.ModelSerializer):

   

    id = serializers.IntegerField(required = False)

  

    class Meta:
        model = Book
        fields = ('id','book_name','book_author')