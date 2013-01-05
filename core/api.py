from django.contrib.auth.models import User

from tastypie import fields
from tastypie.resources import ModelResource

from core.models import Bridge, PostType, Post, Plank


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class PostTypeResource(ModelResource):
    class Meta:
        queryset = PostType.objects.all()
        resource_name = 'post_type'
        fields = ['id', 'title', 'description']

class PostResource(ModelResource):
    bridge = fields.ForeignKey('core.api.BridgeResource', 'bridge')
    post_type = fields.ForeignKey(PostTypeResource, 'post_type', full=True)

    class Meta:
        queryset = Post.objects.all()
        resource_name = 'post'
        fields = ['id',]

class PlankResource(ModelResource):
    bridge = fields.ForeignKey('core.api.BridgeResource', 'bridge')
    post_type = fields.ForeignKey(PostTypeResource, 'post_type')

    class Meta:
        queryset = Plank.objects.all()
        resource_name = 'plank'
        fields = ['id', 'body']

class BridgeResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')
    posts = fields.ToManyField(PostResource, 'posts', null=True, full=True, related_name='bridge')
    planks = fields.ToManyField(PlankResource, 'planks', null=True, full=True, related_name='bridge')

    class Meta:
        queryset = Bridge.objects.all()
        resource_name = 'bridge'
        fields = ['id', 'title', 'planks', 'posts', 'user']

