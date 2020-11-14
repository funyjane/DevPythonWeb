from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from book.models import *
from refference_db.models import *

class CatalogGenreView(ListView):
    """displays cards with Genres objects"""
    
    model = Genre
    newdeals = Book.objects.all().order_by('-pk')[:6]
    extra_context = {'newdeals':newdeals}
    template_name = "catalog/catalog_list.html"
    