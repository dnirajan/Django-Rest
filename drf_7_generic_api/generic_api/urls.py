from django.contrib import admin
from django.urls import path
from myapp import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/',views.LCview.as_view()),
    path('studentapi/<int:pk>',views.RUDView.as_view()),
]
