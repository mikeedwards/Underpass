from django.contrib.auth.models import User

from tastypie import fields
from tastypie.resources import ModelResource

from core.models import Kit, Level, Bridge, PostType, LevelPost, LevelPlank, \
    Post, Plank


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        fields = ['id', 'username', 'first_name', 'last_name']

class PostTypeResource(ModelResource):
    class Meta:
        queryset = PostType.objects.all()
        resource_name = 'post_type'
        fields = ['id', 'title', 'description']

class LevelPostResource(ModelResource):
    level = fields.ForeignKey('core.api.LevelResource', 'level')
    post_type = fields.ForeignKey(PostTypeResource, 'post_type', full=True)

    class Meta:
        queryset = LevelPost.objects.all()
        resource_name = 'level_post'
        fields = ['id', 'lane']

class LevelPlankResource(ModelResource):
    level = fields.ForeignKey('core.api.LevelResource', 'level')
    post_type = fields.ForeignKey(PostTypeResource, 'post_type')

    class Meta:
        queryset = LevelPlank.objects.all()
        resource_name = 'level_plank'
        fields = ['id', 'lane', 'body']

class PostResource(ModelResource):
    bridge = fields.ForeignKey('core.api.BridgeResource', 'bridge')
    post_type = fields.ForeignKey(PostTypeResource, 'post_type', full=True)

    class Meta:
        queryset = Post.objects.all()
        resource_name = 'post'
        fields = ['id', 'lane']

class PlankResource(ModelResource):
    bridge = fields.ForeignKey('core.api.BridgeResource', 'bridge')
    post_type = fields.ForeignKey(PostTypeResource, 'post_type')

    class Meta:
        queryset = Plank.objects.all()
        resource_name = 'plank'
        fields = ['id', 'lane', 'body']

class KitResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')
    levels = fields.ToManyField('core.api.LevelResource', 'levels', null=True, full=True, related_name='kit')

    class Meta:
        queryset = Kit.objects.all()
        resource_name = 'kit'
        fields = ['id', 'title']

class LevelResource(ModelResource):
    kit = fields.ForeignKey(KitResource, 'kit')
    posts = fields.ToManyField(LevelPostResource, 'posts', null=True, full=True, related_name='level')
    planks = fields.ToManyField(LevelPlankResource, 'planks', null=True, full=True, related_name='level')

    class Meta:
        queryset = Level.objects.all()
        resource_name = 'level'
        fields = ['id', 'title']

class BridgeResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')
    level = fields.ForeignKey(LevelResource, 'level')
    posts = fields.ToManyField(PostResource, 'posts', null=True, full=True, related_name='bridge')
    planks = fields.ToManyField(PlankResource, 'planks', null=True, full=True, related_name='bridge')

    class Meta:
        queryset = Bridge.objects.all()
        resource_name = 'bridge'
        fields = ['id', 'title']


