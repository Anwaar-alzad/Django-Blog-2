from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length = 150)
    subtitle = models.CharField(max_length = 350)
    content = models.CharField(max_length = 250)
    image = models.ImageField(upload_to="images/")
    published_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.title