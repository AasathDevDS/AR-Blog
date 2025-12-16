from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect
from .models import Blog,Category,Comment
from django.db.models import Q 
# Create your views here.
def post_by_category(request,category_id):
  posts = Blog.objects.filter(status = 1, category_id=category_id)
  category =get_object_or_404(Category,pk = category_id)
  context = {
    'posts':posts,
    'category':category,
  }
  return render(request,'post_by_category.html', context)


def get_page(request,slug):
  single_blog = get_object_or_404(Blog, slug = slug, status = 1)
  comments = Comment.objects.filter(blog = single_blog)
  if request.method == "POST":
    comments = Comment()
    comments.user = request.user
    comments.blog = single_blog
    comments.comment = request.POST['comment']
    comments.save()
    return HttpResponseRedirect(request.path_info)
    

  context = {
    'single_blog':single_blog,
    'comments': comments,
  }
  return render(request, 'single_page.html',context)

def search(request):
  keyword = request.GET.get('keyword')
  
  find = Blog.objects.filter(Q(title__icontains = keyword)|Q(short_description__icontains = keyword)|Q(blog_body__icontains = keyword), status = 1)
  
  context = {
    'find':find,
    'keyword':keyword,
  }
  return render(request, 'search.html', context)


