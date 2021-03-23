import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Mysite.settings')
import django

django.setup()  # 需要项目进行的操作

a = 999999999
print(id(a))


def x(a):
    print(id(a))
    b = a
    print(id(b))

x(a)
