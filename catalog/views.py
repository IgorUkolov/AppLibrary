from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


from .forms import AuthorModelForm, BookModelForm, GenreModelForm
from .models import Book, Author, Genre
from .utils import ObjectCreateMixin, ObjectDeleteMixin, ObjectEditMixin



def main(request):
    count_book = Book.objects.count()
    count_author = Author.objects.count()
    count_genre = Genre.objects.count()

    return render(
        request,
        'catalog/index.html',
        context={'count_book': count_book, 'count_author': count_author, 'count_genre': count_genre, },
    )


class BooksList(ListView):
    model = Book
    template_name = 'catalog/books_list.html'
    context_object_name = 'books_list'

class BookDetailView(DetailView):
    model = Book


class BookCreateView(ObjectCreateMixin, View):
    form_model = BookModelForm
    template_name = 'catalog/create_form.html'


class BookEditView(LoginRequiredMixin, ObjectEditMixin, View):
    model = Book
    form_model = BookModelForm
    template = 'catalog/create_form.html'
    # login_url = '/login/'
    # redirect_field_name = 'redirect_to'


class BookDeleteView(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Book
    template = 'catalog/author_delete.html'
    success_url = 'books'


class AuthorsList(ListView):
    model = Author
    template_name = 'catalog/authors_list.html'
    context_object_name = 'authors_list'



class AuthorDetailView(DetailView):
    model = Author

    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и иниуиализируем ее некоторым значением
        context['books'] = self.object.book_set.all()
        return context


class AuthorCreateView(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = AuthorModelForm
    template_name = 'catalog/create_form.html'


class AuthorDeleteView(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Author
    template = 'catalog/author_delete.html'
    success_url = 'authors'


class AuthorEditView(LoginRequiredMixin, ObjectEditMixin, View):
    model = Author
    template = 'catalog/create_form.html'
    form_model = AuthorModelForm


class GenreList(ListView):
    model = Genre
    template_name = 'catalog/genres_list.html'


class GenreDetailView(DetailView):
    model = Genre

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get(self.pk_url_kwarg)
        # В первую очередь получаем базовую реализацию контекста
        context = super(GenreDetailView, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и иниуиализируем ее некоторым значением

        context['books_count'] = self.object.book_set.count()

        context['books'] = self.object.book_set.all()

        return context


class GenreCreateView(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = GenreModelForm
    template_name = 'catalog/create_form.html'


class GenreEditView(LoginRequiredMixin, ObjectEditMixin, View):
    model = Genre
    form_model = GenreModelForm
    template = 'catalog/create_form.html'


class GenreDeleteView(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Genre
    template = 'catalog/author_delete.html'
    success_url = 'genres'

