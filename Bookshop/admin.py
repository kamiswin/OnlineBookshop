from django.contrib import admin
from . import models

admin.site.register(models.Book)
admin.site.register(models.Account)
admin.site.register(models.Order)
# Register your models here.
