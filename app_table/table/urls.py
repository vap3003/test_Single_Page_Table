from django.urls import include, path
from .views import get_table

urlpatterns = [
    path('', get_table),
]