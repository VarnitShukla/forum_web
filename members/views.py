from django.shortcuts import render, get_object_or_404
from .models import Category, Author, Post, Comment, Reply
from .utils import update_views
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def home(request):
    forums = Category.objects.all()
    num_posts = Post.objects.filter(approved=True).count()
    num_users = User.objects.all().count()
    num_categories = forums.count()
    context ={
        "forums": forums,
        "num_posts": num_posts,
        "num_users": num_users,
        "num_categories": num_categories,
        "title" : "Home"
    }
    return render(request, "home.html", context)

def posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(approved=True, categories=category)
    paginator = Paginator(posts, 5)
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        "posts": posts,
        "category": category,
        "title" : category.title,
    }
    return render(request, "posts.html", context)

def details(request, slug):
    post = get_object_or_404(Post, slug=slug)
    author = Author.objects.get(user=request.user)
    if "commentform" in request.POST:
        comment = request.POST.get("comment")
        new_comment, created = Comment.objects.get_or_create(user=author, content=comment)
        post.comments.add(new_comment.id)
        
    if "replyform" in request.POST:
        reply = request.POST.get("reply")
        comment_id = request.POST.get("comment_id")
        comment = Comment.objects.get(id=comment_id)
        new_reply, created = Reply.objects.get_or_create(user=author, content=reply)
        comment.replies.add(new_reply.id)
        
    context = {
        "post": post,
        "title" : post.title,
    }
    update_views(request, post)
    return render(request, "details.html", context)

@login_required
def post_creation(request):
    context = {}
    form = PostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            author = Author.objects.get(user=request.user)
            new_post = form.save(commit=False)
            new_post.user = author
            new_post.save()
            form.save_m2m()
            return redirect("home")
    context.update({
        "form": form,
        "title" : "Create a new post"
    })
    return render(request, "post_creation.html", context)

def searchresult_home(request):
    context = {}
    posts = Post.objects.filter(approved=True)
    if "search_home" in request.GET:
        query = request.GET.get("searchquery_home")
        dropdown = request.GET.get("dropdown_home")
        if dropdown == "Title":
            results = posts.filter(title__icontains=query)
        elif dropdown == "Content":
            results = posts.filter(content__icontains=query)
        else:
            results = posts.filter(title__icontains=query) | posts.filter(content__icontains=query)
        context.update({
            "results": results,
            "query": query,
            "dropdown": dropdown,
            "title" : "Home Search Results"
        })
    return render(request, "searchresult_home.html", context)

def searchresult_posts(request):
    context = {}
    posts = Post.objects.filter(approved=True)
    category = request.GET.get("category")
    if "search_posts" in request.GET:
        query = request.GET.get("searchquery_posts")
        dropdown = request.GET.get("dropdown_posts")
        category = request.GET.get("category")
        if dropdown == "Title":
            results = posts.filter(title__icontains=query)
        elif dropdown == "Content":
            results = posts.filter(content__icontains=query)
        else:
            results = posts.filter(title__icontains=query) | posts.filter(content__icontains=query)
        context.update({
            "results": results,
            "query": query,
            "dropdown": dropdown,
            "category": category,
            "title" : "Posts Search Results"
        })
    return render(request, "searchresult_posts.html", context)