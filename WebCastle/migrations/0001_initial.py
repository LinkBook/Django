# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('category_name', models.CharField(verbose_name='دسته بندی ها', max_length=50)),
            ],
            options={
                'ordering': ['category_name'],
                'verbose_name': 'شاخه',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('comment_name', models.CharField(verbose_name='نام', max_length=30)),
                ('comment_email', models.EmailField(verbose_name='ایمیل', max_length=254)),
                ('date_send',
                 models.DateTimeField(blank=True, default=datetime.datetime(2016, 6, 26, 14, 43, 26, 595429),
                                      verbose_name='زمان ارسال')),
                ('comment', models.TextField(verbose_name='محتوای کامنت')),
            ],
            options={
                'ordering': ['comment_name'],
                'verbose_name': 'کامنت',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='نام', max_length=30)),
                ('email', models.EmailField(verbose_name='ایمیل', max_length=254)),
                ('message', models.TextField(verbose_name='محتوای پیام')),
            ],
            options={
                'ordering': ['email'],
                'verbose_name': 'پیام',
            },
        ),
        migrations.CreateModel(
            name='Festival',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('fest_title', models.CharField(verbose_name='عنوان افتخارات', max_length=100)),
                ('fest_logo', models.FileField(upload_to='Festivallogo/%Y/%m/%d', verbose_name='لوگوی افتخارات')),
                ('fest_text', models.TextField(verbose_name='توضیح افتخارات')),
                ('fest_url', models.URLField(verbose_name='آدرس افتخارات')),
            ],
            options={
                'ordering': ['fest_title'],
                'verbose_name': 'عنوان و افتخار',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('phone_number', models.CharField(max_length=10)),
                ('national_code', models.CharField(max_length=10)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('subcategory', models.CharField(verbose_name='زیرشاخه', max_length=50)),
                ('category', models.ForeignKey(verbose_name='شاخه', to='WebCastle.Category')),
            ],
            options={
                'ordering': ['subcategory'],
                'verbose_name': 'زیرشاخه',
            },
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('userEmail', models.EmailField(verbose_name='ایمیل مشترکین', max_length=254)),
            ],
            options={
                'verbose_name': 'خبرنامه',
            },
        ),
        migrations.CreateModel(
            name='Webpage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(verbose_name='عنوان', max_length=100)),
                ('vision', models.TextField(verbose_name='چشم انداز')),
                ('mission', models.TextField(verbose_name='ماموریت')),
                ('service_product', models.TextField(verbose_name='محصولات و خدمات')),
                ('Webpage_logo', models.FileField(upload_to='Webpagelogo/%Y/%m/%d', verbose_name='وب لوگو')),
                ('Webpage_url', models.URLField(verbose_name='آدرس سایت')),
                ('Sub', models.ManyToManyField(verbose_name='دسته مربوطه', to='WebCastle.SubCategory')),
                ('user', models.ForeignKey(verbose_name='کاربر', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'صفحه وب سایت',
            },
        ),
        migrations.AddField(
            model_name='subscribe',
            name='webpage',
            field=models.ForeignKey(verbose_name='اشتراک وب', to='WebCastle.Webpage'),
        ),
        migrations.AddField(
            model_name='festival',
            name='webpage',
            field=models.ForeignKey(default=1, verbose_name='افتخارات وب سایت', to='WebCastle.Webpage'),
        ),
    ]
