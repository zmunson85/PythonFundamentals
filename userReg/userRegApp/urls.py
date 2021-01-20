from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('registration', views.new_user),
    path('success', views.success),
    path('login', views.login),
    path('logout',views.logout),
]
