from django.forms import forms
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import User

from django.conf import global_settings

# print(globals())


# Create your views here.
def login(request):
    print(request.method)
    if request.method == 'POST':
        # 处理POST请求的逻辑
        # 获取用户名与密码
        print(request.POST, type(request.POST))
        username = request.POST.get('user')
        password = request.POST.get('pwd')
        if User.objects.filter(username=username, password=password):
            url = request.GET.get("url")
            if url:
                return_url = url
            else:
                return_url = reverse('index')

            ret = redirect(return_url)
            ret.set_cookie("is_login", '1') #设置Cookie
            # request.session['is_login'] = 1
            return ret
    return render(request, 'login.html')

class Test(forms.Form):
    pass
def test():

    test = Test()
    test.is_valid()