from django.urls import path

from .views import main_page, all_posts, post_detail, post_share, tag_posts

app_name = 'Blog'

urlpatterns = [
    path('', main_page, name='main_page'),
    path('all-posts/', all_posts, name='all_posts'),
    path('<int:post_id>/share/', post_share, name='post_share'),
    path('post/<int:post_id>/<slug:post_slug>/', post_detail, name='post_detail'),
    path('tag/<slug:tag_slug>/', tag_posts, name='tag_posts'),
]