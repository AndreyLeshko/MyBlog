from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post


def main_page(request):
    last_3_posts = Post.objects.all()[:3]
    return render(request, 'Blog/main_page.html', {'posts': last_3_posts})


def all_posts(request):
    all_posts = Post.objects.all()
    paginator = Paginator(all_posts, 2)
    page = request.GET.get('page')
    try:
        page_posts = paginator.page(page)
    except PageNotAnInteger:
        page_posts = paginator.page(1)
    except EmptyPage:
        page_posts = paginator.page(paginator.num_pages)
    return render(request, 'Blog/all_posts.html', {'page': page, 'posts': page_posts})


def post_detail(request, post_id, post_slug):
    post = get_object_or_404(Post, pk=post_id)
    # post = Post.objects.get(pk=post_id)
    return render(request, 'Blog/post_detail.html', {'post': post})
