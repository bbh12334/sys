from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h1>欢迎来到我的Django应用！</h1><p>这是首页内容。</p>")

def about(request):
    return HttpResponse("<h1>关于我们</h1><p>这是一个简单的Django应用演示。</p>")

def contact(request):
    return HttpResponse("<h1>联系我们</h1><p>邮箱: example@example.com</p>")
