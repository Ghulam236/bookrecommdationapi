
from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    publication_date = models.DateField()
    

class UserInteraction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    liked = models.BooleanField(default=False)
    comment = models.TextField(blank=True, null=True)
    

