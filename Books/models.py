from django.db import models

class Book(models.Model):
    name = models.TextField()
    isbn = models.TextField()
    bid = models.IntegerField()

# Create your models here.
