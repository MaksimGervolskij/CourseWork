from django.urls import path
from . import views
from .views import post_detail


urlpatterns = [
    path('', views.index),
    path('home', views.home),
    path('news', views.news),
    path('category', views.category),
    path('category1', views.category1),
    path('search/', views.search, name='search'),
    path('news/<int:pk>/', post_detail, name='post_detail'),
    path('category1/', views.category1, name='category1'),
    path('category2/', views.category2, name='category2'),
    path('category3/', views.category3, name='category3'),
    path('category4/', views.category4, name='category4'),
    path('category5/', views.category5, name='category5'),
    path('category6/', views.category6, name='category6'),
    path('category7/', views.category7, name='category7'),
    path('category8/', views.category8, name='category8'),
    path('category9/', views.category9, name='category9'),
    #path('category1/<str:category>/', category1_view, name='category1'),
]

