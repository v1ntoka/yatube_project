from django.contrib import admin
from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pub_date', 'short_text', 'author', 'group')
    list_filter = ('author', 'pub_date')
    search_fields = ('text',)
    date_hierarchy = 'pub_date'
    ordering = ('-pub_date',)
    list_select_related = ('author', 'group')
    list_per_page = 15


@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')
    list_per_page = 15
    prepopulated_fields = {"slug": ("title",)}
