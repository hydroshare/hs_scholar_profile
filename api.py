from tastypie.api import Api
from tastypie.fields import ForeignKey, ManyToManyField
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authentication import SessionAuthentication
from tastypie.authorization import Authorization

from . import models
from mezzanine.pages.models import Page
from django.contrib.auth import models as auth
from django.conf.urls import url

class ScholarGroup(ModelResource):
    class Meta:
        authorization = Authorization()
        authentication = SessionAuthentication()
        allowed_methods = ['get']
        queryset = models.ScholarGroup.objects.all()
        resource_name = "scholargroup"


class Scholar(ModelResource):
    class Meta:
        authorization = Authorization()
        authentication = SessionAuthentication()
        allowed_methods = ['get']
        queryset = models.Scholar.objects.all()
        resource_name = "scholar"

class Organization(ModelResource):
    class Meta:
        queryset = models.Organization.objects.all()
        resource_name = 'organization'
        allowed_methods = ['get']
        detail_uri_name = "slug"

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/(?P<slug>[\w\d_.-]+)/$" % self._meta.resource_name, self.wrap_view('dispatch_detail'), name="api_dispatch_detail"),
        ]

class Person(ModelResource):
    class Meta:
        queryset = models.Person.objects.all()
        resource_name = 'person'
        allowed_methods = ['get']
        detail_uri_name = "slug"

    # def prepend_urls(self):
    #     return [
    #         url(r"^(?P<resource_name>%s)/(?P<slug>[\w\d_.-]+)/$" % self._meta.resource_name, self.wrap_view('dispatch_detail'), name="api_dispatch_detail"),
    #     ]

resources = Api()
resources.register(Scholar())
resources.register(ScholarGroup())
resources.register(Organization())
resources.register(Person())
