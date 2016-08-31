# encoding:utf-8
from django.shortcuts import render
from core.models import *
from django.http import HttpResponse,HttpResponseRedirect,Http404,HttpResponseNotFound
import random
import os
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import connection
from django.db.models import Q
import urllib.parse
import urllib.request
import http.client as httplib
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

def postBaiDu(filecontent, domain):
    URL = "/urls?site=www.dyhell.com&token=uUABfymakG1cPdbh"
    send_headers = {'Content-Type': 'text/plain'}
    conn = httplib.HTTPConnection("http://data.zz.baidu.com:80")
    # req = urllib2.Request(URL, data=data, headers=send_headers)
    conn.request(method="POST", url=URL, body=filecontent, headers=send_headers)
    response = conn.getresponse()
    baiduresult = response.read()
    conn.close()
    return baiduresult
def my_custom_sql(sql,*para):
    cursor = connection.cursor()

    cursor.execute(sql,*para)

    #cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
    row = cursor.fetchall()

    return row
def index(req):
    argGet = req.GET
    films=FILM.objects.all()
    try:
        paginator = Paginator(films, 50)  # Show 5 contacts per page
        page = argGet.get('page')
        try:
            filmpaged = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            filmpaged = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            filmpaged = paginator.page(paginator.num_pages)
    except:
        return HttpResponse(page)
    return render(req,'index.html',locals())
@csrf_exempt
def gitpull(req):
    msg = os.popen('sudo sh /home/ubuntu/ThunderMovie/deploy.sh').read()
    return HttpResponse(json.dumps({'msg:': msg}))

def search(req,keywords=''):
    films=FILM.objects.filter(Q(film_intro__contains=keywords)|Q(film_name__contains=keywords)|Q(film_actors__contains=keywords)|Q(film_director__contains=keywords))
    #|Q(tags__tag_name__contains=keywords)
    return render(req, 'about.html', locals())
def post(url, data):#封装post方法
    s=urllib.request.Request(url, urllib.parse.urlencode(data).encode('utf-8'))
    #s.headers={}
    # s.urlopen().read()
    s.add_header('Content-Type', 'text/plain')
    #s.add_header('Content-Type', 'text/plain')
    return  urllib.request.urlopen(s).read().decode()

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
    films = FILM.objects.all()[:7]
    newfilmd = FILM.objects.all()[:8]
    return render(request, 'Home.html', locals())


def sitemap(req):
    sitemaplist=['www.dyhell.com','www.dyhell.com/random','www.dyhell.com/movies']
    films=FILM.objects.all()
    for film in films:
        sitemaplist.append('www.dyhell.com/movie/'+str(film.id))
    with open('core/static/sitemap.txt','w') as f:
        for line in sitemaplist:
            os.popen(" curl -H 'Content-Type:text/plain' --data-binary %s 'http://data.zz.baidu.com/urls?site=www.dyhell.com&token=uUABfymakG1cPdbh' " % line)
            f.write(line+"\n")
    #i=0
    # part=0
    #allparts=[]
    # with open('core/static/sitemap.txt', 'r') as f:
    #     line=f.readline()
    #     for i in range(0,2000):
    #         line = f.readline()
    #     if i%2000==1:
    #         part+=1
    #         f=open('core/static/curl'+part+'.txt','w')
    #         f.write(line)
    #         f.close()
    #         #allparts.append('curl'+part+'.txt')
    #         msg=os.popen(" curl -H 'Content-Type:text/plain' --data-binary @/home/ubuntu/ThunderMovie/'core/static/curl%s.txt' 'http://data.zz.baidu.com/urls?site=www.dyhell.com&token=uUABfymakG1cPdbh' " % part).read()
    #     else:
    #         f.write(line)
    return HttpResponse('成功更新\n')
