from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landPage, name='landPage'),
    path('posts/', include('blog.urls'), name='postList'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
