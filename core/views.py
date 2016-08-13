from django.shortcuts import render
from core.models import *
from django.http import HttpResponse,HttpResponseRedirect,Http404,HttpResponseNotFound
import random
def index(req):
    films=FILM.objects.all()[:50]
    return render(req,'index.html',locals())


def search(req,keywords=''):
    films=FILM.objects.filter(film_intro__contains=keywords,film_intro__contains=keywords)
    return render(req, 'about.html', locals())

def single(req,fid=0):
    try:
        film=FILM.objects.get(id=fid)
        tags=film.tags.all()
        return render(req,'single.html',locals())
    except Exception as e:

        return HttpResponseNotFound()

def randomdy(req):
    ran=random.randint(1,1000)
    films = FILM.objects.all()[1*ran:50*ran]
    return render(req, 'randomdy.html', locals())