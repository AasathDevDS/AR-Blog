from django.shortcuts import render,get_object_or_404
from .models import Blog,Category

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
  context = {
    'single_blog':single_blog
  }
  return render(request, 'single_page.html',context)