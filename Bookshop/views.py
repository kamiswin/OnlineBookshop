from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import AccountForm
from .models import Book, Order, ShopCart, OrderBookRelation
from django.utils import timezone
import os

def specification(request, m_isbn):
    try:
        book = Book.objects.get(isbn=m_isbn)
    except:
        return HttpResponseRedirect('/')
    next_url = request.GET.get('next', '')
    if next_url == '':
        return render(request, 'specification.html', {'book': book})
    else:
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/?next=' + request.path)
        isbn = request.GET.get('book_isbn', '')
        if isbn != '':
            book = Book.objects.get(isbn=isbn)
            if book not in request.user.shop_cart.all():
                r = ShopCart.objects.create(aid=request.user, bid=book, number_of_book=1)
            print request.user.shop_cart.all()
        return HttpResponseRedirect(next_url)


@login_required
def show_login(request):
    return HttpResponseRedirect('/')

def register_show(request):
    return render(request, 'registration/register.html', {'form': AccountForm})

@login_required
def account(request):
    uncomplete_orders = request.user.order_set.filter(state='u')
    complete_orders = request.user.order_set.filter(state='c')
    processing_orders = request.user.order_set.filter(state='p')
    return render(request, 'account.html', locals())

def help(request):
    return render(request, 'help.html')

@login_required
def confirm_buy(request):
    order = Order(state='u', aid=request.user)
    order.save()
    return 

@login_required
def generate_order(request):
    return render(request, 'order.html')

@login_required
def pay(request):
    total_number = request.POST.get('book_total_number', '')
    if total_number == '':
        return HttpResponse('empty shop cart')
    order_list = []
    for it in xrange(int(total_number)):
        book = {}
        book['checked'] = request.POST.get('check' + str(it), 'not_checked')
        book['number']  = request.POST.get('number' + str(it), '')
        book['isbn']    = request.POST.get('book' + str(it), '')
        order_list.append(book)
    order = Order(state='u', aid=request.user, date=timezone.now())
    order.save()
    for item in order_list:
        if item['checked'] != 'not_checked':
            book = Book.objects.get(isbn=item['isbn'])
            OrderBookRelation.objects.create(oid=order, bid=book, number_of_book=item['number'])
    request.user.shop_cart.clear()
    return HttpResponse('success')

def search_page(request):
    keywords = request.GET.get('q', '')
    if keywords == '':
        books = Book.objects.all()
    else:
        books = Book.objects.filter(name__icontains=keywords)
    return render(request, 'search.html', { 'last_content': keywords, 'all_books': books })
