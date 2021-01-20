from django.shortcuts import render, redirect
from userRegApp.models import User
from django.contrib import messages
import bcrypt
import re

# Create your views here.


def index(request):
    return render(request, "index.html")

def new_user(request):
    errors = User.objects.validator(request.POST)

    if errors:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/")

    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  # create the hash
        print(pw_hash)
        User.objects.create(first_name=first_name,last_name=last_name, email=email, password=pw_hash)
        user= User.objects.last()
        request.session['userid']= user.id
        return redirect("/success")

def success(request):
    if 'userid' in request.session:
        user = User.objects.get(id=request.session['userid'])
        context = {
        'user': user
        }
        return render(request, "success.html", context)
    return redirect("/")    

def login(request):
    errors = User.objects.login_validator(request.POST)
    
    if errors:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/')

    user = User.objects.filter(email=request.POST['email_login']) 
    if user: # note that we take advantage of truthiness here: an empty list will return false
        logged_user = user[0] 
        print(request.POST['password_login'])
        if bcrypt.checkpw(request.POST['password_login'].encode(), logged_user.password.encode()):
            # if we get True after checking the password, we may put the user id in session
            request.session['userid'] = logged_user.id
            # never render on a post, always redirect!
            return redirect('/success')
    messages.error(request,"incorrect password", extra_tags='password_notfound')
    return redirect('/')
    



def logout(request):
    request.session.clear()
    return redirect('/')

