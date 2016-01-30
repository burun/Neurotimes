from django.contrib import admin
from django import forms
from neuro.models import Category, Page


class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Category', {'fields': ['category']}),
        ('Author', {'fields': ['author']}),
        ('Text', {'fields': ['text']}),
        ('URL', {'fields': ['url']}),
        ('Photo', {'fields': ['photo']}),
        ('Credits', {'fields': ['photo_legend']}),
        ('PDF', {'fields': ['pdf']}),
        ('tags', {'fields': ['tags']}),
        ('Views', {'fields': ['views']}),
        ('Likes', {'fields': ['likes']}),
    ]
    list_display = ('title', 'category', 'author', 'get_tags', 'views', 'likes')

    def get_tags(self, page):
        tags = []
        for tag in page.tags.all():
            tags.append(str(tag))
        return ', '.join(tags)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'date_id', 'views', 'likes')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
