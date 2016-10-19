"""ThunderMovie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from core import views
urlpatterns = [
    url(r'^niqinmabaozha/', admin.site.urls),
    url(r'^movies$',views.index),
    url(r'^movielist$',views.seolist),
    url(r'^tvseries',views.indextvseries),
    url(r'^tv/(?P<fid>\d+)$',views.singletvseries),
    url(r'^random$',views.randomdy),
    url(r'^gitpu11$',views.gitpull),
    url(r'^result$',views.search),
    url(r'^movie/(?P<fid>\d+)$',views.single),
    url(r'^$', views.index),
    url(r'^updatesitemap', views.sitemap),
    url(r'^douban/(?P<start>\d+)/(?P<end>\d+)', views.douban),

    url(r'newmovie$', views.new_movie),

]
