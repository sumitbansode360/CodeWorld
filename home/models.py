from django.db import models
from blog.models import Blog
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name +" "+self.email
    