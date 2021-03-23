from functools import wraps

from django.shortcuts import render, redirect


def login_required(func):
    @wraps(func)
    def inner(request, *args, **kwargs):
        print(request.COOKIES)
        is_login = request.COOKIES.get("is_login")  # 获取Cookie
        # is_login = request.session.get('is_login')
        print(is_login, type(is_login))
        if is_login != '1':
            return redirect("/users/login/?url={}".format(request.path_info))
        ret = func(request, *args, **kwargs)
        return ret

    return inner


@login_required
def index(request):
    return render(request, "index.html")
