from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Note(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True)
    content = models.TextField(null=True)
    created = models.DateTimeField(null=True)
    updated = models.DateTimeField(null=True)

    def __str__(self):
        return f"Title: {self.title} Content: {self.content} created : {self.created} updated: {self.updated}"