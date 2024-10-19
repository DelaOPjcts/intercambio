from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, opciones_regalo, form_regalo, ver_regalo, eliminar_regalo
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('home/', home, name='home'),
    path('opciones_regalo/', opciones_regalo, name='opciones_regalo'),
    path('opciones_regalo/nuevo/', form_regalo, name='form_regalo'),
    path('ver_regalo/<int:regalo_id>/', ver_regalo, name='ver_regalo'),
    path('eliminar_regalo/<int:regalo_id>/', views.eliminar_regalo, name='eliminar_regalo'),
]