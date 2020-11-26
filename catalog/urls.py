from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('books', BooksList.as_view(), name='books'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book_detail'),
    path('book/create', BookCreateView.as_view(), name='book_create'),
    path('book/<int:pk>/edit/', BookEditView.as_view(), name='book_edit'),
    path('book/<int:pk>/delete', BookDeleteView.as_view(), name='book_delete'),
    path('authors', AuthorsList.as_view(), name='authors'),
    path('author/<int:pk>', AuthorDetailView.as_view(), name='author_detail'),
    path('author/create', AuthorCreateView.as_view(), name='author_create'),
    path('author/<int:pk>/edit', AuthorEditView.as_view(), name='author_edit'),
    path('author/<int:pk>/delete', AuthorDeleteView.as_view(), name='author_delete'),
    path('genres', GenreList.as_view(), name='genres'),
    path('genre/<int:pk>', GenreDetailView.as_view(), name='genre_detail'),
    path('genre/create', GenreCreateView.as_view(), name='genre_create'),
    path('genre/<int:pk>/edit', GenreEditView.as_view(), name='genre_edit'),
    path('genre/<int:pk>/delete', GenreDeleteView.as_view(), name='genre_delete'),
]
