from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count
from .models import SubRabbles, Posts, Likes, Comments
from .forms import PostForm
from django.shortcuts import redirect, reverse, get_object_or_404

def index(request):
    context = {"welcome": "Hello, world!"}
    subrabbles = SubRabbles.objects.all()
    return render(request, "rabble/index.html", {'subrabbles': subrabbles})

def profile(request):
    return render(request, "rabble/profile.html")

def subrabble_detail(request, rabble_name):
    subrabble = SubRabbles.objects.get(rabble_name=rabble_name)
    posts = Posts.objects.filter(subrabble_id=subrabble.id).annotate(like_count=Count('likes'), comment_count=Count('comments'))
    return render(request, "rabble/subrabble_detail.html", {'subrabble': subrabble, 'posts': posts})

def post_detail(request, rabble_name, pk):
    subrabble = SubRabbles.objects.get(rabble_name=rabble_name)
    post = Posts.objects.get(id=pk)
    likes = Likes.objects.filter(post_id=pk)
    like_count = len(likes)
    comments = Comments.objects.filter(post_id=pk)
    return render(request, "rabble/post_detail.html", {'subrabble': subrabble, \
    'post': post, 'likes': like_count, 'comments': comments, 'comment_count': len(comments)})

def post_create(request, rabble_name):
    subrabble = SubRabbles.objects.get(rabble_name=rabble_name)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = request.user
            post.subrabble_id = subrabble
            post.save()
            return redirect(reverse('subrabble-detail', args=[subrabble.rabble_name]))
    else:
        form = PostForm()
    return render(request, 'rabble/post_form.html', {'form': form, 'subrabble': subrabble})

def post_edit(request, pk, rabble_name):
    subrabble = SubRabbles.objects.get(rabble_name=rabble_name)
    post = get_object_or_404(Posts, id=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = request.user
            post.subrabble_id = subrabble
            post.save()
            return redirect(reverse('subrabble-detail', args=[rabble_name]))
    else:
        form = PostForm(instance=post)
    return render(request, 'rabble/post_form.html', {'form': form, 'subrabble': subrabble})