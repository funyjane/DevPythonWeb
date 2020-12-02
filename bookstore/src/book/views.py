from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from django.db.models import Q
from django.urls import reverse_lazy
import requests

from refference_db.models import *
from .models import Book
from .forms import *




class BookListView(ListView):
    """displays a list of all Book objects"""

    template_name = "book/main_page.html"
    model = Book
    paginate_by = 12

class BookView(DetailView):
    """displays a single Book objects"""

    newdeals = Book.objects.all().order_by('-pk')[:4]
    extra_context = {'newdeals':newdeals}
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


class MainPageView(ListView):
    """displays a main page"""

    template_name = "book/main_page.html"
    model = Book
    queryset = Book.objects.all().order_by('-pk')[:10]

    def get_current_rate(self):
        result = requests.get('https://www.nbrb.by/api/exrates/rates/145')
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fresh_arrivals"] = Book.objects.order_by('-pk')[:6]
        context["most_popular"] = Book.objects.order_by('-rating')[:6]
        context['user'] = self.request.user
        context['genres'] = Genre.objects.all()
        try:
            page = self.get_current_rate()
            rate = page.json()['Cur_OfficialRate']
            context['rate'] = rate
            
        except requests.exceptions.ConnectionError:
            requests.status_code = "Connection refused"
        return context

class BookSearch(ListView):
    model = Book
    template_name = 'book/book_catalog.html'
    paginate_by = 12
    
    def get_template_names(self):
        search = self.request.GET.get('search')
        books = Book.objects.filter(Q(title__icontains=search))
        if not books.exists():
            template_name = "catalog/empty.html"
            return ["catalog/empty.html"]
        else:
            return [self.template_name]


    def get_queryset(self):
        search = self.request.GET.get('search')
        books = Book.objects.filter(Q(title__icontains=search))
        return books
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_info = str(self.request.GET.get('search'))
        context["search"] = search_info
        return context
    
