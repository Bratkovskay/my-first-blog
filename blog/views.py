from django.shortcuts import render
from django.http  import HttpResponse
from django.template import Context, loader
from django.views.generic import ListView, DetailView
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

class PostList(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

#def post_list (request):
    #return HttpResponse('blog/post_list.html')

#def post_list(request):
    #template= loader.get_template("blog/post_list.html")
    #return HttpResponse(template.render)
