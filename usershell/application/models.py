from django.db import models

class User(models.Model):
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    email_address= models.EmailField()
    age= models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)


    def __repr__(self):
        return f"User: id:{self.id} {self.first_name}{self.last_name}"