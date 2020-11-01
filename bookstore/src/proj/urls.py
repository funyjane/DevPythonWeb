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
from django.urls import path
from hello_world.views import hello_world
from django.conf import settings
from django.conf.urls.static import static

from book.views import *
from refference_db.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/<int:book_id>/', show_book_by_pk),
    path('book/create/', create_book_view),
    path('book/update/<int:pk>/', update_book_view),
    path('book/delete/<int:pk>/', delete_book_view),

    path('genre/', genre_list_view),
    path('genre/<int:pk>/', genre_view),
    path('genre/create/', create_genre_view),
    path('genre/update/<int:pk>/', update_genre_view),
    path('genre/delete/<int:pk>/', delete_genre_view),
    
    path('author/', author_list_view),
    path('author/<int:pk>/', author_view),
    path('author/create/', create_author_view),
    path('author/update/<int:pk>/', update_author_view),
    path('author/delete/<int:pk>/', delete_author_view),
    
    path('series/', series_list_view),
    path('series/<int:pk>/', series_view),
    path('series/create/', create_series_view),
    path('series/update/<int:pk>/', update_series_view),
    path('series/delete/<int:pk>/', delete_series_view),
    
    path('publisher/', publisher_list_view),
    path('publisher/<int:pk>/', publisher_view),
    path('publisher/create/', create_publisher_view),
    path('publisher/update/<int:pk>/', update_publisher_view),
    path('publisher/delete/<int:pk>/', delete_publisher_view),
    
    path('format/', format_list_view),
    path('format/<int:pk>/', format_view),
    path('format/create/', create_format_view),
    path('format/update/<int:pk>/', update_format_view),
    path('format/delete/<int:pk>/', delete_format_view),
    
    path('age/', ageres_list_view),
    path('age/<int:pk>/', ageres_view),
    path('age/create/', create_ageres_view),
    path('age/update/<int:pk>/', update_ageres_view),
    path('age/delete/<int:pk>/', delete_ageres_view),
    
    path('rating/', rating_list_view),
    path('rating/<int:pk>/', rating_view),
    path('rating/create/', create_rating_view),
    path('rating/update/<int:pk>/', update_rating_view),
    path('ratings/delete/<int:pk>/', delete_rating_view),
    path('hello/', hello_world),
    path('', show_books_list_view),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)