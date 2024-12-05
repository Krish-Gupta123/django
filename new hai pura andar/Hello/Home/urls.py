from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [

    #path("",views.index,name = 'krish'),
    path("about/",views.about,name = 'about'),
    path("hellomoto/",views.hi,name = "home"),
    path("contacts/",views.contact,name = "contact"),
    path("",views.templates,name = "templates_files_Krish ice cream pg"),
    path("variable/",views.variable,name = "added_variable")
]