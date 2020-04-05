from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='feed-home'),
    path('new_entry', views.new_entry, name='new-entry')
]   