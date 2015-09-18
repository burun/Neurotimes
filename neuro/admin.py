from django.contrib import admin
from neuro.models import Category, Page


class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Category', {'fields': ['category']}),
        ('Order', {'fields': ['order']}),
        ('Text', {'fields': ['text']}),
        ('URL', {'fields': ['url']}),
        ('Photo', {'fields': ['photo']}),
        ('Views', {'fields': ['views']}),
        ('Likes', {'fields': ['likes']}),
    ]
    list_display = ('title', 'category', 'order', 'url', 'views', 'likes')

admin.site.register(Category)
admin.site.register(Page, PageAdmin)
