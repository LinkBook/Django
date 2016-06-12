from django.contrib.auth.models import User
from django.db.models import *
import datetime


class Karbar(Model):
    name = CharField(max_length=100, verbose_name="نام", blank=True)
    username = CharField(max_length=100, verbose_name="نام کاربری ")
    email = CharField(max_length=100, verbose_name="ایمیل")
    password = CharField(max_length=100, verbose_name="پسورد")
    rep = CharField(max_length=100, verbose_name="تکرار پسورد")

    def __str__(self):
        return self.username


class login(Model):
    username = CharField(max_length=100, verbose_name="نام کاربری")
    password = CharField(max_length=100, verbose_name="رمز عبور")

    def __str__(self):
        return self.username


class Category(Model):
    category_name = CharField(max_length=50, verbose_name="دسته بندی ها")

    def __str__(self):
        return self.category_name


class SubCategory(Model):
    category = ForeignKey(Category, verbose_name="شاخه")
    subcategory = CharField(max_length=50, verbose_name="زیرشاخه")

    def __str__(self):
        return self.subcategory


class Webpage(Model):
    user = ForeignKey(User, null=False, verbose_name="کاربر")
    title = CharField(max_length=100, verbose_name="عنوان")
    vision = TextField(verbose_name="چشم انداز")
    mission = TextField(verbose_name="ماموریت")
    service_product = TextField(verbose_name="محصولات و خدمات")
    Webpage_logo = FileField(upload_to='Webpagelogo/%Y/%m/%d', verbose_name="وب لوگو")
    Webpage_url = URLField(verbose_name="آدرس سایت")

    def __str__(self):
        return self.title

    def Edit_Webpage(self):
        return 'Edit'


# festival class
class Festival(Model):
    webpage = ForeignKey(Webpage, null=False, verbose_name="افتخارات وب سایت")
    fest_title = CharField(max_length=100, verbose_name="عنوان افتخارات")
    fest_logo = FileField(upload_to='Festivallogo/%Y/%m/%d', verbose_name="لوگوی افتخارات")
    fest_text = TextField(verbose_name="توضیح افتخارات")
    fest_url = URLField(verbose_name="آدرس افتخارات")

    def __str__(self):
        return self.fest_title


class Subscribe(Model):
    webpage = ForeignKey(Webpage, null=False, verbose_name="اشتراک وب")
    userEmail = EmailField(null=False, verbose_name="ایمیل مشترکین")

    def __str__(self):
        return self.userEmail


class Comments(Model):
    comment_name = CharField(max_length=30, verbose_name="نام")
    comment_email = EmailField(null=False, verbose_name="ایمیل")
    date_send = DateTimeField(default=datetime.datetime.now(), blank=True, verbose_name="زمان ارسال")
    comment = TextField(null=False, verbose_name="محتوای کامنت")

    def __str__(self):
        return self.comment


class Tag(Model):
    webpage = ForeignKey(Webpage, verbose_name="وب تگ")
    tag_name = CharField(max_length=30, verbose_name="نام برچسب")

    def __str__(self):
        return self.tag_name


# contact class
class Contact(Model):
    name = CharField(max_length=30, verbose_name="نام")
    email = EmailField(null=False, verbose_name="ایمیل")
    message = TextField(null=False, verbose_name="محتوای پیام")

    def __str__(self):
        return self.message
