from rest_framework import serializers
from api.models.userModel import *



class SignupSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = User
        fields = ('id','first_name', 'last_name','phone_no','branch', 'email','password')


class CreateUserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = User
        fields = ('id','first_name', 'last_name','phone_no','branch', 'email','password')


    def create(self, validated_data):
        signup_obj=User()
        signup_obj.email = validated_data['email']
        signup_obj.first_name = validated_data['first_name']
        signup_obj.last_name = validated_data['last_name']
        signup_obj.set_password(validated_data['password'])
        signup_obj.save()  

        return signup_obj  

    def update(self, instance, valdiated_data):
        instance.email = valdiated_data.get("email", None)
        instance.first_name = valdiated_data.get("first_name", None)
        instance.last_name = valdiated_data.get("last_name", None)
        instance.password = valdiated_data.get("password", None)
        instance.save()

        return instance

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']
