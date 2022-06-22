from rest_framework import serializers
from api.models.registerModel import *


class RegisterSerializer(serializers.ModelSerializer):
    
    id = serializers.IntegerField(required = False)
    class Meta:
        model = Register
        fields = ('id','issued_date','end_date','no_of_days','fine')


class GetSerializer(serializers.ModelSerializer):
    
    id = serializers.IntegerField(required = False)
    class Meta:
        model = Register
        fields = ('id','issued_date','end_date','no_of_days','fine')