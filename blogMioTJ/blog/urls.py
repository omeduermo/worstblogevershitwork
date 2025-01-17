from django.urls import path
from . import views

urlpatterns = [
    path('', views.postList, name='postList'),
    path('crear/', views.createPost, name='createPost'),
    path('<int:post_id>/', views.postDetail, name='postDetail'),
]
