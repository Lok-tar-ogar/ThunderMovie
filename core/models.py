# encoding:utf-8
from django.db import models

class TAG_FILM(models.Model):
    tag_name=models.CharField('标签名称',max_length=50,null=False)
    dim_date=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = "标签对照表"
        verbose_name_plural = "标签对照们"
        ordering = ['id']


class FILM(models.Model):
    film_name=models.CharField('电影名',max_length=50,null=False)
    tags=models.ManyToManyField(TAG_FILM)
    cover_img_link=models.CharField('封面图片链接',max_length=500,null=True)
    download_link=models.CharField('下载链接',max_length=5000,null=True)
    film_intro = models.CharField('电影剧情简介',max_length=5000, null=True)
    film_director = models.CharField('导演', max_length=50, null=True)
    film_actors=models.CharField('演员们',max_length=500,null=True)
    film_disc= models.CharField('电影评论',max_length=5000, null=True)
    film_pub_year=models.CharField('电影发行年代',max_length=50, null=True)
    film_country=models.CharField('电影来自国家',max_length=50, null=True)
    dim_date=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.film_name
    class Meta:
        verbose_name = "电影表"
        verbose_name_plural = "电影表们"
        ordering = ['-dim_date']
