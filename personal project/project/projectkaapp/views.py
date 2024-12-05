from django.shortcuts import render , HttpResponse

# Create your views here.
def index(request):
    # contex = { "variable":
    #     "this is value rendered by views of variable"
    # }
    return render(request , "index.html")
    # return HttpResponse("this is a about page")

def about(request):
     return render(request , "about.html")
    

def login(request):
    return HttpResponse("this is a login page")