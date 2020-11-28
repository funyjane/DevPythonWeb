"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from book.views import *
from refference_db.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', include('authentication.urls', namespace='profile')),

    path('book/<int:pk>/', BookView.as_view(), name = 'book-view'),
    path('book/create/', CreateBookView.as_view(), name = 'book-create'),
    path('book/update/<int:pk>/', UpdateBookView.as_view(), name = 'book-update'),
    path('book/delete/<int:pk>/', DeleteBookView.as_view(), name = 'book-delete'),

    path('genre/', GenreListView.as_view(), name = 'genre-list-view'),
    path('genre/<int:pk>/', GenreView.as_view(), name = 'genre-view'),
    path('genre/create/', CreateGenreView.as_view(), name = 'genre-create'),
    path('genre/update/<int:pk>/', UpdateGenreView.as_view(), name = 'genre-update'),
    path('genre/delete/<int:pk>/', DeleteGenreView.as_view(), name = 'genre-delete'),
    
    path('author/', AuthorListView.as_view(), name = 'author-list-view'),
    path('author/<int:pk>/', AuthorView.as_view(), name = 'author-view'),
    path('author/create/', CreateAuthorView.as_view(), name = 'author-create'),
    path('author/update/<int:pk>/', UpdateAuthorView.as_view(), name = 'author-update'),
    path('author/delete/<int:pk>/', DeleteAuthorView.as_view(), name = 'author-delete'),
    
    path('series/', SeriesListView.as_view(), name = 'series-list-view'),
    path('series/<int:pk>/', SeriesView.as_view(), name = 'series-view'),
    path('series/create/', CreateSeriesView.as_view(), name = 'series-create'),
    path('series/update/<int:pk>/', UpdateSeriesView.as_view(), name = 'series-update'),
    path('series/delete/<int:pk>/', DeleteSeriesView.as_view(), name = 'series-delete'),
    
    path('publisher/', PublisherListView.as_view(), name = 'publisher-list-view'),
    path('publisher/<int:pk>/', PublisherView.as_view(), name = 'publisher-view'),
    path('publisher/create/', CreatePublisherView.as_view(), name = 'publisher-create'),
    path('publisher/update/<int:pk>/', UpdatePublisherView.as_view(), name = 'publisher-update'),
    path('publisher/delete/<int:pk>/', DeletePublisherView.as_view(), name = 'publisher-delete'),
    
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
    
    path('cart/', include('orders.urls', namespace = 'orders')),
    path('catalog/', include('catalog.urls')),
    
    path('', BookListView.as_view(), name = 'main-manager')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)