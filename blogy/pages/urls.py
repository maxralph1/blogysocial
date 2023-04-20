from django.views.generic import TemplateView
from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.index, name='index'),
    path('pages=<int:page>/', views.index_pages, name='index_pages'),

    path('articles/', views.articles, name='articles'),
    path('articles/<slug:article_slug>/', views.article, name='article'),
    path('articles/pages=<int:page>/',
         views.articles_pages, name='articles_pages'),

    path('hot-picks/', views.hot_picks, name='hot_picks'),

    path('topics/', views.topics, name='topics'),
    path('topics/<slug:topic_slug>/', views.topic, name='topic'),

    path('search-articles/', views.search_articles, name='search_articles'),
    path('search-articles/<slug:query>/pages=<int:page>/',
         views.search_articles_pages, name='search_articles_pages'),

    # Authors
    path('authors/', views.authors, name='authors'),
    path('authors/<slug:username>/',
         views.author, name='author'),
    path('authors/pages=<int:page>/',
         views.authors_pages, name='authors_pages'),

    path('about-us/', TemplateView.as_view(
        template_name='pages/about_us.html'), name='about_us')
]
