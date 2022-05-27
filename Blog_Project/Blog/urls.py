from django.urls import path

from .views import main_page, all_posts, post_detail

app_name = 'Blog'

urlpatterns = [
    path('', main_page, name='main_page'),
    path('all-posts/', all_posts, name='all_posts'),
    path('post/<int:post_id>', post_detail, name='post_detail')
]