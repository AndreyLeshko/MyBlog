from django.shortcuts import render
from django.http import HttpResponse

from .models import Post


def main_page(request):
    last_3_posts = Post.objects.all()[:3]
    return render(request, 'Blog/main_page.html', {'posts': last_3_posts})


def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'Blog/all_posts.html', {'posts': posts})


def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'Blog/post_detail.html', {'post': post})
