from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import MainAbout


admin.site.register(MainAbout)