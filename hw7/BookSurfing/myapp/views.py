from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from .models import Blog, Comment
from .forms import CommentForm

# Create your views here.
def home(request):
    posts = Blog.objects.filter().order_by('-date')
    return render(request, 'home.html', {'posts':posts})

def new(request):
    return render(request, 'new.html')

def create(request):
    if (request.method == 'POST' or request.method == 'FILES'):
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.photo = request.FILES['upload']
        post.date = timezone.now()
        post.author = request.user
        post.save()
    return redirect('home')

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    comment_form = CommentForm()
    return render(request, 'detail.html', {'blog_detail':blog_detail, 'comment_form':comment_form})

def new_comment(request, blog_id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.author = request.user
        finished_form.post = get_object_or_404(Blog, pk=blog_id)
        finished_form.save()
    return redirect('detail', blog_id)

def page_not_found(request, exception):
    return render(request, '404.html')

def delete(request, blog_id):
    delete_post = Blog.objects.get(id=blog_id)
    delete_post.delete()
    return redirect('home')

def edit(request, blog_id):
    post = get_object_or_404(Blog, pk=blog_id)
    if request.method == "POST":
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.photo = request.FILES['upload']
        post.date = timezone.now()
        post.author = request.user
        post.save()
        return redirect('detail', blog_id)
    else:
        return render(request, 'form_edit.html', {'post':post})

def delete_comment(request, comment_id):
    delete_comment = Comment.objects.get(id=comment_id)
    blog_id = delete_comment.post.id
    delete_comment.delete()
    return redirect('detail', blog_id)