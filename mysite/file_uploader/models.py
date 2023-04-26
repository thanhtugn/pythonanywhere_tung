from django.db import models

# Create your models here.
#from django.forms import ModelForm
#
#TITLE_CHOICES = (
#    ('MR', 'Mr.'),
#    ('MRS', 'Mrs.'),
#    ('MS', 'Ms.'),
#)
#
#class Author(models.Model):
#    name = models.CharField(max_length=100)
#    title = models.CharField(max_length=3, choices= TITLE_CHOICES)
#    birth_day = models.DateField(blank=True, null=True)
#
#class Book(models.Model):
#    name = models.CharField(max_length=100)
#    author = models.ManyToManyField(Author)
#
#class AuthorForm(ModelForm):
#    class Meta:
#        model = Author
#        fields = ['name', 'title', 'birth_date']
#
#class BookForm(ModelForm):
#    class Meta:
#        model = Book
#        fields = ['name', 'authors']
            