from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')

def our(request):
    return render(request,'our.html')

def what(request):
    return render(request,'what.html')

def about(request):
    return render(request,'about.html')

def get(request):
    return render(request,'get.html')