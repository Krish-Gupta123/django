from django.shortcuts import render , HttpResponse

# Create your views here.
def index(request):
        context ={"variable":"'yeh bheja hua content hai'"}
        return render(request,'index.html',context)
        # return render(request,'index.html')
        # return HttpResponse("hello this is blank")

def about(request):
         return render(request,'about.html')

def hello(request):
         return render(request,'contact.html')

def expenses(request):
         return render(request,'prices.html')