from django.urls import path
from . import views
urlpatterns = [
    path('', views.root),
    path('blogs', views.index),
    path('', views.create),
    path('new', views.new),
    path('blogs/<int:blog_id>',views.showblogs),
    path('css/<str:filename>.css', views.css_renderer),
]

