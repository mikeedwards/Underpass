"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase, Client
from django.contrib.auth.models import User
from tastypie.test import ResourceTestCase

from core import api
from core.models import Kit, Level, Bridge, PostType, LevelPost, LevelPlank, \
    Post, Plank

class ModelsTest(TestCase):
    def setUp(self):
        super(ModelsTest, self).setUp()
        
        self.user = User.objects.create(username='admin', 
            email='test@example.com')

        self.kit = Kit.objects.create(title="test kit",
            user=self.user)

        self.level = Level.objects.create(title="test level",
            kit=self.kit)

        self.bridge = Bridge.objects.create(title="test bridge",
            user=self.user,
            level=self.level)

        self.post_type = PostType.objects.create(title="test type")

        self.level_post = LevelPost.objects.create(post_type=self.post_type,
            level=self.level)

        self.level_plank = LevelPlank.objects.create(body="test plank",
            post_type=self.post_type,
            level=self.level)

        self.post = Post.objects.create(post_type=self.post_type,
            bridge=self.bridge)

        self.plank = Plank.objects.create(body="test plank",
            post_type=self.post_type,
            bridge=self.bridge)

    def test_kit_model_defaults(self):
        self.assertEqual(unicode(self.kit), u'test kit')

    def test_kit_clones_self(self):
        """
        Tests that a kit can clone itself
        """

    def test_level_model_defaults(self):
        self.assertEqual(unicode(self.level), u'test level')

    def test_level_clones_bridge(self):
        """
        Tests that a level can clone itself as a bridge
        """
        bridge = self.level.clone()
        self.assertEqual(bridge.title, self.level.title)
        self.assertEqual(bridge.posts.all()[0].post_type,
            bridge.posts.all()[0].post_type)
        self.assertEqual(bridge.planks.all()[0].post_type,
            bridge.planks.all()[0].post_type)
        self.assertEqual(bridge.planks.all()[0].body,
            bridge.planks.all()[0].body)
        self.assertEqual(bridge.planks.all()[0].body,
            bridge.planks.all()[0].body)
        self.assertEqual(bridge.user,
            self.level.kit.user)

    def test_level_clones_bridge_with_new_user(self):
        """
        Tests that a level can clone itself as a bridge,
        but add a new user.
        """
        user = User.objects.create(username='student', 
            email='student@example.com')
        bridge = self.level.clone(user)
        self.assertEqual(bridge.user, user)

    def test_bridge_model_defaults(self):
        self.assertEqual(unicode(self.bridge), u'test bridge')

    def test_post_type_model_defaults(self):
        self.assertEqual(unicode(self.post_type), u'test type')

    def test_level_post_model_defaults(self):
        self.assertEqual(unicode(self.level_post), u'test type post')

    def test_level_plank_model_defaults(self):
        self.assertEqual(unicode(self.level_plank), u'test type plank')

    def test_post_model_defaults(self):
        self.assertEqual(unicode(self.post), u'test type post')

    def test_plank_model_defaults(self):
        self.assertEqual(unicode(self.plank), u'test type plank')

class ApiTest(ResourceTestCase):
    def setUp(self):
        super(ApiTest, self).setUp()

        self.user = User.objects.create(username='admin', 
            email='test@example.com')

        self.kit = Kit.objects.create(title="test kit",
            user=self.user)

        self.level = Level.objects.create(title="test level",
            kit=self.kit)

        self.bridge = Bridge.objects.create(title="test bridge",
            user=self.user,
            level=self.level)

        self.post_type = PostType.objects.create(title="test type")

        self.level_post = LevelPost.objects.create(post_type=self.post_type,
            level=self.level)

        self.level_plank = LevelPlank.objects.create(body="test plank",
            post_type=self.post_type,
            level=self.level)

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
            ['id', 'username', 'first_name', 'last_name', 'resource_uri'])

    def test_kit_resource_exists(self):
        """
        Tests that kit resource exists.
        """
        resource = api.KitResource()
        self.assertIsInstance(resource, api.KitResource)

    def test_kit_resource_path(self):
        """
        Tests that kit resource detail path is valid.
        """
        pk = self.kit.pk
        response = self.api_client.get('/api/v1/kit/{0}/'.format(pk),
            format='json')
        self.assertValidJSONResponse(response)

    def test_kit_resource_fields(self):
        """
        Tests that kit resource fields are valid.
        """
        pk = self.kit.pk
        response = self.api_client.get('/api/v1/kit/{0}/'.format(pk),
            format='json')

        self.assertKeys(self.deserialize(response), 
            ['id', 'levels', 'title', 'user', 'resource_uri'])

    def test_level_resource_exists(self):
        """
        Tests that level resource exists.
        """
        resource = api.LevelResource()
        self.assertIsInstance(resource, api.LevelResource)

    def test_level_resource_path(self):
        """
        Tests that level resource detail path is valid.
        """
        pk = self.level.pk
        response = self.api_client.get('/api/v1/level/{0}/'.format(pk),
            format='json')
        self.assertValidJSONResponse(response)

    def test_level_resource_fields(self):
        """
        Tests that level resource fields are valid.
        """
        pk = self.level.pk
        response = self.api_client.get('/api/v1/level/{0}/'.format(pk),
            format='json')

        self.assertKeys(self.deserialize(response), 
            ['id', 'title', 'kit', 'planks', 'posts', 'resource_uri'])

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
            ['id', 'title', 'level', 'planks', 'posts', 'user', 'resource_uri'])

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

    def test_level_post_resource_exists(self):
        """
        Tests that level_post resource exists.
        """
        resource = api.LevelPostResource()
        self.assertIsInstance(resource, api.LevelPostResource)

    def test_level_post_resource_path(self):
        """
        Tests that level_post resource detail path is valid.
        """
        pk = self.level_post.pk
        response = self.api_client.get('/api/v1/level_post/{0}/'.format(pk),
            format='json')
        self.assertValidJSONResponse(response)

    def test_level_post_resource_fields(self):
        """
        Tests that level_post resource fields are valid.
        """
        pk = self.level_post.pk
        response = self.api_client.get('/api/v1/level_post/{0}/'.format(pk),
            format='json')

        self.assertKeys(self.deserialize(response), 
            ['id', 'post_type', 'level', 'resource_uri'])

    def test_level_plank_resource_exists(self):
        """
        Tests that level_plank resource exists.
        """
        resource = api.LevelPlankResource()
        self.assertIsInstance(resource, api.LevelPlankResource)

    def test_level_plank_resource_path(self):
        """
        Tests that level_plank resource detail path is valid.
        """
        pk = self.level_plank.pk
        response = self.api_client.get('/api/v1/level_plank/{0}/'.format(pk),
            format='json')
        self.assertValidJSONResponse(response)

    def test_level_plank_resource_fields(self):
        """
        Tests that level_plank resource fields are valid.
        """
        pk = self.level_plank.pk
        response = self.api_client.get('/api/v1/level_plank/{0}/'.format(pk),
            format='json')

        self.assertKeys(self.deserialize(response), 
            ['id', 'body', 'post_type', 'level', 'resource_uri'])

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
