from django.contrib import admin
from . import models

admin.site.register(models.Book)
admin.site.register(models.Account)
admin.site.register(models.Order)
admin.site.register(models.OrderBookRelation)
admin.site.register(models.ShopCart)
# Register your models here.
