from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accountapp.models import HelloWorld


def hello_world(request):
    if request.method == "POST":
        temp = request.POST.get('hello_world_input') #request의 POST중에서 가져와라

        new_hello_world = HelloWorld() #이 빵틀에서 나온 새로운 객체 저장
        new_hello_world.text = temp
        new_hello_world.save() #DB에 저장

        return render(request, 'accountapp/hello_world.html', context={'hello_world_output': new_hello_world}) #context : 데이터 꾸러미
    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD!!!'})
