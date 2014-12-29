from django.db import models
from django.contrib.auth.models import AbstractUser

class Book(models.Model):
    bid = models.AutoField(primary_key = True)
    isbn = models.CharField(max_length=100)
    name = models.CharField(max_length=2000)
    description = models.CharField(max_length=2000)
    publish_date = models.DateField()

    def get_show_data(self):
        return {}.update({'book_isbn': self.isbn, 'book_name': self.name, 'book_description': self.description})

class Order(models.Model):
    oid = models.AutoField(primary_key = True)

class Account(AbstractUser):
    address = models.TextField()
    orders = models.ManyToManyField(Order)

