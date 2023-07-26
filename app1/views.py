from django.shortcuts import render
from django.http import HttpResponse
def assign1(request):
    return render(request,'assign1.html')
def assign2(request):
    return render(request,'assign2.html')
def assign3(request):
    return HttpResponse('<center><h1>This is Third Response in the form of String</h1></center>')
