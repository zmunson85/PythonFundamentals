from django import http,forms
from django.http.response import JsonResponse
from django.shortcuts import redirect, render, HttpResponse, render, render_to_response

# Create your views here.


def root(req):
    return render(req, 'blog.html')

def blogs(req):
    return render("DISPLAY BLOGS LATER")


def index(req):
    return HttpResponse("BLOG LIST HERE")

def create(req):
    return HttpResponse('/')

def new(req):
    return render(req, 'index.html')


def showblogs(req):
    return HttpResponse( f'Placeholder for blog! ID: {blog_id}', num=num),



def css_renderer(request, filename):
    return render(request, filename + '.css', {}, content_type="text/css,")
