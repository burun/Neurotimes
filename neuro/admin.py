from django.contrib import admin
from django import forms
from neuro.models import Category, Page, Fragment, FragmentImage


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
    list_display = ('title', 'category', 'author',
                    'get_tags', 'views', 'likes')

    def get_tags(self, page):
        tags = []
        for tag in page.tags.all():
            tags.append(str(tag))
        return ', '.join(tags)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'date_id', 'views', 'likes')


class FragmentImageInline(admin.TabularInline):
    model = FragmentImage
    extra = 9


class FragmentAdmin(admin.ModelAdmin):
    inlines = [FragmentImageInline, ]
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Category', {'fields': ['category']}),
        ('Author', {'fields': ['author']}),
        ('Text', {'fields': ['text']}),
        ('URL', {'fields': ['url']}),
        ('tags', {'fields': ['tags']}),
    ]
    list_display = ('title', 'category', 'author', 'get_tags')

    def get_tags(self, fragment):
        tags = []
        for tag in fragment.tags.all():
            tags.append(str(tag))
        return ', '.join(tags)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Fragment, FragmentAdmin)
