from django.conf.urls import patterns, include, url
from django.contrib import admin

from tastypie.api import Api

from core.api import UserResource, BridgeResource, PostTypeResource, \
    PostResource, PlankResource

admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(BridgeResource())
v1_api.register(PostTypeResource())
v1_api.register(PostResource())
v1_api.register(PlankResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Underpass.views.home', name='home'),
    # url(r'^Underpass/', include('Underpass.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
)
