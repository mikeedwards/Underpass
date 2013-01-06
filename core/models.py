from django.db import models
from django.contrib.auth.models import User

from django_extensions.db.models import TimeStampedModel
from inline_ordering.models import Orderable

# Create your models here.
class Kit(TimeStampedModel):
    title = models.CharField(max_length=500)
    user = models.ForeignKey(User, related_name='kits')

    def __unicode__(self):
        return self.title

class Level(TimeStampedModel, Orderable):
    kit = models.ForeignKey('Kit', related_name='levels')
    title = models.CharField(max_length=500)

    def __unicode__(self):
        return self.title

    def clone(self, user=None):
        if user is None:
            user = self.kit.user

        bridge = Bridge.objects.create(title=self.title,
            level=self,
            user=user)

        for level_post in self.posts.all():
            post = Post.objects.create(post_type=level_post.post_type,
                bridge=bridge)

        for level_plank in self.planks.all():
            plank = Plank.objects.create(post_type=level_plank.post_type,
                body=level_plank.body,
                bridge=bridge)

        return bridge

class Bridge(TimeStampedModel):
    level = models.ForeignKey('Level', related_name='bridges')
    title = models.CharField(max_length=500)
    user = models.ForeignKey(User, related_name='bridges')

    def __unicode__(self):
        return self.title

class PostType(TimeStampedModel):
    title = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    image = models.URLField(null=True, blank=True)

    def __unicode__(self):
        return self.title

class LevelPlank(TimeStampedModel,Orderable):
    level = models.ForeignKey('Level', related_name='planks')
    post_type = models.ForeignKey('PostType', related_name='level_planks')
    body = models.TextField(blank=True)

    def __unicode__(self):
        return self.post_type.title + ' plank'

class LevelPost(TimeStampedModel,Orderable):
    level = models.ForeignKey('Level', related_name='posts')
    post_type = models.ForeignKey('PostType', related_name='level_posts')

    def __unicode__(self):
        return self.post_type.title + ' post'

class Plank(TimeStampedModel,Orderable):
    bridge = models.ForeignKey('Bridge', related_name='planks')
    post_type = models.ForeignKey('PostType', related_name='planks')
    body = models.TextField(blank=True)

    def __unicode__(self):
        return self.post_type.title + ' plank'

class Post(TimeStampedModel,Orderable):
    bridge = models.ForeignKey('Bridge', related_name='posts')
    post_type = models.ForeignKey('PostType', related_name='posts')

    def __unicode__(self):
        return self.post_type.title + ' post'
