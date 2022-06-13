from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail

from .models import Post, Comment, Tag
from .forms import EmailPostForm, CommentForm


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
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'Blog/post_detail.html', {'post': post,
                                                     'new_comment': new_comment,
                                                     'comment_form': comment_form,
                                                     'comments': comments,
                                                     })


def post_share(request, post_id):
    # post = get_object_or_404(Post, pk=post_id, status='active')
    post = get_object_or_404(Post, pk=post_id)
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f'{cd["name"]} ({cd["email"]}) рекомендует вам прочитать пост {post.title}'
            message = f'Прочитайте пост {post.title} \nСсылка на пост: {post_url} \n\n {cd["comments"]}'
            send_mail(subject, message, 'andrey.leshko.blog@gmail.com', [cd["to"], ])
            sent = True
    else:
        form = EmailPostForm()
        return render(request, 'Blog/share.html', {'form': form, 'post': post, 'sent': sent})


def tag_posts(request, tag_slug):
    tag = Tag.objects.get(slug=tag_slug)
    posts = tag.posts.all()
    # posts = Post.objects.filter(tag__slug=tag_slug)
    return render(request, 'Blog/tag_posts.html', {'posts': posts, 'tag': tag})
    # return render(request, 'Blog/tag_posts.html', {'tag': tag})