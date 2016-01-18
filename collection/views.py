#encoding:utf-8
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.conf import settings
from django.db import transaction
import json
import logging

logger = logging.getLogger(__name__)
from models import *


@csrf_exempt
def wechat_url(request, token):
    ''''微信配置回调'''
    if request.method == 'GET' and token == settings.TOKEN:
        echostr = request.GET.get('echostr','')
        return HttpResponse(echostr)


def is_authed(request):
    '''判断用户是否认证'''
    if request.user.is_authenticated():
        return True
    else:
        return False


def login(request):
    if is_authed(request):
        return render(request,'index.html')
    else:
        return HttpResponseRedirect('/login/weixin/?next=/')


def share(request):
    id = request.GET.get('id','')
    if is_authed(request):
        return render(request,'index.html',{'id',id})
    else:
        return HttpResponseRedirect('/login/weixin/?next=share?id='+id)


@transaction.atomic
@require_http_methods(['POST'])
@csrf_exempt
def update_force(request):
    if not is_authed(request):
        return JsonResponse({'message':'user is not authed!'},status=400)

    data = json.loads(request.body)
    id = data.get('id','')
    try:
        person = Person.objects.get(id=id)
    except:
        return JsonResponse({'message':'no person! '},status=400)

    user = request.user
    if user in person.add_user.all() or user.id == person.user.id:
        return JsonResponse({'message':'you have added force for this person!','result':'fail'},status=200)

    person.add_user.add(request.user)
    person.force = person.force + 10
    person.save()
    return JsonResponse({'personId':person.id}, status=200)

@transaction.atomic
@require_http_methods(['POST'])
@csrf_exempt
def reward(request):
    '''抽奖'''
    user = request.user
    if not is_authed():
        return JsonResponse({'message':'user is not authed!'},status=400)
    if DrawRecord.objects.filter(user=user).exists():
        return JsonResponse({'message':'you have drawed!'},status=400)
    try:
        person = Person.objects.get(user=user)
        if person.drawed:
            return JsonResponse({'message':'you have drawed!'},status=400)
        if person.force < 100:
            return JsonResponse({'message':'your force is not enough!'},status=400)
        else:
            person.drawed = True
            person.save()
            rewards = ['dataLine','storageBox','Upan']
            for i in range[27]: #十分之一的中奖概率
                rewards.append('none')
            reward_type = random.choice(rewards)
            if reward_type != 'none':
                reward = Reward.objects.filter(type=reward_type)
                DrawRecord.objects.create(user=user,reward=reward)
                reward.remain = reward.remain - 1
                reward.save()
            return JsonResponse({'reward':reward_type},status=200)
    except:
        return JsonResponse({'message':'no person'},status=400)


@csrf_exempt
def person(request):
    '''保存个人信息'''
    user = request.user
    if not is_authed(request):
        return JsonResponse({'message':'user is not authed!'},status=400)
    if request.method == 'POST':
        if Person.objects.filter(user=user).exists():
            return JsonResponse({'message':'you message have saved!'},status=400)
        data = json.loads(request.body)
        name = data.get('name','')
        phone = data.get('phone','')
        address = data.get('address','')
        if name and phone and address and force:
            try:
                person = Person.objects.create(user=user,name=name,phone=phone,address=address,force=10)
            except:
                error = 'person save fail ----userId:' + str(user.id) + 'name:' + name + ' phone:'+ phone +' address:' + address
                logger.exception(error)
                return JsonResponse({'message':'Server Internal Error'},status=500)
            return JsonResponse({'personId':person.id},status=200)
        else:
            return JsonResponse({'message':'all param is required!'},status=400)

    elif request.method == 'GET':
        try:
            person = Person.objects.filter(user=user).values('name','phone','address','force')[0]
        except:
            person = None
        return JsonResponse({'person':person},status=200)
