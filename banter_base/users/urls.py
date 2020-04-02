from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='users-home'),
    path('login/', views.login, name='users-login'),
]   