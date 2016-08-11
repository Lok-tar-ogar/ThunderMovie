from django.shortcuts import render
from core.models import *
from django.http import HttpResponse,HttpResponseRedirect,Http404,HttpResponseNotFound
def index(req):
    films=FILM.objects.all().distinct()[:200]
    return render(req,'index.html',locals())


def search(req,keywords=''):
    films=FILM.objects.filter(film_name__contains=keywords,film_html__contains=keywords)
    return render(req, 'about.html', locals())

def single(req,fid=0):
    try:
        film=FILM.objects.get(id=fid)
        tags=film.tags.all()
        return render(req,'single.html',locals())
    except Exception as e:

        return HttpResponseNotFound()