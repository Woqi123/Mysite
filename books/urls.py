# @Description:
# 


# @Time : 2020/12/15 17:02 
# @Author : Woqi
# @File : urls.py 
# @Software: PyCharm

from django.urls import path

from . import views

urlpatterns = [
    path('publisher_list/', views.get_publisher_list, name='publisher_list'),
    path('add_publisher/', views.add_publisher, name='add_publisher'),
    path('del_publisher/', views.del_publisher, name='del_publisher'),
    path('update_publisher/', views.update_publisher, name='update_publisher'),

    path('book_list/', views.get_book_list, name='book_list'),
    path('add_book/', views.add_book, name='add_book'),
    path('del_book/', views.del_book, name='del_book'),
    path('update_book/', views.update_book, name='update_book'),

    path('author_list/', views.get_author_list, name='author_list'),
    path('add_author/', views.add_author, name='add_author'),
    path('del_author/', views.del_author, name='del_author'),
    path('update_author/', views.update_author, name='update_author'),

]
