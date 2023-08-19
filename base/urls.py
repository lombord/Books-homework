from django.urls import path

from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    # books urls
    path('books/', BooksView.as_view(), name='books'),
    path('add-book/', AddBookView.as_view(), name='add_book'),
    path('edit-book/<slug:slug>/', EditBookView.as_view(), name='edit_book'),
    path('delete-book/<slug:slug>/', DeleteBookView.as_view(), name='delete_book'),
    path('book/<slug:slug>/', BookView.as_view(), name="book"),

    # author urls
    path("add-author/", AddAuthorView.as_view(), name="add_author"),

    # genre urls
    path("add-genre/", AddGenreView.as_view(), name="add_genre"),
]
