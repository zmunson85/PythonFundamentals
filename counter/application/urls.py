from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path('destroy', views.destroy),
    path('plustwo', views.plustwo),
    # path('admin/', admin.site.urls),
]
