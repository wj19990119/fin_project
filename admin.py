from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'url', 'created_time', 'text']

# Register your models here.
admin.site.register(Comment,CommentAdmin)
