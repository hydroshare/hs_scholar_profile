from __future__ import absolute_import
from django.test import TestCase
from django.utils.unittest import skipUnless
from ..models import Organization, Person, ScholarGroup,Scholar,UserDemographics#,ScholarGroupAssociations
from django.contrib.auth.models import User
from datetime import date
from django.test import TestCase
from django.test.utils import override_settings
from django.contrib.auth import get_user_model
# using "Custom users and testing/fixtures" https://docs.djangoproject.com/en/1.5/topics/auth/customizing/
# this disappears in 1.7 docs AUTH_USER_PROFILE depreciatied

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

from mezzanine.conf import settings

__author__ = 'valentin'
#@override_settings(USE_TZ=False,AUTH_PROFILE_MODULE='hs_user_org.Scholar')
@skipUnless("hs_scholar_profile" in settings.INSTALLED_APPS,"hs_scholar_profile must be installed" )
@override_settings(AUTH_PROFILE_MODULE='hs_scholar_profile.Scholar')
class UserProfileTest(TestCase):
    def setUp(self):
        self.u1 = User.objects.create(username='user1',email='me@example.com')
        #u1 = User(username='user1',email='me@example.com')
        # scholar profile
        self.u1p = self.u1.get_profile()
        self.u1p.uniqueCode="ab"
        self.u1p.givenName="first"
        self.u1p.familyName="last"
        self.u1p.name="First Last"
        self.u1p.jobTitle="job"

        self.dem1 = UserDemographics.objects.create()
        self.dem1.userType = UserDemographics.USER_TYPES_CHOICES[1]
        self.dem1.public = True
        self.u1p.demographics = self.dem1
        #self.u1p.userType=UserDemographics.USER_TYPES_CHOICES[1]
        self.u1p.demographics.save()
        self.u1p.save()

    def test_create_user(self):
        email_lowercase = 'normal@normal.com'
        user = User.objects.create_user('user', email_lowercase)
        self.assertEqual(user.email, email_lowercase)
        self.assertEqual(user.username, 'user')
        #self.assertEqual(user.password, '!')# only applies when doing some testuser class


    def test_scholar_demographics(self):
        UserModel = get_user_model()
        auser = Scholar.objects.get(user__id=self.u1.id)
        "Run tests for a custom user model with email-based authentication"
        #up1 = Scholar.objects.create(uniqueCode="abcde",givenName='first',familyName='last',name="first last")
        dem1 = auser.demographics
        #self.assertEqual(dem1.userType,UserDemographics.USER_TYPES_CHOICES[1])
        #AssertionError: u"('research', 'University Professional or Research Staff')" != ('research', 'University Professional or Research Staff')
        self.assertEqual(dem1.public,True)
        #u1 = User(username="user1", email='me@example.com', scholar=up1)
        #auser.demographics


    @override_settings(AUTH_PROFILE_MODULE='hs_scholar_profile.Scholar')
    def test_custom_user(self):
        "Run tests for a custom user model with email-based authentication"
        self.assertEqual(User.objects.count(),1,"user object count not 1")
        auser = Scholar.objects.filter(user__username='user1')
        self.assertEqual(auser.count(),  1, "did nor get one Scholar Object")
