from django.contrib import admin

from .models import Post


# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title', 'pub_date', 'status']
    list_filter = ['title', 'status', 'pub_date']
    search_fields = ['title', 'text', 'author']
    date_hierarchy = 'pub_date'

