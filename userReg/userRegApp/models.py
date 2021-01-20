from userReg.settings import AUTH_PASSWORD_VALIDATORS
from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def validator(self,postData):
        errors={}

        # validating email
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern
            errors['email'] = "Invalid email address!"
        #if email exist
        mailExist = User.objects.filter(email = postData['email'])
        if mailExist:
            errors['email_exist']= "That email exists"
        # validating the names
        if len(postData['first_name']) < 2:
            errors["first_name"] = "Entry must be more than two characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Entery must be more than 2 characters"
        #validating password characters
        if len(postData['password']) < 8:
            errors["password"] = "Please enter at least 8 characters"
        #validating the fields from password and confirm password
        if postData['password'] != postData ['confirm_pass']:
            errors["confirm_pass"] = "Your entries must match"
        if len(postData['password']) < 8:
            errors["login_password"] = "Inccorect Password"
        return errors


    def login_validator(self, postData):
            errors = {}
            # validating email
            EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
            # test whether a field matches the pattern
            if not EMAIL_REGEX.match(postData['email_login']):
                errors['email_login'] = "Not a valid email!"
            #if email exist
            emailExist = User.objects.filter(email=postData['email_login'])
            if not emailExist:
                errors['email_notfound'] = "This email does not exist"

            return errors




class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=255)
    updated_at = models.DateTimeField(auto_now = True)
    objects =UserManager()
