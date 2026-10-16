from django.urls import path
from .views import home_view

urlpatterns = [
    path('kawasaki', home_view, name='home'),
]