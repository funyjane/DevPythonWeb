from django.urls import path
from django.views.generic.base import View

from book.views import *
from refference_db.views import *
from .views import *

app_name = 'orders'
urlpatterns = [
    path('', CartView.as_view(), name = 'cart'),
    path('update-cart', CartUpdateView.as_view(), name = 'update'),
    path('delete-book-in-cart/<int:pk>', DeleteBookInCart.as_view(), name = 'book-in-cart-del'),
    path('order/', CreateOrderView.as_view(), name='create-order'),
    path('history/', HistoryDetailView.as_view(), name='history')

]
