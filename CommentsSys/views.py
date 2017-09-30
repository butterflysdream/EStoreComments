from django.shortcuts import render
from . import taobaoSpider
# Create your views here.

def home(request):
    return  render(request,'home.html')

def dealComm(request):
    if request.POST:
        url = request.POST['urltext']
        result =taobaoSpider.spider(url =url)
        return render(request, 'home.html',result)

