from django.urls import path

import libraryapp.views as libraryapp

app_name = 'libraryapp'

urlpatterns = [
    path('', libraryapp.library, name='index'),
    path('article/<int:pk>/', libraryapp.article, name='article'),
]
