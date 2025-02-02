from django.urls import path
from memorial.views import index, about_page, articles
urlpatterns = [
    path('', index),
    path('about/', about_page),
    path('article/<int:number>', articles)
]