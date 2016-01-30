from django.utils import timezone
from django.db import models
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.PositiveIntegerField(default=0)
    likes = models.IntegerField(default=0)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name

    def date_id(self):
        return str(self.date)


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128, unique=True)
    text = RichTextField('text')
    url = models.URLField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_legend = models.CharField(max_length=128, blank=True)
    pdf = models.URLField(blank=True)
    date = models.DateTimeField(default=timezone.now)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    author = models.CharField(max_length=128, blank=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title
