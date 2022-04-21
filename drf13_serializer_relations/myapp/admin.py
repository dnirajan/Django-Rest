import imp
from django.contrib import admin
from .models import Singer,Song
# Register your models here.

@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display=['name','gender','song']

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display=['title','duration','singer']