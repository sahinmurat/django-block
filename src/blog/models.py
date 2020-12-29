from django.db import models
from django.db.models.fields import TextField
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    return 'blog/{0}/{1}'.format(instance.author.id, filename)

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

class Post(models.Model):
    OPTIONS =(
        ('d', 'Draft'),
        ('p', 'Published')
    )
    title = models.CharField(max_length=50)
    content = models,TextField()
    image= models.ImageField(upload_to = user_directory_path)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    publish_date = models.DateTimeField(auto_now_add= True)
    last_updated = models.DateTimeField(auto_now= True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # cascade hepsini siler, protect korur
    status = models.CharField(max_length=10, choices=OPTIONS, default='d') 
    
    slug = models.SlugField(blank=True, unique=True) 
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add= True)
    content = models.TextField()
    
    def __str__(self):
        return self.user.username
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.user.username

class PostView(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add= True)
    
    def __str__(self):
        return self.user.username
      
      

    
 