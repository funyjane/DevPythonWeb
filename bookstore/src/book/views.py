from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Book
from .forms import CreateBookForm


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
    """creates a single object"""
    
    if request.method == 'POST':
        form = CreateBookForm(data=request.POST)
        if form.is_valid():
            book_name = form.cleaned_data.get('name')
            Book.objects.create(title=book_name)
            return HttpResponseRedirect('/')
    else:
        form = CreateBookForm()
    return render(
        request,
        template_name='book/create_book.html',
        context={'form':form}
    )
