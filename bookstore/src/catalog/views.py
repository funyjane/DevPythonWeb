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

class ReturnView(TemplateView):
    template_name = "catalog/returns.html"

class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"

class ShippingView(TemplateView):
    template_name = "catalog/shipping.html"

class AboutView(TemplateView):
    template_name = "catalog/about.html"

class ErrorView(TemplateView):
    template_name = "catalog/error.html"

class EmptyView(TemplateView):
    template_name = "catalog/empty.html"


    