from django.contrib import admin
from django.urls import path
from projectkaapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index ,name = "index"),
    path('about', views.about ,name = "about"),
    path('login', views.login ,name = "login"),
]






