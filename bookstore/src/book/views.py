from django.shortcuts import render
from django.http import HttpResponse

from .models import Book

def show_books_list_view(request):
    """Returns a list of Book objects"""
    
    books = Book.objects.all()
    con = {'books_key':books}
    return render(request, template_name="book/book_list.html", context=con)

def show_book_by_pk(request, book_id):
    """Returns a single object"""
    #book/12/
    book_obj = Book.objects.get(pk=book_id)
    con = {'book':book_obj}
    return render(request, template_name="book/book.html", context=con)
