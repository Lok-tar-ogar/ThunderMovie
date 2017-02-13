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


class ACTORS(models.Model):
    name = models.CharField("演员名字", max_length=100, null=True)
    douban_id = models.CharField("演员豆瓣id", max_length=100, null=True)
    alt = models.CharField("豆瓣链接", max_length= 200, null=True)
    small_douban_image = models.CharField('豆瓣演员小海报图', max_length=200, null=True)
    middle_douban_image = models.CharField('豆瓣演员中海报图', max_length=200, null=True)
    big_douban_image = models.CharField('豆瓣演员大海报图', max_length=200, null=True)
    dim_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "演员"
        verbose_name_plural = "演员们"
        ordering = ['-dim_date']


class DIRECTORS(models.Model):
    name = models.CharField("导演名字", max_length=100, null=True)
    douban_id = models.CharField("导演豆瓣id", max_length=100, null=True)
    alt = models.CharField("豆瓣链接", max_length=200, null=True)
    small_douban_image = models.CharField('豆瓣导演小海报图', max_length=200, null=True)
    middle_douban_image = models.CharField('豆瓣导演中海报图', max_length=200, null=True)
    big_douban_image = models.CharField('豆瓣导演大海报图', max_length=200, null=True)
    dim_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "导演"
        verbose_name_plural = "导演们"
        ordering = ['-dim_date']


class FILM(models.Model):
    film_name=models.CharField('电影名',max_length=50,null=False)
    tags=models.ManyToManyField(TAG_FILM)
    cover_img_link=models.CharField('封面图片链接',max_length=500,null=True)
    download_link=models.CharField('下载链接',max_length=5000,null=True)
    download_link2 = models.CharField('下载链接2', max_length=500, null=True)
    download_link3 = models.CharField('下载链接3', max_length=500, null=True)
    film_intro = models.CharField('电影剧情简介',max_length=5000, null=True)
    film_director = models.CharField('导演', max_length=50, null=True)
    film_actors=models.CharField('演员们',max_length=500,null=True)
    film_disc= models.CharField('电影评论',max_length=5000, null=True)
    film_pub_year=models.CharField('电影发行年代',max_length=50, null=True)
    film_country=models.CharField('电影来自国家',max_length=50, null=True)
    comments_count = models.CharField('短评人数', max_length=50, null=True)
    ratings_count = models.CharField('评分人数', max_length=50, null=True)
    reviews_count = models.CharField('影评人数', max_length=50, null=True)
    stars = models.CharField('电影评分', max_length=50, null=True)
    wish_count = models.CharField('想看的人数', max_length=50, null=True)
    douban_id = models.CharField('豆瓣id', max_length=50, null=True)
    douban_title = models.CharField('豆瓣电影名称', max_length=100, null=True)
    alt = models.CharField('豆瓣电影地址', max_length=100, null=True)
    collect_count = models.CharField('看过人数', max_length=50, null=True)
    origin_title = models.CharField('原名', max_length=100, null=True)
    small_douban_image = models.CharField('豆瓣电影小海报图', max_length=200, null=True)
    middle_douban_image = models.CharField('豆瓣电影中海报图', max_length=200, null=True)
    big_douban_image = models.CharField('豆瓣电影大海报图', max_length=200, null=True)
    dim_date=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.film_name
    class Meta:
        verbose_name = "电影表"
        verbose_name_plural = "电影表们"
        ordering = ['-dim_date']
class TVSERIES(models.Model):
    tvseries_name=models.CharField('电视剧名',max_length=50,null=False)
    tags=models.CharField('电视剧类型',max_length=100, null=True)
    cover_img_link=models.CharField('封面图片链接',max_length=500,null=True)
    download_link=models.CharField('下载链接',max_length=30000,null=True)
    tvseries_intro = models.CharField('电视剧情简介',max_length=5000, null=True)
    tvseries_director = models.CharField('导演', max_length=50, null=True)
    tvseries_actors=models.CharField('演员们',max_length=500,null=True)
    tvseries_disc= models.CharField('电视剧评论',max_length=5000, null=True)
    tvseries_pub_year=models.CharField('电视剧发行年代',max_length=50, null=True)
    tvseries_country=models.CharField('电视剧来自国家',max_length=50, null=True)
    dim_date=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.tvseries_name
    class Meta:
        verbose_name = "电视剧表"
        verbose_name_plural = "电视剧表们"
        ordering = ['-dim_date']



