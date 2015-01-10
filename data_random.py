from Bookshop.models import *
from django.utils import timezone
import random
import json
import hashlib
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def get_publisher():
    return "Online Bookshop Publisher"

def get_date():
    return timezone.now()

def get_isbn(book):
    print book['book_name']
    mm = hashlib.sha256(book['book_name']).hexdigest()
    return mm[:5] + '-' + mm[5:10] + '-' + mm[10:15]

def get_language():
    languages = ['Chinese', 'English', 'Japanese', 'Spanish', 'Germany']
    return random.choice(languages)

def insert_book():
    books_info = json.load(open('book.json'))

    for book in books_info:
        haha = Book.objects.create(isbn=get_isbn(book), name=book['book_name'], 
                description=book['book_description'],
                publish_date=timezone.now(),
                price=random.randint(20, 200),
                publisher=get_publisher(),
                page_number=random.randint(200, 500),
                language=get_language(),
                cover_image=book['book_image_name'])

def get_recommend_books(this_book, all_books):
    rt = random.sample(all_books, 4)
    while this_book in rt:
        rt = random.sample(all_books, 4)
    return rt

def insert_relations():
    all_books = Book.objects.all()
    for book in all_books:
        recommend_books = get_recommend_books(book, all_books)
        for rbook in recommend_books:
            book.related_books.add(rbook)

if __name__ == '__main__':
    main()
