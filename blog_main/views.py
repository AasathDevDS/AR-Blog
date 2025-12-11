from django.shortcuts import render 
from blogs.models import Category,Blog
from about.models import About

def home(request):
  categories = Category.objects.all()
  about = About.objects.all()
  featured_posts = Blog.objects.filter(is_featured = True)
  posts = Blog.objects.filter(is_featured = False)
  context = {
    'categories':categories,
    'about':about,
    'featured_posts':featured_posts,
    'posts':posts,
  }
  return render(request, 'home.html',context)

