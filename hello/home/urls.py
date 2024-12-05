from django.contrib import admin
from django.urls import path 
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name = "hii" ),
    path('about',views.about,name = "about" ),
    path('contact',views.hello,name = "kya bhai" ),
    path('prices',views.expenses,name = "bhav bol" ),
    
    
]
