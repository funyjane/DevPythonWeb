from django.urls import path
from .views import *

app_name = 'manager'
urlpatterns = [
    path('order/list/', ManagerOrderList.as_view(), name='order-list'),
    path('order/update/<int:pk>/', ManagerOrderUpdate.as_view(), name='order-update'),
    path('order/delete/<int:pk>/', ManagerOrderDelete.as_view(), name='order-delete'),

    path('author/list/', AuthorList.as_view(), name='author-list'),
    path('author/create/', AuthorCreate.as_view(), name='author-create'),
    path('author/view/<int:pk>/', AuthorView.as_view(), name='author-view'),
    path('author/delete/<int:pk>/', AuthorDelete.as_view(), name='author-delete'),
    path('author/update/<int:pk>/', AuthorUpdate.as_view(), name='author-update'),


    path('series/list/', SeriesList.as_view(), name='series-list'),
    path('series/create/', SeriesCreate.as_view(), name='series-create'),
    path('series/view/<int:pk>/', SeriesView.as_view(), name='series-view'),
    path('series/update/<int:pk>/', SeriesUpdate.as_view(), name='series-update'),
    path('series/delete/<int:pk>/', SeriesDelete.as_view(), name='series-delete'),


    path('genre/list/', GenreList.as_view(), name='genre-list'),
    path('genre/create/', GenreCreate.as_view(), name='genre-create'),
    path('genre/view/<int:pk>/', GenreView.as_view(), name='genre-view'),
    path('genre/update/<int:pk>/', GenreUpdate.as_view(), name='genre-update'),
    path('genre/delete/<int:pk>/', GenreDelete.as_view(), name='genre-delete'),


    path('publisher/list/', PublisherList.as_view(), name='publisher-list'),
    path('publisher/create/', PublisherCreate.as_view(), name='publisher-create'),
    path('publisher/view/<int:pk>/', PublisherView.as_view(), name='publisher-view'),
    path('publisher/update/<int:pk>/', PublisherUpdate.as_view(), name='publisher-update'),
    path('publisher/delete/<int:pk>/', PublisherDelete.as_view(), name='publisher-delete'),

    
    path('format/', FormatListView.as_view(), name = 'format-list-view'),
    path('format/<int:pk>/', FormatView.as_view(), name = 'format-view'),
    path('format/create/', CreateFormatView.as_view(), name = 'format-create'),
    path('format/update/<int:pk>/', UpdateFormatView.as_view(), name = 'format-update'),
    path('format/delete/<int:pk>/', DeleteFormatView.as_view(), name = 'format-delete'),
    
    path('age/', Age_resListView.as_view(), name = 'ageres-list-view'),
    path('age/<int:pk>/', Age_resView.as_view(), name = 'ageres-view'),
    path('age/create/', CreateAge_resView.as_view(), name = 'ageres-create'),
    path('age/update/<int:pk>/', UpdateAge_resView.as_view(), name = 'ageres-update'),
    path('age/delete/<int:pk>/', DeleteAge_resView.as_view(), name = 'ageres-delete'),
    
    path('rating/', RatingListView.as_view(), name = 'rating-list-view'),
    path('rating/<int:pk>/', RatingView.as_view(), name = 'rating-view'),
    path('rating/create/', CreateRatingView.as_view(), name = 'rating-create'),
    path('rating/update/<int:pk>/', UpdateRatingView.as_view(), name = 'rating-update'),
    path('rating/delete/<int:pk>/', DeleteRatingView.as_view(), name = 'rating-delete'),


    path('book/list/', ManagerBookList.as_view(), name='book-list'),
    path('book/create/', ManagerBookCreate.as_view(), name='book-create'),
    path('book/delete/<int:pk>/', ManagerBookDelete.as_view(), name='book-delete'),
    path('book/update/<int:pk>/', ManagerBookUpdate.as_view(), name='book-update'),
    path('book/view/<int:pk>/', ManagerBookView.as_view(), name='book-view'),


    path('customer/list/', CustomersList.as_view(), name='customer-list'),
    path('customer/update/<int:pk>/', CustomerUpdate.as_view(), name='customer-update'),
    path('customer/view/<int:pk>/', CustomerView.as_view(), name='customer-view')

    
]
