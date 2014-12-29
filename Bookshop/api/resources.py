from tastypie.resources import ModelResource
from Bookshop.models import Book

class BookResource(ModelResource):
    class Meta:
        queryset = Book.objects.all()
        allowed_methods = ['get']
