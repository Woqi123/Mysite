from django.http import Http404, JsonResponse
from django.shortcuts import render, HttpResponse, redirect, reverse

from Mysite.views import login_required
from .models import Publisher, Book, Author
import time


# Create your views here.
@login_required
def get_publisher_list(request):
    all_publisher = Publisher.objects.all()
    return render(request, "publisher_list.html",
                  {"all_publisher": all_publisher, "publisher_length": len(all_publisher)})


def add_publisher(request):
    if request.method == 'POST':
        # Publisher.objects.create(**request.POST)
        pubname = request.POST.get('pubname')
        pubaddr = request.POST.get('pubaddr')
        pubpost = request.POST.get('pubpost')
        website = request.POST.get('website')
        contact = request.POST.get('contact')
        contele = request.POST.get('contele')
        e_mail = request.POST.get('e_mail')
        pubinfo = request.POST.get('pubinfo')

        if Publisher.objects.filter(pubname=pubname):
            return render(request, "add_publisher.html", {'error': "出版社名称不能重复"})

        Publisher.objects.create(pubid=str(int(time.time())), pubname=pubname, pubaddr=pubaddr, pubpost=pubpost,
                                 website=website, contact=contact,
                                 contele=contele, e_mail=e_mail, pubinfo=pubinfo)

        return redirect(reverse("publisher_list"))

    return render(request, "add_publisher.html")


def del_publisher(request):
    pubname = request.GET.get('pubname')
    pub = Publisher.objects.get(pubname=pubname)
    if pub:
        pub.delete()
    # return redirect(reverse("publisher_list"))
    return JsonResponse({'status': 200 })


def update_publisher(request):
    pubname = request.GET.get('pubname')
    try:
        pub = Publisher.objects.get(pubname=pubname)
        if request.method == 'GET':
            return render(request, "update_publisher.html", {'pub': pub})
        elif request.method == 'POST':
            pub.pubname = request.POST.get('pubname')
            pub.pubaddr = request.POST.get('pubaddr')
            pub.pubpost = request.POST.get('pubpost')
            pub.website = request.POST.get('website')
            pub.contact = request.POST.get('contact')
            pub.contele = request.POST.get('contele')
            pub.e_mail = request.POST.get('e_mail')
            pub.pubinfo = request.POST.get('pubinfo')
            pub.save()
    except Publisher.DoesNotExist:
        raise Http404("Publisher does not exist")
    return redirect(reverse("publisher_list"))


# 查询所有书籍
@login_required
def get_book_list(request):
    all_books = Book.objects.all()
    return render(request, "book_list.html", {"all_books": all_books, "books_length": len(all_books)})


def add_book(request):
    if request.method == 'POST':
        bookname = request.POST.get('bookname')
        if not bookname:
            return render(request, 'add_book.html', {'error': '书名不能为空'})
        publisher = request.POST.get('pubid')
        Book.objects.create(bookid=str(int(time.time())), bookname=bookname, publisher_id=publisher)

        return redirect(reverse("book_list"))

    all_publisher = Publisher.objects.all()
    return render(request, 'add_book.html', {'all_publisher': all_publisher})


def del_book(request):
    book_id = request.GET.get('bookid')
    Book.objects.filter(bookid=book_id).delete()
    return JsonResponse({'status': 200, })


def update_book(request):
    book_id = request.GET.get('bookid')
    try:
        book = Book.objects.get(bookid=book_id)
        if request.method == 'GET':
            all_publisher = Publisher.objects.all()
            return render(request, "update_book.html", {'book': book, 'all_publisher': all_publisher})
        elif request.method == 'POST':
            book.bookname = request.POST.get('bookname')
            book.publisher_id = request.POST.get('pubid')
            book.save()
    except Publisher.DoesNotExist:
        raise Http404("book does not exist")
    return redirect(reverse("book_list"))


# 查询所有作者
def get_author_list(request):
    all_authors = Author.objects.all()
    for author in all_authors:
        print(author.book)
        print(author.book.all())

    return render(request, "author_list.html", {'all_authors': all_authors, "authors_length": len(all_authors)})


# 新增作者
def add_author(request):
    all_books = Book.objects.all()
    if request.method == 'POST':
        authorname = request.POST.get('authorname')
        book_ids = request.POST.getlist('book_ids')  # 获取多个数据
        author_obj = Author.objects.create(authorid=str(int(time.time())), authorname=authorname)

        # 绑定作者与书籍之间多对多的关系
        author_obj.book.set(book_ids)

        return redirect(reverse("author_list"))
    return render(request, "add_author.html", {'all_books': all_books})


def del_author(request):
    author_id = request.GET.get('authorid')
    Author.objects.filter(authorid=author_id).delete()
    return JsonResponse({'status': 200, })


def update_author(request):
    author_id = request.GET.get('authorid')
    try:
        author = Author.objects.get(authorid=author_id)
        if request.method == 'GET':
            all_books = Book.objects.all()
            return render(request, "update_author.html", {'author': author, 'all_books': all_books})
        elif request.method == 'POST':

            author.authorname = request.POST.get('authorname')
            author.save()

            book_ids = request.POST.getlist('book_ids')  # 获取多个数据
            # 绑定作者与书籍之间多对多的关系
            author.book.set(book_ids)
            return redirect(reverse("author_list"))
    except Publisher.DoesNotExist:
        raise Http404("book does not exist")
    return redirect(reverse("book_list"))
