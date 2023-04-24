from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context={
      "variable1":"Harry is great",
      "variable2":"Rohan is great"

    }
    #return HttpResponse("This is Home Page")
    return render(request,'index.html',context)

def upload_cv(request):
    return render(request, "index1.html")

def about(request):
    return HttpResponse("This is Information Page")

def services(request):
    return HttpResponse("This is Services Page")