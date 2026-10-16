from django.urls import path
from .views import home_view

urlpatterns = [
    path('kago', home_view, name='home'),
]