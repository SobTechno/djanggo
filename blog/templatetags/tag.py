
from django import template
from blog.models import Post
import datetime

register = template.Library()


@register.simple_tag(name='post')
def PostCount():
    return Post.objects.count()

@register.simple_tag
def post_categoty_count(i):
    post_categoty_count = Post.objects.filter(status = 1,category=i).count()
    return post_categoty_count

@register.simple_tag()
def current_time(past_time):
    now = datetime.now()
    delta = now - past_time

    total_seconds = int(delta.total_seconds())

    if total_seconds < 0:
        total_seconds = abs(total_seconds)
        suffix = " باقی مانده تا آن تایم"
    else:
        suffix = " گذشته"

    days = total_seconds // 86400
    hours = (total_seconds % 86400) // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    parts = []
    if days > 0:
        parts.append(f"{days} روز")
    if hours > 0:
        parts.append(f"{hours} ساعت")
    if minutes > 0:
        parts.append(f"{minutes} دقیقه")
    if seconds > 0 or not parts:
        parts.append(f"{seconds} ثانیه")

    return " و ".join(parts) + suffix

@register.inclusion_tag('extentions/lastestPost.html')
def lastestPost():
    post = Post.objects.filter(status=1).order_by('create_at').all()
    return {'lastestPost':post}






