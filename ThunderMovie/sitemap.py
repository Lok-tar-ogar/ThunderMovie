from core.models import FILM
from django.contrib.sitemaps import Sitemap

class filmSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return ['main', 'about', 'license']

    def lastmod(self, obj):
        return obj.pub_date
