from rest_framework import status
from datetime import timedelta
from rest_framework.response import Response
from api.models.registerModel import *
from api.serializers import RegisterSerializer,GetSerializer

class RegisterSerivce():
    def __int__(self):
        pass

#Register entry 
   

    def create_Register(self,request,format=None):
        
                serializer=RegisterSerializer(data=request.data)
                no_of_days = int(request.data["no_of_days"])
                if serializer.is_valid():
                    serializer.save()
                    ad_obj=Register.objects.get(id=serializer.data.get("id"))
                    ad_obj.end_date= ad_obj.issued_date + timedelta(days=no_of_days)
                    ad_obj.save()
                    serializer = GetSerializer(ad_obj)
                    
                    # print("------------------>>>>>>>>>>>>")
                    return({"data":serializer.data, "code":status.HTTP_200_OK, "message":"REGISTER_SUCCESSFULLY"})
                else:
                   
                    return ({"data":serializer.errors, "code":status.HTTP_400_BAD_REQUEST, "message":"BAD_REQUEST"})

#Update a Register
        
    def update_Register(Self, request, pk, format=None):
        try:
            subscription = Register.objects.get(id=pk)
            serializer = RegisterSerializer(subscription,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return ({"data":serializer.data, "code":status.HTTP_200_OK, "message":"OK"})
            return ({"data":serializer.data, "code":status.HTTP_400_BAD_REQUEST,"message":"Bad Request"}) 
        except Register.DoesNotExist:
            return ({"data":None, "code":status.HTTP_400_BAD_REQUEST,"message":"Record Not Found"})

#Delete a Register.

    def delete_Register(self, request, pk, format=None):
        try:
            subscription = Register.objects.get(id=pk)
            subscription.delete()
            return({"data":None, "code":status.HTTP_200_OK, "message":" Deleted Successfully!!"})
        except Register.DoesNotExist:
            return ({"data":None, "code":status.HTTP_404_BAD_REQUEST, "message":"Does not Exist"})  

#Retrieve all the Register.

    def get_all_Register(self,request,format=None):
        data = Register.objects.all()
        serializer = RegisterSerializer(data, many=True)
        return({"data":serializer.data,"code":status.HTTP_200_OK,"message":"OK"})