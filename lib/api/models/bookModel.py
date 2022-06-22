from django.db import models
from .userModel import User


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=100,null=True,blank=True)
    book_author = models.CharField(max_length=100,null=True,blank=True)
    

    def __unicode__(self):
        return self.id
        

    class Meta: 
        db_table = 'Book'
        indexes = [
            models.Index(fields=['id'])
        ]