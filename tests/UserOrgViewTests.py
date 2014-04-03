from __future__ import absolute_import
from django.test import TestCase
from django.utils.unittest import skipUnless
from django.core.urlresolvers import reverse,resolve,reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User,Group
#from django_webtest import WebTest
from ..models import Organization, Person,OrgAssociations, ExternalOrgIdentifiers,ScholarGroup
from datetime import date


try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

from mezzanine.conf import settings

__author__ = 'valentin'

@skipUnless("hs.hs_user_org" in settings.INSTALLED_APPS,"hs_user_org must be installed" )
class UserOrgViewTests(TestCase):

    def setUp(self):
        self.aPerson = Person.objects.create(givenName="last", familyName="first", name="last first")
        self.org2 = Organization.objects.create(name="org2")
        self.u1 = User.objects.create(username='user1',email='me@example.com')
        self.u1p = self.u1.get_profile()
        self.u1p.uniqueCode="ab"
        self.u1p.givenName="first"
        self.u1p.familyName="last"
        self.u1p.name="First Last"
        self.u1p.jobTitle="job"


        self.u1p.save()
        #scholar = Scholar.objects.create(uniqueCode="ab",givenName="first", familyName="last", name="First Last",
        #                                 userType=UserDemographics.USER_TYPES_CHOICES[1],jobTitle="job")

        self.rGroup = ScholarGroup.objects.create(name="ResearchGroup",createdBy=self.u1p)
        #ScholarGroupAssociations.objects.create(scholar=u1p,scholargroup=rGroup, beginDate=date(2013,01,10))
        self.rGroup.user_set.add(self.u1)

    def test_list_views(self):
        response = self.client.get(reverse("PersonList"))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("OrganizationList"))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("ScholarGroupList"))
        self.assertEqual(response.status_code, 200)

    def test_detail_views(self):
        response = self.client.get(reverse("PersonDetail", args=[ self.aPerson.id] ) )
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("OrganizationDetail", args=[  self.org2.id] ) )
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("ScholarGroupDetail", args=[  self.rGroup.id] ) )
        self.assertEqual(response.status_code, 200)

# tried:  resolve....)
    # people, /people, /people/
    # party/people, /party/people
    # hs_user_org:people
    # def test_urls(self):
    #     response = self.client.get(resolve('hs_user_org:people'))
    #     self.assertEqual(response.status_code, 200)
