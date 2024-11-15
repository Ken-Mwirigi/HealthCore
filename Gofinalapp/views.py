from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request,'index.html ')

def service(request):
    return render (request,'service-details.html ')

def starter(request):
    return render (request,'starter-page.html ')

def about(request):
    return render (request,'about.html')

def doctors(request):
    return render(request ,'doctors.html')

def services(request):
    return render(request,'services.html')
