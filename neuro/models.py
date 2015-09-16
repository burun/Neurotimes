from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.PositiveIntegerField(default=0)
    likes = models.IntegerField(default=0)
    date = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    text = models.CharField(max_length=12800)
    url = models.URLField()
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title
