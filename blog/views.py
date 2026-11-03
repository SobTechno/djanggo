from django.shortcuts import render,get_object_or_404,redirect,get_list_or_404
from .models import Post,Comment,Category
from django.core.paginator import Paginator
from web.forms import CommentForm
from django.contrib import messages


def category_name_fun(arg):
        c = Category.objects.filter(name=arg).first()
        if c :
         return c.id


def blog_view(request,arg=None):
   if request.method == "GET":
      if request.GET.get('search'):
          post=Post.objects.filter(status = 1).filter(title__contains=request.GET.get('search')).all()
          category_status = 1
      else:
         if arg != None:
            post=get_list_or_404(Post.objects.filter(status = 1).filter(category=category_name_fun(arg)).all())
            category_status = 1
         else:
            post = Post.objects.filter(status = 1).all()
            category_status = 0
      category_status = 0
   categoty = Category.objects.all()
   p = Paginator(post,2)
   page_number = request.GET.get('page')
   page_object = p.get_page(page_number)
   content = {'post':page_object,'category':categoty,'categoty_status':category_status}
   return render(request,'blog-home.html',content)





def blog_single(request,name):
   form = CommentForm()
   if request.method == "GET":
      p =get_object_or_404(Post.objects.filter(status = 1 , slug = name))
      p.count_view +=1
      p.save()
      c = Comment.objects.filter(status = 1 ,post_id= p).all()
      content =  {'post':p,
                  'comment':c,
                  'form':form
                  }
      
      return render(request,'blog-single.html',content)
      
   else:
      username = request.POST.get('name')
      email = request.POST.get('email')
      text = request.POST.get('text')
      if username and email and text and form.is_valid:
         p =Post.objects.filter(status = 1 , slug = name).first()
         c = Comment(name = username,email = email,text=text ,post_id=p)
         c.save()
         messages.add_message(request, messages.SUCCESS, "success")
      else:
         messages.add_message(request, messages.ERROR, "error")

      return redirect(f'/blog/{name}')

