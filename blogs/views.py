from django.db import reset_queries
import blogs
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.core.paginator import Paginator
from .models import BlogPost
from .forms import BlogForm

def check_post_owner(request, post):
    """Checks if the requesting user is the post owner"""
    if post.owner != request.user:
        raise Http404

def index(request):
    """Home page listing the blogs in chronological order."""
    blogs = BlogPost.objects.all().order_by('-date_added')
    paginator = Paginator(blogs, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'blogs': page_obj}
    return render(request, 'blogs/index.html', context)

def blog_post(request, post_id):
    """Displays individual blog post."""
    blog = BlogPost.objects.get(id=post_id)
    context = {'blog': blog}
    return render(request, 'blogs/blog_post.html', context)

@login_required
def new_post(request):
    """Create a new blog post."""
    if request.method != 'POST':
        # No form has been submitted, create a new one.
        form = BlogForm()
    else:
        # Data submitted, process and save if valid
        form = BlogForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('blogs:index')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, blog_id):
    """Edit a blog post."""
    post = BlogPost.objects.get(id=blog_id)
    text = post.text
    title = post.title
    check_post_owner(request, post)

    if request.method != 'POST':
        # Pre-fill with what is saved in the database
        form = BlogForm(instance=post)
    else:
        # Data submitted, validate
        form = BlogForm(instance= post, data= request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog_post', post_id=post.id)

    # Show a new edit entry form, or an invalidated form
    context = {'title': title, 'text': text, 'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)
