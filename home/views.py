from django.shortcuts import render, HttpResponse
from pprint import pprint
import random
# Create your views here.
def index(request):
    # print(request)
    # print(type(request))
    # pprint(request.META)
    return HttpResponse("Welcome to Dajango !")

def dinner(requset):
    dinner = ['불고기', '김치찌개', '삼겹살', '수타면']
    choice  = random.choice(dinner)
    # print(choice)
    # return HttpResponse(choice)
    return render(requset, 'dinner.html',{'choice':choice, 'dinner':dinner})
    
def hello(requset, name):
    return render(requset, 'hello.html', {'name':name})
    
def cube(requset, num):
    result = int(num)**3
    return render(requset, 'cube.html', {'result':result})
    
def ping(request):
    return render(request, 'ping.html')

def pong(request):
    print(request.GET)
    data = request.GET.get('data')
    return render(request, 'pong.html',{'data':data})

def user_new(request):
    return render(request, 'user_new.html')
    
def user_create(request):
    return render(request, 'user_create.html')

    
    
    