from __future__ import absolute_import
from django.utils.unittest import skipUnless
from django.test import TestCase
from ..models import Organization, Person, ScholarGroup,Scholar,UserDemographics#,ScholarGroupAssociations,
from django.contrib.auth.models import User,Group
from datetime import date
from django.test.utils import override_settings
from django.contrib.auth import get_user_model

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

from mezzanine.conf import settings

__author__ = 'valentin'

#@override_settings(USE_TZ=False,AUTH_PROFILE_MODULE='hs_user_org.Scholar')
@skipUnless("hs_scholar_profile" in settings.INSTALLED_APPS,"hs_scholar_profile must be installed" )
@override_settings(AUTH_PROFILE_MODULE='hs_scholar_profile.Scholar')
class ScholarAndGroupTest(TestCase):
    def setUp(self):
        self.u1 = User.objects.create(username='user1',email='me@example.com')
        self.u1p = self.u1.get_profile()
        self.u1p.uniqueCode="ab"
        self.u1p.givenName="first"
        self.u1p.familyName="last"
        self.u1p.name="First Last"
        self.u1p.jobTitle="job"
        self.u1p.demographics = UserDemographics.objects.create()
        self.u1p.demographics.userType=UserDemographics.USER_TYPES_CHOICES[1]

        self.u1p.save()
        #scholar = Scholar.objects.create(uniqueCode="ab",givenName="first", familyName="last", name="First Last",
        #                                 userType=UserDemographics.USER_TYPES_CHOICES[1],jobTitle="job")

        self.rGroup = ScholarGroup.objects.create(name="ResearchGroup",createdBy=self.u1p)
        #ScholarGroupAssociations.objects.create(scholar=u1p,scholargroup=rGroup, beginDate=date(2013,01,10))
        self.rGroup.user_set.add(self.u1)

    def test_ScholarUser(self):
        rq = Scholar.objects.filter(givenName="first")
        self.assertEqual(rq.count(),1)
        firstOne = rq.first()
        self.assertEqual(firstOne.user.username, 'user1')
        self.assertEqual(firstOne.user.groups.count(), 1)

    def test_ScholarUserHasUser(self):
        s = Scholar.objects.get(id=self.u1p.id)
        self.assertEqual(s.user,self.u1)
        self.assertIsInstance(s,Scholar)
        self.assertIsInstance(s,Person)
        self.assertIsInstance(s.demographics,UserDemographics)
        self.assertEqual(s.user.username, 'user1')
        self.assertEqual(s.user.groups.count(), 1)
        # in the future, this test should use the USER_AUTH_MODEL

    def test_ScholarGroup(self):
        sg = ScholarGroup.objects.get(name="ResearchGroup")
        self.assertEqual(sg,self.rGroup)
        self.assertEqual(sg.createdBy,self.u1p)

    def test_ScholarGroupIsGroup(self):
        g1 = Group.objects.get(name="ResearchGroup")
        self.assertIsInstance(self.rGroup,Group)


    pass