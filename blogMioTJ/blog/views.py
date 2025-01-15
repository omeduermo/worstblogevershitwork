from django.shortcuts import render, redirect
from .models import post
from .forms import postForm

def postList(request):
    posts = post.objects.all().order_by('-fecha')
    return render(request, 'postList.html', {'posts': posts})

def createPost(request):
    if request.method == 'POST':
        form = postForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('postList')
    else:
        form = postForm()
        
    return render(request, 'createPost.html', {'form': form})