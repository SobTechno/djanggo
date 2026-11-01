from django.contrib import sitemaps
from django.urls import reverse
from blog.models import Post

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        list = ["app:main", "blog:index"]
        return list

    def location(self, item):
        return reverse(item)