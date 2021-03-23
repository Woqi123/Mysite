from django.db import models


# Create your models here.

class Publisher(models.Model):
    pubid = models.CharField("出版社ID", primary_key=True, max_length=50)
    pubname = models.CharField('出版社名称', max_length=50)
    pubaddr = models.CharField('出版社地址', max_length=60)
    pubpost = models.CharField('出版社邮编', max_length=10)
    website = models.CharField('出版社网址', max_length=50)
    contact = models.CharField('联系人', max_length=8)
    contele = models.CharField('联系方式', max_length=30)
    e_mail = models.CharField('联系人E-mail', max_length=50)
    pubinfo = models.TextField('备注信息', blank=True)

    def __str__(self):
        return self.pubname


class Book(models.Model):
    bookid = models.CharField('书籍编号', primary_key=True, max_length=10)
    bookname = models.CharField('书籍名称', max_length=50)
    # authorname = models.CharField('作者名称', max_length=50)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, verbose_name='出版社')

    def __str__(self):
        return self.bookname


class Author(models.Model):
    authorid = models.CharField('作者编号', primary_key=True, max_length=10)
    authorname = models.CharField('作者名称', max_length=50)
    book = models.ManyToManyField(Book, verbose_name='出版书籍')

    def __str__(self):
        return self.authorname

