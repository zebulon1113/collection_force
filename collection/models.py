#encoding=utf-8
from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    user = models.OneToOneField(User,related_name='person')
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=100)
    force = models.IntegerField(u'原力值',default=0)
    add_user = models.ManyToManyField(User,related_name='add_user')#增加原力的人
    drawed = models.BooleanField(u'是否抽过奖',default=False)


#class ForceRecord(models.Model):


class Reward(models.Model):  #奖励
    TYPES = (
        ('dataLine','数据线'),
        ('storageBox','收纳盒'),
        ('Upan','U盘'),
        ('none','未中奖'),
    )
    type = models.CharField(u'奖励类型',choices=TYPES, max_length=50,default='qikuBag')
#    number = models.CharField(u'奖券号',unique=True,max_length=20)
#    password = models.CharField(u'奖券密码',default=0,max_length=20)
    remain = models.IntegerField(u'剩余奖券总数',default=0)
    amount = models.IntegerField(u'奖券总数',default=0)


class DrawRecord(models.Model):  #抽奖记录
    user = models.OneToOneField(User, related_name='draw')
    reward = models.ForeignKey(Reward,related_name='draw')
    created_time = models.DateTimeField(auto_now_add=True)
