# encoding:utf-8
from django.shortcuts import render
from core.models import *
from django.http import HttpResponse,HttpResponseRedirect,Http404,HttpResponseNotFound
import random
import os
import json
from django.views.decorators.csrf import csrf_exempt
# import sys
#
# reload(sys)
# sys.setdefaultencoding('utf-8')
def index(req):
    films=FILM.objects.all()[:50]
    return render(req,'index.html',locals())
@csrf_exempt
def gitpull(req):
    msg = os.popen('sudo sh /home/ubuntu/ThunderMovie/deploy.sh').read()
    return HttpResponse(json.dumps({'msg:': msg}))

def search(req,keywords=''):
    films=FILM.objects.filter(film_intro__contains=keywords,film_name__contains=keywords)
    return render(req, 'about.html', locals())

def single(req,fid=0):
    try:
        film=FILM.objects.get(id=fid)
        tags=film.tags.all()
        film.download_link = film.download_link.split('\n')
        return render(req,'single.html',locals())
    except Exception as e:
        return HttpResponseNotFound()

def randomdy(req):
    ran=random.randint(1,10000)
    films = FILM.objects.all()[ran:50+ran]
    return render(req, 'randomdy.html', locals())


def homepage(request):
    films=FILM.objects.all()[:5]
    return render(request, 'Home.html', locals())