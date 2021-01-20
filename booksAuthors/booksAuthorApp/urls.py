from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book),
    path('show_book/<int:book_id>', views.show_info_book),
    path('add_Author/<int:book_id>', views.add_author_to_book),
    path('authors', views.show_author),
    path('add_author', views.add_author),
    path('show_author/<int:author_id>',views.show_author),
    path('add_a_book/<int:author_id>', views.add_book_to_author)
]

