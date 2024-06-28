from django.contrib import admin
from .models import *

# Register your models here.

class StoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    ordering = ['title']
    list_filter = ['tag']
    search_fields = ['body']
    list_per_page = 3
    # action_form = ['insert', 'delete']

admin.site.register(Story, StoryAdmin)