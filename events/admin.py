from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Event, Comment

# Register your models here.

admin.site.register(Event)
admin.site.register(Comment)