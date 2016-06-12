from django.contrib.auth.models import User
from django.db.models import *
import datetime
from django.conf import settings


class Member(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    phone_number = CharField(max_length=10)
    national_code = CharField(max_length=10)


class Category(Model):
    category_name = CharField(max_length=50, verbose_name="دسته بندی ها")

    def __str__(self):
        return self.category_name

    class Meta:
        ordering = ['category_name']
        verbose_name = 'شاخه'


class SubCategory(Model):
    category = ForeignKey(Category, verbose_name="شاخه")
    subcategory = CharField(max_length=50, verbose_name="زیرشاخه")

    def __str__(self):
        return self.subcategory

    class Meta:
        ordering = ['subcategory']
        verbose_name = 'زیرشاخه'


class Webpage(Model):
    user = ForeignKey(User, null=False, verbose_name="کاربر")
    title = CharField(max_length=100, verbose_name="عنوان")
    vision = TextField(verbose_name="چشم انداز")
    mission = TextField(verbose_name="ماموریت")
    service_product = TextField(verbose_name="محصولات و خدمات")
    Webpage_logo = FileField(upload_to='Webpagelogo/%Y/%m/%d', verbose_name="وب لوگو")
    Webpage_url = URLField(verbose_name="آدرس سایت")
    Sub = ManyToManyField(SubCategory, verbose_name="دسته مربوطه")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'صفحه وب سایت'


class Festival(Model):
    webpage = ForeignKey(Webpage, null=False, verbose_name="افتخارات وب سایت", default=1)
    fest_title = CharField(max_length=100, verbose_name="عنوان افتخارات")
    fest_logo = FileField(upload_to='Festivallogo/%Y/%m/%d', verbose_name="لوگوی افتخارات")
    fest_text = TextField(verbose_name="توضیح افتخارات")
    fest_url = URLField(verbose_name="آدرس افتخارات")

    def __str__(self):
        return self.fest_title

    class Meta:
        ordering = ['fest_title']
        verbose_name = 'عنوان و افتخار'


class Subscribe(Model):
    webpage = ForeignKey(Webpage, null=False, verbose_name="اشتراک وب")
    userEmail = EmailField(null=False, verbose_name="ایمیل مشترکین")

    def __str__(self):
        return self.userEmail

    class Meta:
        verbose_name = 'خبرنامه'


class Comments(Model):
    comment_name = CharField(max_length=30, verbose_name="نام")
    comment_email = EmailField(null=False, verbose_name="ایمیل")
    date_send = DateTimeField(default=datetime.datetime.now(), blank=True, verbose_name="زمان ارسال")
    comment = TextField(null=False, verbose_name="محتوای کامنت")

    def __str__(self):
        return self.comment

    class Meta:
        ordering = ['comment_name']
        verbose_name = 'کامنت'


class Contact(Model):
    name = CharField(max_length=30, verbose_name="نام")
    email = EmailField(null=False, verbose_name="ایمیل")
    message = TextField(null=False, verbose_name="محتوای پیام")

    def __str__(self):
        return self.message

    class Meta:
        ordering = ['email']
        verbose_name = 'پیام'
