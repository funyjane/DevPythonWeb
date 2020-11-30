from django.urls import path
from .views import *

app_name = 'profile'
urlpatterns = [
    path('signin/', AuthenticationView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', AuthLogoutView.as_view(), name='logout'),
    path('password_change/', AuthPasswordChangeView.as_view(), name='password-change'),
    path('password_change_success/', AuthPasswordUpdDoneView.as_view(), name='password-updt-success'),
    path('auth/', ProfileView.as_view(), name='profile-view'),
    path('<int:pk>/update/', UpdateProfileView.as_view(), name='profile-update'),
]
