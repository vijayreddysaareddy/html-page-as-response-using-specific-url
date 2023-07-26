from django.shortcuts import render
from django.http import HttpResponse
def work1(request):
    return render(request,'work1.html')
def work2(request):
    return render(request,'work2.html')
def work3(request):
    return HttpResponse('<center><h1>This is Third Response as a String in app2</h1></center>')
