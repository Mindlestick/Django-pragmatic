from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld


def hello_world(request):
    if request.method == "POST":
        temp = request.POST.get('hello_world_input') #request의 POST중에서 가져와라

        new_hello_world = HelloWorld() #이 빵틀에서 나온 새로운 객체 저장
        new_hello_world.text = temp
        new_hello_world.save() #DB에 저장

        return HttpResponseRedirect(reverse('accountapp:hello_world')) #이 주소로 돌아갈 수 있게 재접속 (urls에서) reverse로 감싸줘야됨
    else:
        hello_world_list = HelloWorld.objects.all()  # DB에 있는 모든 데이터 불러오기
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list}) #context : 데이터 꾸러미


class AccountCreateView(CreateView):
    # 1. 무슨 모델을 사용할 것인지?
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world') #계정 만드는 데 성공했다면/ 클래스에서는 reverse_lazy 사용 함수에서는 reverse 사용
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world') #계정 만드는 데 성공했다면/ 클래스에서는 reverse_lazy 사용 함수에서는 reverse 사용
    template_name = 'accountapp/update.html'

class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'