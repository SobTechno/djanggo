from django.contrib import admin
from .models import Post,Comment,Category
import time
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    post = Post.objects.all()
    date_hierarchy = 'create_at'
    list_display = ('title','status','count_view','author')
    list_filter = ('status',)
    search_fields = ['title/']
    summernote_fields='__all__'

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','status','post_id')
    list_filter = ('status',)

admin.site.register(Category)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
