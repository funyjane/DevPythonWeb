from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from authentication.models import Profile
from authentication import views as profile_views
from book.models import Book
from book import views as book_view
from orders.models import *
from refference_db import models as ref_models


class ManagerOrderList(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'manager_admin/orders/order_list.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()

class ManagerOrderUpdate(LoginRequiredMixin, UpdateView):
    model = Order
    template_name = 'manager_admin/orders/order_update.html'
    fields = ('status1', 'delivery_address', 'phone', 'comment')
    success_url = reverse_lazy('manager:order-list')

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()

class ManagerOrderDelete(LoginRequiredMixin, DeleteView):
    model = Order
    template_name = 'manager_admin/orders/order_delete.html'
    success_url = reverse_lazy('manager:order-list')

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()


class AuthorList(LoginRequiredMixin, ListView):
    model = ref_models.Author
    template_name = 'manager_admin/refs/author_list.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()

class AuthorView(LoginRequiredMixin, DetailView):
    model = ref_models.Author
    template_name = 'manager_admin/refs/author_view.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()

class AuthorCreate(LoginRequiredMixin, CreateView):
    model = ref_models.Author
    fields = '__all__'
    success_url = reverse_lazy('manager:author_list')
    template_name = 'manager_admin/refs/author_create.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()

class AuthorUpdate(LoginRequiredMixin, UpdateView):
    model = ref_models.Author
    fields = '__all__'
    success_url = reverse_lazy('manager:author_list')
    template_name = 'manager_admin/refs/series_update.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()

class AuthorDelete(LoginRequiredMixin, DeleteView):
    model = ref_models.Author
    success_url = reverse_lazy('manager:author_list')
    template_name = 'manager_admin/refs/author_delete.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()



class SeriesList(LoginRequiredMixin, ListView):
    model = ref_models.Series
    template_name = 'manager_admin/refs/series_list_view.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()

class SeriesView(LoginRequiredMixin, DetailView):
    model = ref_models.Series
    template_name = 'manager_admin/refs/series_view.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()

class SeriesCreate(LoginRequiredMixin, CreateView):
    model = ref_models.Series
    fields = '__all__'
    success_url = reverse_lazy('manager:series_list')
    template_name = 'manager_admin/refs/series_create.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()

class SeriesUpdate(LoginRequiredMixin, UpdateView):
    model = ref_models.Series
    fields = '__all__'
    success_url = reverse_lazy('manager:series_list')
    template_name = 'manager_admin/refs/series_update.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()

class SeriesDelete(LoginRequiredMixin, DeleteView):
    model = ref_models.Series
    success_url = reverse_lazy('manager:series_list')
    template_name = 'manager_admin/refs/series_delete.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()


class GenreList(LoginRequiredMixin, ListView):
    model = ref_models.Genre
    template_name = 'manager_admin/refs/genre_list.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()

class GenreView(LoginRequiredMixin, DetailView):
    model = ref_models.Genre
    template_name = 'manager_admin/refs/genre_view.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()

class GenreCreate(LoginRequiredMixin, CreateView):
    model = ref_models.Genre
    fields = '__all__'
    success_url = reverse_lazy('manager:genre_list')
    template_name = 'manager_admin/refs/genre_create.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()

class GenreUpdate(LoginRequiredMixin, UpdateView):
    model = ref_models.Genre
    fields = '__all__'
    success_url = reverse_lazy('manager:genre_list')
    template_name = 'manager_admin/refs/genre_update.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()

class GenreDelete(LoginRequiredMixin, DeleteView):
    model = ref_models.Genre
    success_url = reverse_lazy('manager:genre_list')
    template_name = 'manager_admin/refs/genre_delete.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()



class PublisherList(LoginRequiredMixin, ListView):
    model = ref_models.Publisher
    template_name = 'manager_admin/refs/publisher_list.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()

class PublisherView(LoginRequiredMixin, DetailView):
    model = ref_models.Publisher
    template_name = 'manager_admin/refs/publisher_view.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()

class PublisherCreate(LoginRequiredMixin, CreateView):
    model = ref_models.Publisher
    fields = '__all__'
    success_url = reverse_lazy('manager:publisher_list')
    template_name = 'manager_admin/refs/publisher_create.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()

class PublisherUpdate(LoginRequiredMixin, UpdateView):
    model = ref_models.Publisher
    fields = '__all__'
    success_url = reverse_lazy('manager:publisher_list')
    template_name = 'manager_admin/refs/publisher_update.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()

class PublisherDelete(LoginRequiredMixin, DeleteView):
    model = ref_models.Publisher
    fields = '__all__'
    success_url = reverse_lazy('manager:publisher_list')
    template_name = 'manager_admin/refs/publisher_delete.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()


class FormatListView(LoginRequiredMixin,ListView):

    paginate_by = 5
    template_name = "refferences_db/format_list_view.html"
    model = ref_models.Format

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()

class FormatView(LoginRequiredMixin,DetailView):

    model = ref_models.Format
    template_name = "refferences_db/format_view.html"

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()

class CreateFormatView(LoginRequiredMixin,CreateView):

    model = ref_models.Format
    fields = '__all__'
    template_name = 'refferences_db/create_format.html'
    success_url = reverse_lazy('manager:format_list')

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()

class UpdateFormatView(LoginRequiredMixin,UpdateView):

    model = ref_models.Format
    fields = '__all__'
    template_name = 'refferences_db/update_format.html'
    success_url = reverse_lazy('manager:format_list')

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()

class DeleteFormatView(LoginRequiredMixin,DeleteView):
    
    model = ref_models.Format
    template_name = 'refferences_db/delete_view.html'
    success_url = reverse_lazy('manager:format_list')

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()



class Age_resListView(LoginRequiredMixin,ListView):

    paginate_by = 5
    template_name = "refferences_db/ageres_list_view.html"
    model = ref_models.Age_res

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()

class Age_resView(LoginRequiredMixin,DetailView):

    model = ref_models.Age_res
    template_name = "refferences_db/ageres_view.html"

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()

class CreateAge_resView(LoginRequiredMixin,CreateView):

    model = ref_models.Age_res
    fields = '__all__'
    template_name = 'refferences_db/create_ageres.html'
    success_url = reverse_lazy('manager:age_list')

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()

class UpdateAge_resView(LoginRequiredMixin,UpdateView):

    model = ref_models.Age_res
    fields = '__all__'
    template_name = 'refferences_db/update_ageres.html'
    success_url = reverse_lazy('manager:age_list')

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()

class DeleteAge_resView(LoginRequiredMixin,DeleteView):
    
    model = ref_models.Age_res
    template_name = 'refferences_db/delete_view.html'
    success_url = reverse_lazy('manager:age_list')

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()



class RatingListView(LoginRequiredMixin,ListView):

    paginate_by = 5
    template_name = "refferences_db/rating_list_view.html"
    model = ref_models.Rating

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()

class RatingView(LoginRequiredMixin,DetailView):

    model = ref_models.Rating
    template_name = "refferences_db/rating_view.html"

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()

class CreateRatingView(LoginRequiredMixin,CreateView):

    model = ref_models.Rating
    fields = '__all__'
    template_name = 'refferences_db/create_rating.html'
    success_url = reverse_lazy('manager:rating_list')

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()

class UpdateRatingView(LoginRequiredMixin,UpdateView):

    model = ref_models.Rating
    fields = '__all__'
    template_name = 'refferences_db/update_rating.html'
    success_url = reverse_lazy('manager:rating_list')

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()

class DeleteRatingView(LoginRequiredMixin,DeleteView):
    
    model = ref_models.Rating
    template_name = 'refferences_db/delete_view.html'
    success_url = reverse_lazy('manager:rating_list')

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()



class ManagerBookList(LoginRequiredMixin, book_view.BookListView):
    template_name = 'manager_admin/book/admin_panel.html'
    paginate_by = 12

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()

class ManagerBookView(LoginRequiredMixin, book_view.BookView):
    template_name = 'manager_admin/book/book_view.html'
    success_url = reverse_lazy('manager:book-list')

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()

class ManagerBookCreate(book_view.CreateBookView):
    template_name = 'manager_admin/book/book_create.html'
    success_url = reverse_lazy('manager:book-list')

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()

class ManagerBookUpdate(LoginRequiredMixin, book_view.UpdateBookView):
    template_name = 'manager_admin/book/book_update.html'
    success_url = reverse_lazy('manager:book-list')

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()

class ManagerBookDelete(LoginRequiredMixin, book_view.DeleteBookView):
    template_name = 'manager_admin/book/book_delete.html'
    success_url = reverse_lazy('manager:book-list')

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()


class CustomersList(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'manager_admin/customer/customer_list.html'

    def get_queryset(self, *args, **kwargs):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()


class CustomerUpdate(profile_views.UpdateProfileView):
    template_name = 'manager_admin/customer/customer_update.html'
    success_url = reverse_lazy('manager:customer-list')

    def get_queryset(self, *args, **kwargs):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()


class CustomerView(LoginRequiredMixin, DetailView):
    template_name = 'manager_admin/customer/customer_view.html'
    model = Profile

    def get_queryset(self, *args, **kwargs):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()