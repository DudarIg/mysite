from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

 # новый менеджер моделей
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


# Create your models here.
class Post(models.Model):
    objects = models.Manager()  # менеджер, применяемый по умолчанию
    public = PublishedManager()  # конкретно-прикладной менеджер

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250, verbose_name = 'Название')
    slug = models.SlugField(max_length=250, verbose_name = 'Слоган', unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts',
                               verbose_name = 'Автор')
    body = models.TextField(verbose_name = 'Текст')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.DRAFT,
    )

    class Meta:
        verbose_name_plural = 'Посты'
        verbose_name = 'Пост'
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args= [self.publish.year,
                                                            self.publish.month,
                                                            self.publish.day,
                                                            self.slug])