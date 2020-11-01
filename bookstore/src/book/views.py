from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Book
from .forms import *


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

def create_book_view (request):
    """creates a single book object"""
    
    if request.method == 'POST':
        form = CreateBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = CreateBookForm()
    return render(
        request,
        template_name='book/create_book.html',
        context={'form':form}
    )

def update_book_view (request, pk):
    """updates a single book object"""
    
    if request.method == 'POST':
        form = UpdateBookForm(request.POST, request.FILES)
        if form.is_valid():
            old_book = Book.objects.get(pk=pk)
            new_book = UpdateBookForm(request.POST, request.FILES, instance=old_book)
            new_book.save()
            return HttpResponseRedirect('/')
    else:
        book = Book.objects.get(pk=pk)
        form = UpdateBookForm(instance=book)
        return render(
            request, 
            template_name='book/update_book.html', 
            context={'form':form}
            )

def delete_book_view(request, pk):
    if request.method == "POST":
        book = Book.objects.get(pk=pk)
        book.delete()
        return HttpResponseRedirect('/')
    else:
        book = Book.objects.get(pk=pk)
    return render(request, template_name='book/delete_view.html', context={'book': book, 'header': book.title})