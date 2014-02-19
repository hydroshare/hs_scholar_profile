from django.test import TestCase
from django.contrib.auth import get_user_model
#from django_webtest import WebTest
from hs.hs_user_org.models import Organization, Person, OtherNames



__author__ = 'valentin'


class PersonTest(TestCase):
    def setUp(self):

        Person.objects.create(givenName="first", familyName="last", name="First Last")
        aPerson = Person.objects.create(givenName="last", familyName="first", name="last first")
        OtherNames.objects.create(persons=aPerson, otherName="abcd", annotation="other")
        OtherNames.objects.create(persons=aPerson, otherName="def", annotation="other")

    def test_Person(self):
        person1 = Person.objects.get(familyName="last")

        self.assertEqual(person1.otherNames.count(), 0)

        person2 = Person.objects.get(familyName="first")
        self.assertEqual(person2.otherNames.count(),2)
        self.assertEquals(person2.otherNames.get(otherName='def').annotation, 'other')




pass