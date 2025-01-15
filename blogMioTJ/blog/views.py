from django.shortcuts import render
from .models import post

def postList(request):
    posts = post.objects.all().order_by('-fecha')
    return render(request, 'postList.html', {'posts': posts})