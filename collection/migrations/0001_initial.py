# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DrawRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=11)),
                ('address', models.CharField(max_length=100)),
                ('force', models.IntegerField(default=0, verbose_name='\u539f\u529b\u503c')),
                ('add_user', models.ManyToManyField(related_name='add_user', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(related_name='person', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(default=b'qikuBag', max_length=50, verbose_name='\u5956\u52b1\u7c7b\u578b', choices=[(b'dataLine', b'\xe6\x95\xb0\xe6\x8d\xae\xe7\xba\xbf'), (b'storageBox', b'\xe6\x94\xb6\xe7\xba\xb3\xe7\x9b\x92'), (b'Upan', b'U\xe7\x9b\x98')])),
                ('number', models.CharField(unique=True, max_length=20, verbose_name='\u5956\u5238\u53f7')),
                ('password', models.CharField(default=0, max_length=20, verbose_name='\u5956\u5238\u5bc6\u7801')),
                ('remain', models.IntegerField(default=0, verbose_name='\u5269\u4f59\u5956\u5238\u603b\u6570')),
                ('amount', models.IntegerField(default=0, verbose_name='\u5956\u5238\u603b\u6570')),
            ],
        ),
        migrations.AddField(
            model_name='drawrecord',
            name='reward',
            field=models.ForeignKey(related_name='draw', to='collection.Reward'),
        ),
        migrations.AddField(
            model_name='drawrecord',
            name='user',
            field=models.OneToOneField(related_name='draw', to=settings.AUTH_USER_MODEL),
        ),
    ]
