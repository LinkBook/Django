# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-10 13:28
from __future__ import unicode_literals

import datetime

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_name', models.CharField(max_length=30)),
                ('comment_email', models.EmailField(max_length=254)),
                ('date_send',
                 models.DateTimeField(blank=True, default=datetime.datetime(2016, 6, 10, 17, 58, 6, 861381))),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Festival',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fest_title', models.CharField(max_length=100)),
                ('fest_logo', models.FileField(upload_to='Festivallogo/%Y/%m/%d')),
                ('fest_text', models.TextField()),
                ('fest_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory', models.CharField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebCastle.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userEmail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Webpage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('vision', models.TextField()),
                ('mission', models.TextField()),
                ('service_product', models.TextField()),
                ('Webpage_logo', models.FileField(upload_to='Webpagelogo/%Y/%m/%d')),
                ('Webpage_url', models.URLField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='tag',
            name='webpage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebCastle.Webpage'),
        ),
        migrations.AddField(
            model_name='subscribe',
            name='webpage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebCastle.Webpage'),
        ),
        migrations.AddField(
            model_name='festival',
            name='webpage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebCastle.Webpage'),
        ),
    ]
