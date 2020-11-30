from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.views.generic import UpdateView, TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from . import forms
from . import models



class AuthenticationView(LoginView):
    template_name = 'registration/log_in.html'
    success_url = reverse_lazy('profile:profile-view')

class AuthLogoutView(LogoutView):
    template_name = 'registration/log_out.html'


class AuthPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'registration/password_change.html'
    success_url = '/password_change'

class AuthPasswordUpdDoneView(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = 'registration/password_change_success.html'


class SignUpView(CreateView):
    form_class = forms.UserRegisterForm
    template_name = 'registration/sign_up.html'
    success_url = reverse_lazy('profile:profile-update')
    success_message = "Your profile has been created successfully"

    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return HttpResponseRedirect(reverse_lazy('profile:profile-view'))



class ProfileView(LoginRequiredMixin, TemplateView):
    model = models.Profile
    template_name = 'authentication/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        user = self.request.user
        profile = models.Profile.objects.filter(user=user).first()

        if user.first_name:
            profile.first_name = user.first_name

        if user.last_name:
            profile.last_name = user.last_name

        profile.email = user.email

        profile.save()

        context['profile'] = profile
        return context


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    
    model = models.Profile
    template_name = 'authentication/update_profile.html'
    fields = ('first_name',
              'last_name',
              'email',
              'phone_number',
              'city',
              'address1',
              'address2',
              'zip_code',
              'additional_info')
    success_url = '/profile'
