from django.test import TestCase
from django.contrib.auth import get_user_model
#from django_webtest import WebTest
from hs.hs_user_org.models import Organization, Person, OtherNames



__author__ = 'valentin'


class PersonTest(TestCase):
    def setUp(self):
        Person.objects.create(firstName="first", lastName="last", name="First Last")

    def test_Person(self):
        org1 = Person.objects.get(lastName="last")
        self.assertEqual(org1.otherName.count(), 0)


pass