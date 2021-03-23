# @Description:
# 


# @Time : 2020/12/15 15:58 
# @Author : Woqi
# @File : urls.py 
# @Software: PyCharm

from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login, name='login'),
]
