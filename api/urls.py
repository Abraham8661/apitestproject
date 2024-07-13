from django.urls import path
from . import views

urlpatterns = [
    path('allbooks', views.api_home_view),
    path('books', views.allBooks.as_view())
]
