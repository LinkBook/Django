from django.contrib.auth.models import User
from django.db.models import *
import datetime


class Karbar(Model):
    name = CharField(max_length=100, verbose_name="نام", blank=True)
    username = CharField(max_length=100, verbose_name="نام کاربری ")
    email = CharField(max_length=100, verbose_name="ایمیل")
    password = CharField(max_length=100, verbose_name="پسورد")
    rep = CharField(max_length=100, verbose_name="تکرار پسورد")


class login(Model):
    username = CharField(max_length=100)
    password = CharField(max_length=100)


class Category(Model):
    category_name = CharField(max_length=50)


class SubCategory(Model):
    category = ForeignKey(Category)
    subcategory = CharField(max_length=50)


class Webpage(Model):
    user = ForeignKey(User, null=False)
    title = CharField(max_length=100)
    vision = TextField()
    mission = TextField()
    service_product = TextField()
    Webpage_logo = FileField(upload_to='Webpagelogo/%Y/%m/%d')
    Webpage_url = URLField()

    def __str__(self):
        return self.title

    def Edit_Webpage(self):
        return 'Edit'


# festival class
class Festival(Model):
    webpage = ForeignKey(Webpage, null=False)
    fest_title = CharField(max_length=100)
    fest_logo = FileField(upload_to='Festivallogo/%Y/%m/%d')
    fest_text = TextField()
    fest_url = URLField()

    def __str__(self):
        return self.ftitle


class Subscribe(Model):
    webpage = ForeignKey(Webpage, null=False)
    userEmail = EmailField(null=False)


class Comments(Model):
    comment_name = CharField(max_length=30, verbose_name="نام")
    comment_email = EmailField(null=False, verbose_name="ایمیل")
    date_send = DateTimeField(default=datetime.datetime.now(), blank=True)
    comment = TextField(null=False, verbose_name="محتوای کامنت")

    def __str__(self):
        return self.comment


class Tag(Model):
    webpage = ForeignKey(Webpage)
    tag_name = CharField(max_length=30)


# contact class
class Contact(Model):
    name = CharField(max_length=30, verbose_name="نام")
    email = EmailField(null=False, verbose_name="ایمیل")
    message = TextField(null=False, verbose_name="محتوای پیام")

    def __str__(self):
        return self.message
