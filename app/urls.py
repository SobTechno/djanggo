from django.contrib.sitemaps.views import sitemap
from django.urls import path,include
from .sitemaps import StaticViewSitemap
from blog.sitemaps import BlogSitemap
from .views import *
app_name = 'app'
sitemaps = {
    "static": StaticViewSitemap,
    'blog': BlogSitemap
}

urlpatterns = [
    path('about',about_view,name='about'),
    path('',home,name='main'),
    path('test',test,name='test'),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path('robots.txt', include('robots.urls')),
]