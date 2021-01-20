from enum import auto
from django.db import models

# Create your models here.

class ShowManager(models.Manager):

    def validator( self, postData):
        errors ={}


        if len(postData['title']) <2:
            errors["title"] = "Title is required"

        if len(postData['network']) <2:
            errors["network"] = "Network Must Be Compled to Submit"

        if len(postData['date']) ==0:
            errors["date"] = "You must Include the Date To Submit"

        if len(postData['description']) <2:
            errors["description"] = "You must include A Description to Submit"

        showExists= Show.objects.filter(title=postData["title"])
        if showExists:
            errors ["titleExists"] = "Show Already exits"

        return errors
        
class Show(models.Model):
    title = models.CharField(max_length=100)
    network = models.CharField(max_length=100)
    date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShowManager()

    # def __repr__(self):
    #     return f"Show: {self.title} {self.network}"

