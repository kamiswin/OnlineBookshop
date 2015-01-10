from django.shortcuts import render
from Bookshop.models import Book, Account

def home(request):
    hotest_books = Book.hotest_objects.get_hotest_books()
    latest_books = Book.latest_objects.get_latest_books()
    if request.user.is_authenticated():
        recommend_books = request.user.recommend_books.all()
        print recommend_books
    return render(request, 'index.html', locals())
