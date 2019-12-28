from django.urls import path

import libraryapp.views as libraryapp

app_name = 'libraryapp'

urlpatterns = [
    path('', libraryapp.library, name='index'),
    path('page/<int:page>/', libraryapp.library, name='page'),
    path('listview/', libraryapp.ArticleView.as_view(), name='listview'),
    path('create_author/', libraryapp.CreateAuthor.as_view(), name='create_author'),
    path('create_theme/<int:author_id>/', libraryapp.CreateTheme.as_view(), name='create_theme'),
    path('create_ref/<int:author_id>/<int:theme_id>/', libraryapp.CreateRef.as_view(), name='create_ref'),
    path('create_article/<int:author_id>/<int:theme_id>/<int:ref_id>', libraryapp.CreateArticle.as_view(), name='create_article'),
    path('edit_article/<int:pk>/', libraryapp.EditArticle.as_view(), name='edit_article'),
    path('edit_theme/<int:article_id>/<int:pk>/', libraryapp.EditTheme.as_view(), name='edit_theme'),
    path('edit_author/<int:article_id>/<int:pk>/', libraryapp.EditAuthor.as_view(), name='edit_author'),
    path('edit_refs/<int:article_id>/<int:pk>/', libraryapp.EditRefs.as_view(), name='edit_refs'),
    path('article/<int:pk>/', libraryapp.article, name='article'),
    path('add_shelf/<int:pk>/', libraryapp.add_shelf, name='add_shelf'),
    path('delete_from_shelf/<int:pk>', libraryapp.delete_from_shelf, name='delete_from_shelf'),
    path('open_pdf/<int:pk>/', libraryapp.open_pdf, name='open_pdf'),
]
