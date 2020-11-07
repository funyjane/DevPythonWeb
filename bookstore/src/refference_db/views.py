from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from django.http import HttpResponse, HttpResponseRedirect

from .models import *
from .forms import *


class GenreListView(ListView):
    """displays a list of all Genre objects"""

    template_name = "refferences_db/genre_list_view.html"
    model = Genre

class GenreView(DetailView):
    """displays a single Genre objects"""

    model = Genre
    template_name = "refferences_db/genre_view.html"

class CreateGenreView(CreateView):
    """creates a single Genre object"""

    model = Genre
    fields = '__all__'
    template_name = 'refferences_db/create_genre.html'
    success_url = '/genre'

class UpdateGenreView(UpdateView):
    """updates a single Genre object"""

    model = Genre
    fields = '__all__'
    template_name = 'refferences_db/update_genre.html'
    success_url = '/genre'

class DeleteGenreView(DeleteView):
    """deletes a single Genre object"""
    
    model = Genre
    template_name = 'refferences_db/delete_view.html'
    success_url = '/genre'



class AuthorListView(ListView):
    """displays a list of all Author objects"""

    template_name = "refferences_db/author_list_view.html"
    model = Author

class AuthorView(DetailView):
    """displays a single Author objects"""

    model = Author
    template_name = "refferences_db/author_view.html"

class CreateAuthorView(CreateView):
    """creates a single Author object"""

    model = Author
    fields = '__all__'
    template_name = 'refferences_db/create_author.html'
    success_url = '/author'

class UpdateAuthorView(UpdateView):
    """Updates a single Author object"""

    model = Author
    fields = '__all__'
    template_name = 'refferences_db/update_author.html'
    success_url = '/author'

class DeleteAuthorView(DeleteView):
    """deletes a single Author object"""
    
    model = Author
    template_name = 'refferences_db/delete_view.html'
    success_url = '/author'



class SeriesListView(ListView):
    """displays a list of all Series objects"""

    template_name = "refferences_db/series_list_view.html"
    model = Series

class SeriesView(DetailView):
    """displays a single Series objects"""

    model = Series
    template_name = "refferences_db/series_view.html"

class CreateSeriesView(CreateView):
    """creates a single Series object"""

    model = Series
    fields = '__all__'
    template_name = 'refferences_db/create_series.html'
    success_url = '/series'

class UpdateSeriesView(UpdateView):
    """Updates a single Series object"""

    model = Series
    fields = '__all__'
    template_name = 'refferences_db/update_series.html'
    success_url = '/series'

class DeleteSeriesView(DeleteView):
    """deletes a single Series object"""
    
    model = Series
    template_name = 'refferences_db/delete_view.html'
    success_url = '/series'



class PublisherListView(ListView):
    """displays a list of all Publisher objects"""

    template_name = "refferences_db/publisher_list_view.html"
    model = Publisher

class PublisherView(DetailView):
    """displays a single Publisher objects"""

    model = Publisher
    template_name = "refferences_db/publisher_view.html"

class CreatePublisherView(CreateView):
    """creates a single Publisher object"""

    model = Publisher
    fields = '__all__'
    template_name = 'refferences_db/create_publisher.html'
    success_url = '/publisher'

class UpdatePublisherView(UpdateView):
    """Updates a single Publisher object"""

    model = Publisher
    fields = '__all__'
    template_name = 'refferences_db/update_publisher.html'
    success_url = '/publisher'

class DeletePublisherView(DeleteView):
    """deletes a single Publisher object"""
    
    model = Publisher
    template_name = 'refferences_db/delete_view.html'
    success_url = '/publisher'



class FormatListView(ListView):
    """displays a list of all Format objects"""

    template_name = "refferences_db/format_list_view.html"
    model = Format

class FormatView(DetailView):
    """displays a single Format objects"""

    model = Format
    template_name = "refferences_db/format_view.html"

class CreateFormatView(CreateView):
    """creates a single Format object"""

    model = Format
    fields = '__all__'
    template_name = 'refferences_db/create_format.html'
    success_url = '/format'

class UpdateFormatView(UpdateView):
    """Updates a single Format object"""

    model = Format
    fields = '__all__'
    template_name = 'refferences_db/update_format.html'
    success_url = '/format'

class DeleteFormatView(DeleteView):
    """deletes a single Format object"""
    
    model = Format
    template_name = 'refferences_db/delete_view.html'
    success_url = '/format'



class Age_resListView(ListView):
    """displays a list of all Age_res objects"""

    template_name = "refferences_db/ageres_list_view.html"
    model = Age_res

class Age_resView(DetailView):
    """displays a single Age_res objects"""

    model = Age_res
    template_name = "refferences_db/ageres_view.html"

class CreateAge_resView(CreateView):
    """creates a single Age_res object"""

    model = Age_res
    fields = '__all__'
    template_name = 'refferences_db/create_ageres.html'
    success_url = '/age'

class UpdateAge_resView(UpdateView):
    """Updates a single Age_res object"""

    model = Age_res
    fields = '__all__'
    template_name = 'refferences_db/update_ageres.html'
    success_url = '/age'

class DeleteAge_resView(DeleteView):
    """deletes a single Age_res object"""
    
    model = Age_res
    template_name = 'refferences_db/delete_view.html'
    success_url = '/age'



def rating_list_view(request):
    '''displays a list of all rating objects'''

    context = {'ratings': Rating.objects.all()}
    return render(request, template_name='refferences_db/rating_list_view.html', context=context)

def rating_view(request, pk):
    '''displays a single rating object'''

    context = {'rating': Rating.objects.get(pk=pk)}
    return render(request, template_name='refferences_db/rating_view.html', context=context)

def create_rating_view (request):
    """creates a single rating object"""
    
    if request.method == 'POST':
        form = CreateRatingForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rating')
    else:
        form = CreateRatingForm()
    return render(
        request,
        template_name='refferences_db/create_rating.html',
        context={'form':form}
    )

def update_rating_view (request, pk):
    """updates a single rating object"""
    
    if request.method == 'POST':
        form = UpdateRatingForm(data=request.POST)
        if form.is_valid():
            rating_name = form.cleaned_data.get('rating')
            new_rating = Rating.objects.get(pk=pk)
            new_rating.rating = rating_name
            new_rating.save()
            return HttpResponseRedirect('/rating')
    else:
        rating = Rating.objects.get(pk=pk)
        form = UpdateRatingForm(data={'rating':rating.rating})
        return render(
            request, 
            template_name='refferences_db/update_rating.html', 
            context={'form':form}
            )

def delete_rating_view(request, pk):
    if request.method == "POST":
        rating = Rating.objects.get(pk=pk)
        rating.delete()
        return HttpResponseRedirect('/rating')
    else:
        rating = Rating.objects.get(pk=pk)
    return render(request, template_name='refferences_db/delete_view.html', context={'rating': rating, 'header': rating.rating})

class RatingListView(ListView):
    """displays a list of all Rating objects"""

    template_name = "refferences_db/rating_list_view.html"
    model = Rating

class RatingView(DetailView):
    """displays a single Rating objects"""

    model = Rating
    template_name = "refferences_db/rating_view.html"

class CreateRatingView(CreateView):
    """creates a single Rating object"""

    model = Rating
    fields = '__all__'
    template_name = 'refferences_db/create_rating.html'
    success_url = '/rating'

class UpdateRatingView(UpdateView):
    """Updates a single Rating object"""

    model = Rating
    fields = '__all__'
    template_name = 'refferences_db/update_rating.html'
    success_url = '/rating'

class DeleteRatingView(DeleteView):
    """deletes a single Rating object"""
    
    model = Rating
    template_name = 'refferences_db/delete_view.html'
    success_url = '/rating'