from django.shortcuts import HttpResponse, render


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        return "欢迎来到王者峡谷"

    def __str__(self):
        return "name :{} , age: {}".format(self.name, self.age)


def index(request):
    num = 1
    str = "This is a new project: Mysite"
    name_list = ['woqi', "scq", "yf", 'cwx']
    dic = {"name": "woqi", "age": 25}
    tup = ('woqi', "scq", "yf", 'cwx')
    name_set = {'woqi', "scq", "yf", 'cwx'}

    woqi = Person("woqi", 25)
    return render(request, "test.html", {
        'num': num,
        'str': str,
        'name_list': name_list,
        'dic': dic,
        'tup': tup,
        'name_set': name_set,
        'person': woqi,
        'blank': "",  # 或者为空列表、空字典
        'filesize': 1024 * 1024 * 1024,

        'add_test': 10

    })
