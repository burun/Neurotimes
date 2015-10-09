from django.contrib import admin
from django import forms
from neuro.models import Category, Page


class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Category', {'fields': ['category']}),
        ('Text', {'fields': ['text']}),
        ('URL', {'fields': ['url']}),
        ('Photo', {'fields': ['photo']}),
        ('PDF', {'fields': ['pdf']}),
        ('tags', {'fields': ['tags']}),
        ('Views', {'fields': ['views']}),
        ('Likes', {'fields': ['likes']}),
    ]
    list_display = ('title', 'category', 'url', 'get_tags', 'views', 'likes')

    def get_tags(self, page):
        tags = []
        for tag in page.tags.all():
            tags.append(str(tag))
        return ', '.join(tags)


admin.site.register(Category)
admin.site.register(Page, PageAdmin)
