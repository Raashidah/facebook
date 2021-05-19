from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def test1(request):
    return HttpResponse("hello world")
def test2(request):
     return render(request,'fb.html')