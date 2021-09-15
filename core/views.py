from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(Request, nome, idade):
    return HttpResponse('<h1>hello {}, sua idade é {}</h1>'.format(nome,idade))