from django.contrib import admin

from .models import Post, Comment, Tag


# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title', 'pub_date', 'status']
    list_filter = ['title', 'status', 'pub_date']
    search_fields = ['title', 'text', 'author']
    date_hierarchy = 'pub_date'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'active', 'post', 'created']
    list_filter = ['active', 'created']
    search_fields = ['name', 'email', 'text']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    list_filter = ['name',]
    prepopulated_fields = {"slug": ("name",)}
