from django.urls import path
from .views import home_view

urlpatterns = [
    path('krico', home_view, name='home'),
]