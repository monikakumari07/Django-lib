from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser): 
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100,null=True,blank=True)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    phone_no = models.CharField(max_length=100)
    branch = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    
    created_on= models.DateTimeField(default=timezone.now)
    is_active=models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    token = models.TextField(max_length=255, blank=True)
    

    USERNAME_FIELD ='email'
    REQUIRED_FIELD = ['first_name','last_name' ]