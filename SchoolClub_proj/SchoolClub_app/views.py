from django.shortcuts import render, redirect, get_object_or_404
from .models import Club, Comment
from django.utils import timezone

# Create your views here.
def home(request):
    clubs = Club.objects.all()
    return render(request, 'home.html', {'clubs':clubs})

def new(request):
    if (request.method == 'POST'):
        post = Club()
        post.name = request.POST['name']
        post.body = request.POST['body']
        post.number = request.POST['number']
        post.save()
        return redirect('home')
    return render(request, 'new.html')
    # 상세페이지로 바꾸기

def detail(request, club_id):
    club_detail = get_object_or_404(Club, pk=club_id)
    comments = Comment.objects.all()
    return render(request, 'detail.html', {'club_detail':club_detail, 'comments':comments})

def delete(request, club_id):
    delete_post = Club.objects.get(id=club_id)
    delete_post.delete()
    return redirect('home')

def edit(request, club_id):
    post = get_object_or_404(Club, pk=club_id)
    if request.method == "POST":
        post.name = request.POST['name']
        post.body = request.POST['body']
        post.number = request.POST['name']
        post.save()
        return redirect('detail', club_id)
    else:
        return render(request, 'edit.html', {'post':post})

def new_comment(request, club_id):
    if (request.method == 'POST'):
        post = Comment()
        post.comment = request.POST['comment']
        post.date = timezone.now()
        post.save()
    return redirect('detail', club_id)