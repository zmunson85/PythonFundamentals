from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

class Ninjas(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    dojo= models.ForeignKey("dojo", related_name="ninjas", on_delete= models.CASCADE)