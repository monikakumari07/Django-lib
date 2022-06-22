from django.db import models
from django.utils import timezone
from .userModel import User
from .bookModel import Book
from datetime import date

class Register(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,null=True,on_delete=models.CASCADE)
    issued_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True)
    no_of_days = models.IntegerField(default= 0)
    fine = models.IntegerField(null=True,blank=True)
    

    def __unicode__(self):
        return self.id
        

    class Meta: 
        db_table = 'Register'
        indexes = [
            models.Index(fields=['id'])
        ]