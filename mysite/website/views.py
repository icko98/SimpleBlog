from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib.auth.models import User
from django.contrib import messages
from PIL import Image

# Create your views here.
def home(request):

    allposts = Post.objects.get_queryset().filter(status='published')
    return render(request, 'index.html', {'posts' : allposts})

def post_single(request, post):
    print(Post.objects.get_queryset().filter(id=post)[0].id)
    if(request.user.username== str(Post.objects.get_queryset().filter(id=post)[0].author) ):
        
        post = get_object_or_404(Post, id=post)
        author = str(post.author)
        #print(post.author)
        return render(request, 'single.html', {'post':post, 'author':author})
    else:
        
        post = get_object_or_404(Post, id=post, status='published')
        author = str(post.author)
        print(post.author)
        return render(request, 'single.html', {'post':post, 'author':author})


def editpost(request, post):
    pp = get_object_or_404(Post, id=post)
    if request.method=="GET":
        return render(request, 'editpost.html', {'post': pp})
    elif request.method=="POST":
        pp.content = request.POST['body']
        pp.title = request.POST['title']
        pp.image = request.FILES['image']
        try:
            if request.POST['publish']=='NO':
                pp.status = "published"
        except KeyError:
            pp.status = "draft"
        pp.save()
        return redirect('http://127.0.0.1:8000/post/' + str(post))

def author_blog(request, author):
    usr = User.objects.get_queryset().filter(username=author)
    allposts = Post.objects.get_queryset().filter(author=usr[0].id)
    filposts = allposts.filter(status='published')
    return render(request, 'author.html', {'posts': allposts, 'author': author, 'filposts':filposts})
    
def newpost(request):
    if request.method=="GET":
        return render(request, 'newpost.html')
    else:
        title= request.POST['title']
        content= request.POST['body']
        slug = title[0:5]
        publish = datetime.now()
        try: 
            if request.FILES['image']:
                image = request.FILES['image']
        except KeyError:
            image=None
        try:
            if request.POST['publish']=='NO':
                status = "published"
        except KeyError:
            status = "draft"
        author = request.user

        pp = Post.create(title=title ,content=content, status=status, author=author, slug=slug ,publish=publish, image=image)
        pp.save()
        
        messages.success(request, ("Register sucessful."))
        return redirect('http://127.0.0.1:8000/')



