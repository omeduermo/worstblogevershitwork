from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import postForm, comentarioForm

def postList(request):
    posts = Post.objects.all().order_by('-fecha')

    if request.method == 'POST':
        form = comentarioForm(request.POST)
        if form.is_valid():
            post = get_object_or_404(Post, id=request.POST.get('post_id'))
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.save()
            return redirect('postList')  # Redirige después de procesar el comentario

    else:
        form = comentarioForm()

    return render(request, 'postList.html', {'posts': posts, 'form': form})

def createPost(request):
    if request.method == 'POST':
        form = postForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('postList')
    else:
        form = postForm()
        
    return render(request, 'createPost.html', {'form': form})

def postDetail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comentarios = post.comentario_set.all()
    if request.method == 'POST':
        form = comentarioForm(request.POST)
        if form.is_valid():
            # Crear el comentario y asociarlo al post
            newComentario = form.save(commit=False)
            newComentario.post = post
            newComentario.save()
            return redirect('post_detail', post_id=post.id)  # Redirigir para evitar resubir el formulario
    else:
        form = comentarioForm()
    
    return render(request, 'post_detail.html', {'post': post, 'form': form, 'comentarios': comentarios})