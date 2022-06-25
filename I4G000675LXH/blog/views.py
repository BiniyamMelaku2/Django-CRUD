from django.shortcuts import render
from django.views import generic
from .models import Post
from django.urls import reverse_lazy


# Create your views here.

class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-publish')
    template_name = 'blog/post_list.html'

class PostCreateView(generic.CreateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")
    template_name = 'blog/post_form.html'

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostUpdateView(generic.UpdateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")
    template_name = 'blog/post_update.html'


class PostDeleteView(generic.UpdateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")
    template_name = 'blog/post_delete.html'