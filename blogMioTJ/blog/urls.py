from django.urls import path
from . import views

urlpatterns = [
    path('', views.postList, name='postList'),
    path('crear/', views.createPost, name='createPost'),
]
