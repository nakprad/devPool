import imp
from multiprocessing.spawn import import_main_path
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    # return HttpResponse("hello")
    return render(request,'index.html')

