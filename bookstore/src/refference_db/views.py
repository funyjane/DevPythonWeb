from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import *
from .forms import *


def genre_list_view(request):
    '''displays a list of all genre objects'''

    context = {'genres': Genre.objects.all()}
    return render(request, template_name='refferences_db/genre_list_view.html', context=context)

def genre_view(request, pk):
    '''displays a single genre object'''

    context = {'genre': Genre.objects.get(pk=pk)}
    return render(request, template_name='refferences_db/genre_view.html', context=context)

def create_genre_view (request):
    """creates a single genre object"""
    
    if request.method == 'POST':
        form = CreateGenreForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/genre')
    else:
        form = CreateGenreForm()
    return render(
        request,
        template_name='refferences_db/create_genre.html',
        context={'form':form}
    )

def update_genre_view (request, pk):
    """updates a single genre object"""
    
    if request.method == 'POST':
        form = UpdateGenreForm(data=request.POST)
        if form.is_valid():
            genre_name = form.cleaned_data.get('genre')
            genre_dcptn = form.cleaned_data.get('description')
            new_genre = Genre.objects.get(pk=pk)
            new_genre.genre = genre_name
            new_genre.description = genre_dcptn
            new_genre.save()
            return HttpResponseRedirect('/genre')
    else:
        genre = Genre.objects.get(pk=pk)
        form = UpdateGenreForm(data={'genre':genre.genre, 'description': genre.description})
        return render(
            request,
            template_name='refferences_db/update_genre.html',
            context={'form':form}
        )

def delete_genre_view(request, pk):
    if request.method == "POST":
        genre = Genre.objects.get(pk=pk)
        genre.delete()
        return HttpResponseRedirect('/genre')
    else:
        genre = Genre.objects.get(pk=pk)
    return render(request, template_name='refferences_db/delete_view.html', context={'genre': genre, 'header': genre.genre})



def author_list_view(request):
    '''displays a list of all author objects'''

    context = {'authors': Author.objects.all()}
    return render(request, template_name='refferences_db/author_list_view.html', context=context)

def author_view(request, pk):
    '''displays a single author object'''

    context = {'author': Author.objects.get(pk=pk)}
    return render(request, template_name='refferences_db/author_view.html', context=context)

def create_author_view (request):
    """creates a single author object"""
    
    if request.method == 'POST':
        form = CreateAuthorForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/author')
    else:
        form = CreateAuthorForm()
    return render(
        request,
        template_name='refferences_db/create_author.html',
        context={'form':form}
    )

def update_author_view (request, pk):
    """updates a single author object"""
    
    if request.method == 'POST':
        form = UpdateAuthorForm(data=request.POST)
        if form.is_valid():
            author_name = form.cleaned_data.get('author')
            author_bio = form.cleaned_data.get('biography')
            new_author = Author.objects.get(pk=pk)
            new_author.author = author_name
            new_author.biography = author_bio
            new_author.save()
            return HttpResponseRedirect('/author')
    else:
        author = Author.objects.get(pk=pk)
        form = UpdateAuthorForm(data={'author':author.author, 'biography': author.biography})
        return render(
            request, 
            template_name='refferences_db/update_author.html', 
            context={'form':form}
            )

def delete_author_view(request, pk):
    if request.method == "POST":
        author = Author.objects.get(pk=pk)
        author.delete()
        return HttpResponseRedirect('/author')
    else:
        author = Author.objects.get(pk=pk)
    return render(request, template_name='refferences_db/delete_view.html', context={'author': author, 'header': author.author})



def series_list_view(request):
    '''displays a list of all series objects'''

    context = {'series': Series.objects.all()}
    return render(request, template_name='refferences_db/series_list_view.html', context=context)

def series_view(request, pk):
    '''displays a single series object'''

    context = {'series': Series.objects.get(pk=pk)}
    return render(request, template_name='refferences_db/series_view.html', context=context)

def create_series_view (request):
    """creates a single series object"""
    
    if request.method == 'POST':
        form = CreateSeriesForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/series')
    else:
        form = CreateSeriesForm()
    return render(
        request,
        template_name='refferences_db/create_series.html',
        context={'form':form}
    )

def update_series_view (request, pk):
    """updates a single series object"""
    
    if request.method == 'POST':
        form = UpdateSeriesForm(data=request.POST)
        if form.is_valid():
            series_name = form.cleaned_data.get('title')
            series_dscp = form.cleaned_data.get('description')
            new_series = Series.objects.get(pk=pk)
            new_series.title = series_name
            new_series.description = series_dscp
            new_series.save()
            return HttpResponseRedirect('/series')
    else:
        series = Series.objects.get(pk=pk)
        form = UpdateSeriesForm(data={'title':series.title, 'biography': series.description})
        return render(
            request, 
            template_name='refferences_db/update_series.html', 
            context={'form':form}
            )

def delete_series_view(request, pk):
    if request.method == "POST":
        series = Series.objects.get(pk=pk)
        series.delete()
        return HttpResponseRedirect('/series')
    else:
        series = Series.objects.get(pk=pk)
    return render(request, template_name='refferences_db/delete_view.html', context={'series': series, 'header': series.title})



def publisher_list_view(request):
    '''displays a list of all publisher objects'''

    context = {'publishers': Publisher.objects.all()}
    return render(request, template_name='refferences_db/publisher_list_view.html', context=context)

def publisher_view(request, pk):
    '''displays a single publisher object'''

    context = {'publisher': Publisher.objects.get(pk=pk)}
    return render(request, template_name='refferences_db/publisher_view.html', context=context)

def create_publisher_view (request):
    """creates a single publisher object"""
    
    if request.method == 'POST':
        form = CreatePublisherForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/publisher')
    else:
        form = CreatePublisherForm()
    return render(
        request,
        template_name='refferences_db/create_publisher.html',
        context={'form':form}
    )

def update_publisher_view (request, pk):
    """updates a single publisher object"""
    
    if request.method == 'POST':
        form = UpdatePublisherForm(data=request.POST)
        if form.is_valid():
            publisher_name = form.cleaned_data.get('house')
            publisher_dscp = form.cleaned_data.get('history')
            new_publisher = Publisher.objects.get(pk=pk)
            new_publisher.house = publisher_name
            new_publisher.history = publisher_dscp
            new_publisher.save()
            return HttpResponseRedirect('/publisher')
    else:
        publisher = Publisher.objects.get(pk=pk)
        form = UpdatePublisherForm(data={'house':publisher.house, 'history': publisher.history})
        return render(
            request, 
            template_name='refferences_db/update_publisher.html', 
            context={'form':form}
            )

def delete_publisher_view(request, pk):
    if request.method == "POST":
        publisher = Publisher.objects.get(pk=pk)
        publisher.delete()
        return HttpResponseRedirect('/series')
    else:
        publisher = Publisher.objects.get(pk=pk)
    return render(request, template_name='refferences_db/delete_view.html', context={'series': publisher, 'header': publisher.house})



def format_list_view(request):
    '''displays a list of all format objects'''

    context = {'formats': Format.objects.all()}
    return render(request, template_name='refferences_db/format_list_view.html', context=context)

def format_view(request, pk):
    '''displays a single format object'''

    context = {'format': Format.objects.get(pk=pk)}
    return render(request, template_name='refferences_db/format_view.html', context=context)

def create_format_view (request):
    """creates a single format object"""
    
    if request.method == 'POST':
        form = CreateFormatForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/format')
    else:
        form = CreateFormatForm()
    return render(
        request,
        template_name='refferences_db/create_format.html',
        context={'form':form}
    )

def update_format_view (request, pk):
    """updates a single format object"""
    
    if request.method == 'POST':
        form = UpdateFormatForm(data=request.POST)
        if form.is_valid():
            format_name = form.cleaned_data.get('format')
            new_format = Format.objects.get(pk=pk)
            new_format.format = format_name
            new_format.save()
            return HttpResponseRedirect('/format')
    else:
        format_obj = Format.objects.get(pk=pk)
        form = UpdateFormatForm(data={'format':format_obj.format})
        return render(
            request, 
            template_name='refferences_db/update_format.html', 
            context={'form':form}
            )

def delete_format_view(request, pk):
    if request.method == "POST":
        format_obj = Format.objects.get(pk=pk)
        format_obj.delete()
        return HttpResponseRedirect('/format')
    else:
        format_obj = Format.objects.get(pk=pk)
    return render(request, template_name='refferences_db/delete_view.html', context={'format': format_obj, 'header': format_obj.format})



def ageres_list_view(request):
    '''displays a list of all age_res objects'''

    context = {'age_restrictions': Age_res.objects.all()}
    return render(request, template_name='refferences_db/ageres_list_view.html', context=context)

def ageres_view(request, pk):
    '''displays a single age_res object'''

    context = {'age_restrictions': Age_res.objects.get(pk=pk)}
    return render(request, template_name='refferences_db/ageres_view.html', context=context)

def create_ageres_view (request):
    """creates a single age_res object"""
    
    if request.method == 'POST':
        form = CreateAgeresForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/age')
    else:
        form = CreateAgeresForm()
    return render(
        request,
        template_name='refferences_db/create_ageres.html',
        context={'form':form}
    )

def update_ageres_view (request, pk):
    """updates a single age_res object"""
    
    if request.method == 'POST':
        form = UpdateAgeresForm(data=request.POST)
        if form.is_valid():
            age_name = form.cleaned_data.get('age_res')
            new_age = Age_res.objects.get(pk=pk)
            new_age.age_res = age_name
            new_age.save()
            return HttpResponseRedirect('/age')
    else:
        ageres = Age_res.objects.get(pk=pk)
        form = UpdateAgeresForm(data={'age_res':ageres.age_res})
        return render(
            request, 
            template_name='refferences_db/update_ageres.html', 
            context={'form':form}
            )

def delete_ageres_view(request, pk):
    if request.method == "POST":
        age_res = Age_res.objects.get(pk=pk)
        age_res.delete()
        return HttpResponseRedirect('/age')
    else:
        age_res = Age_res.objects.get(pk=pk)
    return render(request, template_name='refferences_db/delete_view.html', context={'age_res': age_res, 'header': age_res.age_res})



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