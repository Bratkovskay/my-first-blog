from django.shortcuts import render
from django.http  import HttpResponse
from django.template import Context, loader
from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'post'

#def post_list(request):
    #return render(request, 'blog/post_list.html',{})

#def post_list (request):
    #return HttpResponse('blog/post_list.html')

#def post_list(request):
    #template= loader.get_template("blog/post_list.html")
    #return HttpResponse(template.render)
