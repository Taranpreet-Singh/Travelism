from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
# Create your views here.

User = get_user_model()


class PostList(generic.ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'posts/post_list.html'

class CreatePost(LoginRequiredMixin, generic.CreateView):
    fields = ('image', 'caption', 'location')
    model = Post
    template_name = 'posts/post.html'
    success_url = reverse_lazy('posts:post_list')

    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.user = self.request.user
    #     self.object.save()
    #     return super().form_valid(form)
