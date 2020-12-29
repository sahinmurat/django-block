from django.db import models
from django.db.models.fields import TextField

# Create your models here.

class Post(models.Model):
    OPTIONS =(
        ('d', 'Draft')
        ('p', 'Published')
    )
    title = models.CharField(max_length=50)
    content = models,TextField()
    image= models.ImageField()
    # category = models.ForeignKey(Category, on_delete=models.PROTECT)
    publish_date = models.DateTimeField(auto_now_add= True)
    last_updated = models.DateTimeField(auto_now= True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # cascade hepsini siler, protect korur
    status = models.CharField(max_length=10, choices=OPTIONS) 
    # draft published
    slug = models. how-to-learn-django