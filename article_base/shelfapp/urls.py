from django.urls import path

import shelfapp.views as shelfapp

app_name = 'shelfapp'

urlpatterns = [
    path('', shelfapp.bookshelf, name='index'),
    path('article/<int:pk>/', shelfapp.article, name='article'),
]