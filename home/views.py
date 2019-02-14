from django.shortcuts import render, HttpResponse
from pprint import pprint
import random
from datetime import datetime



# Create your views here.
def index(request):
    # print(request)
    # print(type(request))
    # pprint(request.META)
    #return HttpResponse("Welcome to Dajango !")
    return render(request,'home/index.html')

def dinner(request):
    dinner = ['불고기', '김치찌개', '삼겹살', '수타면']
    choice  = random.choice(dinner)
    # print(choice)
    # return HttpResponse(choice)
    return render(request, 'home/dinner.html',{'choice':choice, 'dinner':dinner})
    
def hello(request, name):
    return render(request, 'home/hello.html', {'name':name})
    
def cube(requset, num):
    result = int(num)**3
    return render(requset, 'home/cube.html', {'result':result})
    
def ping(request):
    return render(request, 'home/ping.html')

def pong(request):
    print(request.GET)
    data = request.GET.get('data')
    return render(request, 'home/pong.html',{'data':data})

def user_new(request):
    return render(request, 'home/user_new.html')
        
def user_create(request):
    nickname = request.POST.get('nickname')
    password = request.POST.get('password')
    return render(request, 'home/user_create.html', {'nickname':nickname, 'password':password})
    
def template_example(request):
    my_list = ['짜장면','탕수육','짬뽕','양장피']
    my_sentence = 'Life is short you need python'
    messages = ['apple','banana','cucumber','mango']
    empty_list=[]
    datetimenow = datetime.now()
    return render(request,'home/template_example.html',
                {'my_list' : my_list,
                'my_sentence' : my_sentence,
                'messages': messages,
                'empty_list' : empty_list,
                'datetimenow' : datetimenow
                }
                )
                
def static_example(request):
    return render(request, 'home/static_example.html')



















    
    