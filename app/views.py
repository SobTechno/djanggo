from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
from web.forms import CommentForm


def about_view(request):
    return render(request,'about.html')
def home(request):
    p = Post.objects.filter(status = 1).all()
    user = request.user
    content = {'post':p,'user':user}
    return render(request,'index.html',content)

def test(request):
  
    if request.method == "POST":
        name= (request.POST)
    form = CommentForm() 
    
    return render(request,'test.html',{'form':form})    
