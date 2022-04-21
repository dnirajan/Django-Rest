from django.contrib import admin
from django.urls import path
from myapp import views



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('studentapi/',views.hello_world)
    path('studentapi/',views.StudentAPI.as_view()),
    path('studentapi/<int:pk>',views.StudentAPI.as_view()),
]
