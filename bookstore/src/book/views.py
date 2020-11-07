from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView

from refference_db.models import *
from .models import Book
from .forms import *



class BookListView(ListView):
    """displays a list of all Book objects"""

    template_name = "book/book_list.html"
    model = Book
    queryset = Book.objects.all().order_by('-pk')[:10]

class BookView(DetailView):
    """displays a single Book objects"""

    model = Book
    template_name = "book/book.html"

class CreateBookView(CreateView):
    """creates a single book object"""

    model = Book
    fields = '__all__'
    template_name = 'book/create_book.html'
    success_url = '/'

class UpdateBookView(UpdateView):
    """updates a single book object"""

    model = Book
    fields = '__all__'
    template_name = 'book/update_book.html'
    success_url = '/'

class DeleteBookView(DeleteView):
    model = Book
    template_name = 'book/delete_view.html'
    success_url = '/'