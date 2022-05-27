from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('draft', 'Draft'),
        ('deleted', 'Deleted'),
    ]
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст поста')
    pub_date = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, null=True, default='Автор неизвестен', verbose_name='Автор')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name='Статус')
    slug = models.SlugField(max_length=200, unique_for_date='pub_date')

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Blog:post_detail', args=[self.id, self.slug])