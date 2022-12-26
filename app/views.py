from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('hello...........')

def venki(request):
    return HttpResponse('i love u........')
def venki2(request):
    return HttpResponse('<h1>I LOVE U TOO</h1>')
def venki3(request):
    return HttpResponse('<marquee><h1>madhu is a good guy</h1></marquee>')
def v(reequest):
    return HttpResponse('good morning')