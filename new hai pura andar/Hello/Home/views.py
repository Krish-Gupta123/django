from django.shortcuts import render,HttpResponse

from Home.models import Contact
from datetime import datetime
from django.contrib import messages

# Create your views here.

# def index(request):
#     return HttpResponse("i am creator")

def about(request):
    #return HttpResponse("this is about page")
    return render(request,"about.html")

def hi(request):
    #return HttpResponse("this is home page")
    return render(request,"home.html")

def contact(request):
    #return HttpResponse("this is contact page chup chap mail kar call nhi karneka")
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name = name,email=email , phone = phone , desc = desc, date = datetime.today())
        contact.save()
        messages.success(request, "submit ho gaya bhai")

    
    return render(request,"contact.html")

def templates(request):
    #return render(request,"index.html")
    return render(request,"index1.html")

def variable(request):
    conte = {
        "variable1" : "this is variable 1",
        "variable2" : "this is variable 2"
    }
    return render(request,"index.html",conte)
    
