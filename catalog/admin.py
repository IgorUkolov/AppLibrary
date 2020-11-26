from django.contrib import admin
from .models import Author, Genre, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('Surname', 'FirstName', 'LastName', 'Birthday')
    fields = [('FirstName', 'Surname')]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_author', 'display_genre')
    list_filter = ('YearEdition', 'title')

    # fieldsets = (
    #     (None, {
    #         'fields': ('title', 'description')
    #     }),
    # )



