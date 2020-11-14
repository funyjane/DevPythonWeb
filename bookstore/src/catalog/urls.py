from django.urls import path

from book.views import *
from refference_db.views import *
from .views import *

urlpatterns = [
    path('', CatalogGenreView.as_view(), name = 'catalog')
]
