from django.contrib import admin
from django.db import router
from django.urls import path,include
from myapp import views
from rest_framework.routers import DefaultRouter

#creating router obj
router=DefaultRouter()

#registering
router.register('singer', views.SingerViewset,basename='singer')
router.register('song', views.SongViewset,basename='song')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]