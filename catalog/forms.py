from django import forms
from .models import Author, Book, Genre

class AuthorModelForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = '__all__'
        labels = {'FirstName': 'Имя',
                  'Surname': 'Фамилия',
                  'LastName': 'Отчество или второе имя',
                  'Birthday': 'Дата рождения',
                  'Gender': 'Пол',
                  }
        gender = [(0, 'Женщина'), (1, 'Мужчина')]
        widgets = {
            'FirstName': forms.TextInput(attrs={'class': 'form-control'}),
            'Surname':  forms.TextInput(attrs={'class': 'form-control'}),
            'LastName':  forms.TextInput(attrs={'class': 'form-control'}),
            'Gender': forms.RadioSelect(choices=gender, attrs={'class': 'form-check-input position-static'}),
            'Birthday': forms.DateInput(attrs={'class': 'form-control'})
        }


class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        labels = {
            'title': 'Название',
            'isbn': 'ISBN',
            'description': 'Описание',
            'genre': 'Жанр',
            'author': 'Автор',
            'YearEdition': 'Год издания',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'author': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'YearEdition': forms.TextInput(attrs={'class': 'form-control'}),
        }


class GenreModelForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'
        labels = {'name': 'Название'}
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'})}