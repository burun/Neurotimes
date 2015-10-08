from django.contrib import admin
from neuro.models import Category, Page


class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Category', {'fields': ['category']}),
        ('Text', {'fields': ['text']}),
        ('URL', {'fields': ['url']}),
        ('Photo', {'fields': ['photo']}),
        ('PDF', {'fields': ['pdf']}),
        ('Views', {'fields': ['views']}),
        ('Likes', {'fields': ['likes']}),
    ]
    list_display = ('title', 'category', 'url', 'views', 'likes', )

admin.site.register(Category)
admin.site.register(Page, PageAdmin)
