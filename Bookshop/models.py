from django.db import models
from django.contrib.auth.models import AbstractUser

class BookHotestManager(models.Manager):
    def get_hotest_books(self):
        return super(BookManager, self).get_queryset()

class BookLatestManager(models.Manager):
    def get_hotest_books(self):
        return super(BookManager, self).get_queryset()

class Book(models.Model):
    bid = models.AutoField(primary_key = True)
    isbn = models.CharField(max_length=100)
    name = models.CharField(max_length=2000)
    description = models.CharField(max_length=2000)
    publish_date = models.DateField()
    price = models.FloatField()
    publisher = models.CharField(max_length=1000)
    page_number = models.IntegerField()
    language = models.CharField(max_length=200)

    objects = models.Manager()
    hotest_objects = BookHotestManager() 
    latest_objects = BookLatestManager() 

    def __unicode__(self):
        return self.name


class Account(AbstractUser):
    address = models.TextField()
    recommend_books = models.ManyToManyField(Book, related_name='accounts_should_recommend_this_book')
    shop_cart = models.ManyToManyField(Book, through='ShopCart', through_fields=('aid', 'bid'))

    def __unicode__(self):
        return self.username + ' ' + self.address

States = (
        ('u', 'uncomplete'),
        ('p', 'processing'),
        ('c', 'complete')
        )

class Order(models.Model):
    oid = models.AutoField(primary_key = True)
    state = models.CharField(max_length=20, choices = States)
    aid = models.ForeignKey(Account)
    books = models.ManyToManyField(Book, through='OrderBookRelation', through_fields=('oid', 'bid'))
    date = models.DateTimeField()

    class Meta:
        ordering = ['-date']

    def __unicode__(self):
        return self.get_description()

    def get_description(self):
        description = ""
        if len(self.books.all()) == 0:
            description += 'empty'
        else:
            relation = OrderBookRelation.objects.filter(oid=self)
            description += relation[0].bid.name + '*' + str(relation[0].number_of_book)
            for book in relation[1 : ]:
                description += ' + ' + book.bid.name + '*' + str(book.number_of_book)
        return description 

    def get_totalprice(self):
        total_price = 0
        relation = OrderBookRelation.objects.filter(oid=self)
        for book in relation:
            total_price += book.bid.price * book.number_of_book
        return total_price


class OrderBookRelation(models.Model):
    oid = models.ForeignKey(Order)
    bid = models.ForeignKey(Book)
    number_of_book = models.IntegerField()

class ShopCart(models.Model):
    aid = models.ForeignKey(Account)
    bid = models.ForeignKey(Book)
    number_of_book = models.IntegerField()

