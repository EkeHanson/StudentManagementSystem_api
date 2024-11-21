from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20, unique=True)
    available_copies = models.IntegerField(default=1)

    def __str__(self):
        return self.title
