from curses.ascii import US

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name_plural = "categories"
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children',on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    def __str__(self):

        full_path = [self.name]
        k = self.parent

        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return' --> '.join(full_path[::-1])


class Post(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False,auto_now_add=False)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


