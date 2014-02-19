from django.test import TestCase
from django.contrib.auth import get_user_model
#from django_webtest import WebTest
from hs.hs_user_org.models import Organization, Person,Associations, ExternalOrgIdentifiers
from datetime import date



__author__ = 'valentin'


class organizationTest(TestCase):
    def setUp(self):
        p1 = Person.objects.create(givenName="first", familyName="last", name="First Last")
        p2 = Person.objects.create(givenName="last", familyName="first", name="last first")
        Organization.objects.create(name="org1")
        org2 = Organization.objects.create(name="org2")
        Associations.objects.create(person=p1,organization=org2,beginDate=date(01,01,2013))
        Associations.objects.create(person=p2,organization=org2,beginDate=date(01,01,2014))
        org3 = Organization.objects.create(name="org3")
        Associations.objects.create(person=p1,organization=org3,beginDate=date(01,01,2013), endDate=date(01,02,2013), presentOrganization=False)
        Associations.objects.create(person=p2,organization=org3,beginDate=date(01,01,2014))
        ExternalOrgIdentifiers.objects.create(organization=org2,identifierName='other',identifierCode="code1")
        org3.parentOrganization = org2
        org3.save()


    def test_organization(self):
        org1 = Organization.objects.get(name="org1")
        self.assertEqual(org1.persons.count(), 0)

        org2 = Organization.objects.get(name="org2")
        self.assertEqual(org2.persons.count(), 2)
        self.assertEqual(org2.persons.get(presentOrganization=True), 2)

        org3 = Organization.objects.get(name="org3")
        self.assertEqual(org3.persons.count(), 2)
        self.assertEqual(org3.persons.get(presentOrganization=True), 1)

    def test_association(self):
        # need to find a way to get association to test begin data time
        # self.assertEqual(org3.persons.get(familyName='last')., 1)
        pass

    def test_externalIdentifier(self):
        org2 = Organization.objects.get(name="org2")
        self.assertEqual(org2.externalIdentifiers.count(), 1)

    def test_parent(self):
        org2 =  Organization.objects.get(name="org2")
        org3 = Organization.objects.get(name="org3")
        self.assertEqual(org3.parentOrganization, org2)

pass