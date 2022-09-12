from datetime import datetime
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):

    allposts = Post.objects.get_queryset().filter(status='published')
    return render(request, 'index.html', {'posts' : allposts})

def post_single(request, post):

    if(request.user.username== str(Post.objects.get_queryset().filter(slug=post)[0].author) ):
        
        post = get_object_or_404(Post, slug=post)
        author = str(post.author)
        print(post.author)
        return render(request, 'single.html', {'post':post, 'author':author})
    else:
        
        post = get_object_or_404(Post, slug=post, status='published')
        author = str(post.author)
        print(post.author)
        return render(request, 'single.html', {'post':post, 'author':author})
    

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
            if request.POST['publish']=='NO':
                status = "published"
        except KeyError:
            status = "draft"
        author = request.user

        pp = Post.objects.create(title=title ,content=content, status=status, author=author, slug=slug ,publish=publish)
        
        messages.success(request, ("Register sucessful."))
        print("USPEH")
        return home(request)



