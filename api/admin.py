from django.contrib import admin
from api import models


@admin.register(models.Parents)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender']


@admin.register(models.Child)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender']


@admin.register(models.GrandChild)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender']
