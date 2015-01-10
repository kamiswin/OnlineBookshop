from django.db import models
from django.contrib.auth.models import AbstractUser
import base64
import random

class BookHotestManager(models.Manager):
    def get_hotest_books(self):
        return super(BookHotestManager, self).get_queryset()[:4]

class BookLatestManager(models.Manager):
    def get_latest_books(self):
        return super(BookLatestManager, self).get_queryset()[:4]

class OrderDecryptManager(models.Manager):
    def get_encrypt_order(self, oid):
        key = base64.b64decode(oid)
        t_oid = int(key[: key.find('|')])
        return super(OrderDecryptManager, self).get_queryset().get(oid=t_oid)

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
    related_books = models.ManyToManyField("self")
    cover_image = models.CharField(max_length=100)

    objects = models.Manager()
    hotest_objects = BookHotestManager() 
    latest_objects = BookLatestManager() 

    def __unicode__(self):
        return self.name

    def get_header_description(self):
        rt = self.description
        if len(rt) > 200:
            rt = rt[:200] + '...'
        return rt

    def get_related_books(self):
        books = self.related_books.all()
        return random.sample(books, 4)

class Account(AbstractUser):
    address = models.TextField()
    recommend_books = models.ManyToManyField(Book, related_name='accounts_should_recommend_this_book')
    shop_cart = models.ManyToManyField(Book, through='ShopCart', through_fields=('aid', 'bid'))
    comments = models.ManyToManyField(Book, related_name='comments_on_this_book', through='Comment', through_fields=('aid', 'bid'))

    def __unicode__(self):
        return self.username + ' ' + self.address

    def get_recommend_books(self):
        orders = self.order_set.all()
        all_related = []
        for order in orders:
            for book in order.books.all():
                all_related.extend(book.related_books.all())
        
        length = 4 if (len(all_related) > 4) else len(all_related)
        return random.sample(all_related, length)

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
    decrypt_objects = OrderDecryptManager()

    class Meta:
        ordering = ['-date']

    def __unicode__(self):
        return self.get_description()

    def get_id(self):
        return base64.b64encode(str(self.oid) + '|' + str(self.date))

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

class Comment(models.Model):
    bid = models.ForeignKey(Book)
    aid = models.ForeignKey(Account)
    content = models.CharField(max_length=2000)
    date = models.DateTimeField()

    def get_user_info(self):
        return self.aid.username
