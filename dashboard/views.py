from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from blogs.models import Category,Blog
from .forms import CategoryForm,BlogForm
from django.template.defaultfilters  import slugify

@login_required(login_url='login')
def dashboard(request):
  category_count = Category.objects.all().count()
  blogs_count = Blog.objects.all().count()
  context = {
    'category_count':category_count,
    'blogs_count':blogs_count,
  } 
  return render(request, 'dashboard/dashboard.html',context)

def category(request):
  return render(request, 'dashboard/category.html')

def add_category(request):
  if request.method == "POST":
    form = CategoryForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('category')
  else:
    form = CategoryForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_category.html', context)
    
def edit_category(request,pk):
  category = get_object_or_404(Category, pk=pk)
  if request.method == "POST":
    form = CategoryForm(request.POST, instance=category)
    if form.is_valid():
      form.save()
      return redirect('category')
  form = CategoryForm(instance=category)
  context = {
    'form':form,
    'category':category,
  }
  return render(request, 'dashboard/edit_category.html',context)

def delete_category(request,pk):
  category = get_object_or_404(Category, pk = pk)
  category.delete()
  return redirect('category')

def posts(request):
  posts = Blog.objects.all()
  context = {
    'posts': posts,
  }
  return render(request, 'dashboard/posts.html', context)

def add_post(request):
  if request.method == "POST":
    form = BlogForm(request.POST, request.FILES)
    if form.is_valid():
      post = form.save(commit = False)
      post.author = request.user
      title = form.cleaned_data['title']
      post.slug = slugify(title)
      post.save()
      return redirect('posts')
  form = BlogForm()
  context = {
    'form': form,
  }
  return render(request, 'dashboard/add_post.html', context)


def edit_post(request, pk):
  blog = get_object_or_404(Blog, pk = pk )
  if request.method == "POST":
    form = BlogForm(request.POST,request.FILES, instance=blog)
    if form.is_valid():
      post = form.save(commit = False)
      post.author = request.user
      title = form.cleaned_data['title']
      post.slug = slugify(title)
      post.save()
      return redirect('posts')
  form = BlogForm(instance=blog)
  context = {
    'form':form,
    'blog': blog,
  }
  return render(request, 'dashboard/edit_post.html', context)

def delete_post(request,pk):
  blog = get_object_or_404(Blog, pk = pk)
  blog.delete()
  return redirect('posts')