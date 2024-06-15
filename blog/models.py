from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from ckeditor.fields import RichTextField

# Create your models here.

    
class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=120)
    like = models.IntegerField(default=0)
    views_count = models.IntegerField(default=0)
    headings = models.CharField(max_length=100)
    content = RichTextField()
    image = models.ImageField(upload_to='blog_images')
    slug = models.CharField(unique=True,blank=True,max_length=200)
    timeStamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title +" by "+self.author
    class   meta:
        ordering = ["views_count"]
    
class BlogComment(models.Model): 
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Blog,on_delete=models.CASCADE) # post = blog manke chlao
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username
    
   
class UserBlog(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=120)
    like = models.IntegerField(default=0)
    views_count = models.IntegerField(default=0)
    headings = models.CharField(max_length=100)
    content = RichTextField()
    image = models.ImageField(upload_to='blog_images')
    timeStamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title +" by "+self.author
    class   meta:
        ordering = ["views_count"]