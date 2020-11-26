from django.db import models
from django.urls import reverse


class Author(models.Model):
    FirstName = models.CharField(max_length=25)
    Surname = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50, blank=True)
    Birthday = models.DateField(blank=True, null=True)
    Gender = models.BooleanField()

    def __str__(self):
        return '{} {} {}'.format(self.Surname, self.FirstName, self.LastName)


    def get_absolute_url(self):
        """
        Возвращает URL-адрес для доступа к конкретному автору.
        """
        return reverse('author_detail', kwargs={'pk': self.id})


    class Meta:
        ordering = ['Surname']


class Genre(models.Model):
    """
    Модель, в которой представлены жанры книг
    """
    name = models.CharField(max_length=50, unique=True, help_text="Укажите жанр книги")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('genre_detail', kwargs={'pk': self.id})

class Book(models.Model):
    isbn = models.CharField('ISBN', max_length=25, unique=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    genre = models.ManyToManyField(Genre)
    YearEdition = models.CharField(blank=True, max_length=4)
    author = models.ManyToManyField('Author')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Возвращает URL-адрес для доступа к конкретному экземпляру книги.
        """
        return reverse('book_detail', kwargs={'pk': self.id})


    def display_genre(self):
        return ', '.join([genre.name for genre in self.genre.all()])

    display_genre.short_description = 'Genre'

    def display_author(self):
        return ', '.join([author.__str__() for author in self.author.all()])

    display_author.short_description = 'Author'

    class Meta:
        ordering = ['title']
