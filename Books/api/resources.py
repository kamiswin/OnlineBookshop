from tastypie.resources import ModelResource
from Books.models import Book

class BookResource(ModelResource):
    class Meta:
        queryset = Book.objects.all()
        allowed_methods = ['get']
