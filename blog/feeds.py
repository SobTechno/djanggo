from django.contrib.syndication.views import Feed
from blog.models import Post


class LatestEntriesFeed(Feed):
    title = "blog newests"
    link = "/rss/feeds"
    description = "best blog that ever have been"

    def items(self):
        return Post.objects.filter(status = True)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:100]
