from django.urls.conf import path
from . import views

urlpatterns = [
    path('', views.index),
    path('check', views.check_numbers),
    path('start_again', views.start_again),
]
