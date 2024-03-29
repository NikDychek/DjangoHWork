from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):
    # title = models.CharField(max_length=60)
    # subtitle = models.CharField(max_length=20)
    # content = models.TextField()
    # page = models.IntegerChoices("Pages", "1 2 3")
    # categories = models.ManyToManyField(Category)
    title = models.CharField(max_length=100)
    content = models.TextField()
    pages = models.IntegerField(null=True, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return slugify(self.title)
