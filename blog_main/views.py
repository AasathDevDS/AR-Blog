from django.shortcuts import redirect, render 
from blogs.models import Category,Blog
from about.models import About
from .forms import Registrationform
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

def register(request):
  if request.method == 'POST':
    form = Registrationform(request.POST)
    if form.is_valid():
      form.save()
      return redirect('register')
    else:
      print(form.errors)   
  else:
    form = Registrationform()
  context = {
    'form':form,
  }
  return render(request, 'register.html',context)