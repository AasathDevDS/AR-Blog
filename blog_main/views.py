from django.shortcuts import redirect, render 
from blogs.models import Category,Blog
from about.models import About
from .forms import Registrationform
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

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
  return render(request,'home.html',context)

def register(request):
  if request.method == 'POST':
    form = Registrationform(request.POST)
    if form.is_valid():
      form.save()
      return redirect('home')
    else:
      print(form.errors)   
  else:
    form = Registrationform()
  context = {
    'form':form,
  }
  return render(request, 'register.html',context)

def login(request):
  if request.method == "POST":
    form = AuthenticationForm(request, request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = auth.authenticate(username=username,password=password)
      if user is not None:
        auth.login(request, user)
        return redirect('dashboard')
  form = AuthenticationForm()
  context = {
    'form':form
  }
  return render(request,'login.html',context)

def logout(request):
  auth.logout(request)
  return redirect('home')