from email.mime import image
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django_resized import ResizedImageField

# Create your models here.

class Post(models.Model):

    options=(
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    content = models.TextField()
    status = models.CharField(max_length=10, choices=options, default='draft')
    image = ResizedImageField(null=True, blank=True, upload_to="images")

    class Meta:
        ordering = ('-publish',)


    def __str__(self):
        return self.title
    @classmethod
    def create(self, title, content, status, author, slug ,publish, image):
        post = Post.objects.create(title=title, content=content, status=status, author=author, slug=slug, publish=publish, image=image)
        return post
