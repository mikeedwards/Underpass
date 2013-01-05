"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase, Client
from django.contrib.auth.models import User
from tastypie.test import ResourceTestCase

from core import api
from core.models import Bridge, PostType, Post, Plank

class ApiTest(ResourceTestCase):
    def setUp(self):
        super(ApiTest, self).setUp()

        self.user = User.objects.create(username='admin', 
            email='test@example.com')

        self.bridge = Bridge.objects.create(title="test bridge",
            user=self.user)

        self.post_type = PostType.objects.create(title="test type")

        self.post = Post.objects.create(post_type=self.post_type,
            bridge=self.bridge)

        self.plank = Plank.objects.create(body="test plank",
            post_type=self.post_type,
            bridge=self.bridge)

    def test_user_resource_exists(self):
        """
        Tests that user resource exists.
        """
        resource = api.UserResource()
        self.assertIsInstance(resource, api.UserResource)

    def test_user_resource_path(self):
        """
        Tests that user resource detail path is valid.
        """
        pk = self.user.pk
        response = self.api_client.get('/api/v1/user/{0}/'.format(pk),
            format='json')
        self.assertValidJSONResponse(response)

    def test_user_resource_fields(self):
        """
        Tests that user resource detail path is valid.
        """
        pk = self.user.pk
        response = self.api_client.get('/api/v1/user/{0}/'.format(pk),
            format='json')

        self.assertKeys(self.deserialize(response), 
            ['id', 'username', 'email', 'first_name', 'last_name', 'resource_uri'])

    def test_bridge_resource_exists(self):
        """
        Tests that bridge resource exists.
        """
        resource = api.BridgeResource()
        self.assertIsInstance(resource, api.BridgeResource)

    def test_bridge_resource_path(self):
        """
        Tests that bridge resource detail path is valid.
        """
        pk = self.bridge.pk
        response = self.api_client.get('/api/v1/bridge/{0}/'.format(pk),
            format='json')
        self.assertValidJSONResponse(response)

    def test_bridge_resource_fields(self):
        """
        Tests that bridge resource fields are valid.
        """
        pk = self.bridge.pk
        response = self.api_client.get('/api/v1/bridge/{0}/'.format(pk),
            format='json')

        self.assertKeys(self.deserialize(response), 
            ['id', 'title', 'planks', 'posts', 'user', 'resource_uri'])

    def test_post_type_resource_exists(self):
        """
        Tests that post_type resource exists.
        """
        resource = api.PostTypeResource()
        self.assertIsInstance(resource, api.PostTypeResource)

    def test_post_type_resource_path(self):
        """
        Tests that post_type resource detail path is valid.
        """
        pk = self.post_type.pk
        response = self.api_client.get('/api/v1/post_type/{0}/'.format(pk),
            format='json')
        self.assertValidJSONResponse(response)

    def test_post_type_resource_fields(self):
        """
        Tests that post_type resource fields are valid.
        """
        pk = self.post_type.pk
        response = self.api_client.get('/api/v1/post_type/{0}/'.format(pk),
            format='json')

        self.assertKeys(self.deserialize(response), 
            ['id', 'title', 'description', 'resource_uri'])

    def test_post_resource_exists(self):
        """
        Tests that post resource exists.
        """
        resource = api.PostResource()
        self.assertIsInstance(resource, api.PostResource)

    def test_post_resource_path(self):
        """
        Tests that post resource detail path is valid.
        """
        pk = self.post.pk
        response = self.api_client.get('/api/v1/post/{0}/'.format(pk),
            format='json')
        self.assertValidJSONResponse(response)

    def test_post_resource_fields(self):
        """
        Tests that post resource fields are valid.
        """
        pk = self.post.pk
        response = self.api_client.get('/api/v1/post/{0}/'.format(pk),
            format='json')

        self.assertKeys(self.deserialize(response), 
            ['id', 'post_type', 'bridge', 'resource_uri'])

    def test_plank_resource_exists(self):
        """
        Tests that plank resource exists.
        """
        resource = api.PlankResource()
        self.assertIsInstance(resource, api.PlankResource)

    def test_plank_resource_path(self):
        """
        Tests that plank resource detail path is valid.
        """
        pk = self.plank.pk
        response = self.api_client.get('/api/v1/plank/{0}/'.format(pk),
            format='json')
        self.assertValidJSONResponse(response)

    def test_plank_resource_fields(self):
        """
        Tests that plank resource fields are valid.
        """
        pk = self.plank.pk
        response = self.api_client.get('/api/v1/plank/{0}/'.format(pk),
            format='json')

        self.assertKeys(self.deserialize(response), 
            ['id', 'body', 'post_type', 'bridge', 'resource_uri'])
