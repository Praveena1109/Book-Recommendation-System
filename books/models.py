from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    ISBN = models.CharField(max_length=200, null=True)
    AvgBookRating = models.FloatField(null=True)
    NumberOfRating = models.CharField(max_length=200, null=True)
    BookTitle = models.CharField(max_length=200, null=True)
    BookAuthor = models.CharField(max_length=200, null=True)
    YearOfPublication = models.CharField(max_length=200, null=True)
    Publisher = models.CharField(max_length=200, null=True)
    new_score = models.FloatField(null=True)
    Description = models.CharField(max_length=3000, null=True)
    Genre = models.CharField(max_length=200, null=True)
    Previewlink = models.CharField(max_length=200, null=True)
    Image = models.CharField(max_length=200, null=True)
    favourites = models.ManyToManyField(User, related_name='favourite',default=None, blank=True)
    readlist = models.ManyToManyField(User, related_name='readlist',default=None, blank=True)
    # def__str__(self):
    #     return self.BookTitle

# class Favourite(models.Model):
#     user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
#     book = models.ForeignKey(Book, null=True, on_delete=models.CASCADE)
#
#     class Meta:
#         unique_together=[['user', 'book']]


# class ForYou(models.Model):
#     book = models.ForeignKey(Book, null=True, on_delete=models.SET_NULL)
#     user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
