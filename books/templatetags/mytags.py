# @Description:
# 


# @Time : 2020/12/19 18:49 
# @Author : Woqi
# @File : mytags.py 
# @Software: PyCharm
from django import template

register = template.Library()


@register.filter
def add_arg(value, arg):
    # 功能
    return "{} ** {}".format(value, arg)


@register.simple_tag
def str_join(*args, **kwargs):
    return "{}_{}".format(''.join(args), '*'.join(kwargs.values()))


@register.inclusion_tag('pagination.html')
def pagination(n):
    # 每两个元素一页
    import math
    return {"page": range(1, int(math.ceil(n / 2 + 1)))}
