from django.db import models
from django.db.models.fields import TextField
from django.contrib.auth.models import User

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
    image= models.ImageField()
    # category = models.ForeignKey(Category, on_delete=models.PROTECT)
    publish_date = models.DateTimeField(auto_now_add= True)
    last_updated = models.DateTimeField(auto_now= True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    # cascade hepsini siler, protect korur
    status = models.CharField(max_length=10, choices=OPTIONS, default='d') 
    
    slug = models.SlugField(blank=True, unique=True) 
    
#     git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/sahinmurat/django-block.git
# git push -u origin main
                