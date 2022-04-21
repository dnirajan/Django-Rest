import imp
from django.contrib import admin
from django.db import router
from django.urls import path,include
from myapp import views
from rest_framework.routers import DefaultRouter

#creating router obj
router=DefaultRouter()

#registering
router.register('student',views.StudentViewset,basename='student') 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]
