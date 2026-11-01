from django.db import models
from app.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
         return self.name
    

    
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(max_length=200,null=True)
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    count_view = models.IntegerField(default=0)
    tag = models.IntegerField(null=True)
    status = models.BooleanField(default=False)
    category = models.ManyToManyField(Category)
    create_at =models.DateField(null=True)
    image = models.ImageField(upload_to='blog-img/',default='static/img/feature-img1.jpg',null=True)
    class Meta():
        ordering = ['create_at']

    def __str__(self):
        return f'{self.title}' + '-' + f'{self.id}'

    def snipper(self):
         return self.content[:100]
    def get_absolute_url(self):
         return reverse('blog:single',kwargs={'name':self.slug})
        

class Comment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100,null=True)
    text = models.TextField()
    post_id = models.ForeignKey('Post',on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    publish_at = models.DateField(null=True)

    def __str__(self):
            return f'{self.name}' + '-' + f'{self.post_id}'






