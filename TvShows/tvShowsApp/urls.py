from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.all_shows),
    path('shows/new', views.add_show_template),
    path('shows/create', views.create_show),
    path('shows/<int:show_id>', views.show_info_template),
    path('shows/<int:show_id>/edit', views.edit_info_from_info_template),
    path('shows/<int:show_id>/update', views.update_info_template),
    path('update_page/<int:show_id>/update', views.update_info),
    path('delete/<int:show_id>', views.delete_show),
]

