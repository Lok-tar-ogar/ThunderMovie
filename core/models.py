from django.db import models
class   FILM(models.Model):
    film_name=models.CharField(max_length=50,null=False)
    tags=models.ManyToManyField(TAG_FILM)
    download_link=models.CharField(max_length=500,null=True)
    dim_date=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.film_name
    class Meta:
        verbose_name = "电影表"
        verbose_name_plural = "电影表们"
        ordering = ['id']

class TAG_FILM(models.Model):
    tag_name=models.CharField(max_length=50,null=False)
    dim_date=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = "标签对照表"
        verbose_name_plural = "电影表们"
        ordering = ['id']

# Create your models here.
