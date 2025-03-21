from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post (models.Model):
    author = models.ForeignKey(User , on_delete=models.CASCADE , related_name='his_posts')
    title =  models.CharField(max_length=100 , blank=False , null=False)
    description = models.TextField(blank=False , null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + "\n"+ self.description[0:50]