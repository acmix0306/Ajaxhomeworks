from django.shortcuts import render
from django.http import HttpResponse # api加入此物件

# Create your views here.

def index(request):
    return HttpResponse('Hello API!!') # AJAX 呼叫程式
