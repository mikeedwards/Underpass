from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bridge(models.Model):
    title = models.CharField(max_length=500)
    user = models.ForeignKey(User, related_name='bridges')

class PostType(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    image = models.URLField(null=True, blank=True)

class Plank(models.Model):
    bridge = models.ForeignKey('Bridge', related_name='planks')
    post_type = models.ForeignKey('PostType', related_name='planks')
    body = models.TextField(blank=True)

class Post(models.Model):
    bridge = models.ForeignKey('Bridge', related_name='posts')
    post_type = models.ForeignKey('PostType', related_name='posts')
