from __future__ import absolute_import
from django.test import TestCase
from django.contrib.auth import get_user_model
#from django_webtest import WebTest
from ..models import Organization, Person,OrgAssociations, ExternalOrgIdentifiers
from datetime import date



__author__ = 'valentin'


class organizationTest(TestCase):
    def setUp(self):
        p1 = Person.objects.create(givenName="first", familyName="last", name="First Last")
        p2 = Person.objects.create(givenName="last", familyName="first", name="last first")
        Organization.objects.create(name="org1")
        org2 = Organization.objects.create(name="org2")
        OrgAssociations.objects.create(person=p1,organization=org2,beginDate=date(2013,01,01))
        OrgAssociations.objects.create(person=p2,organization=org2,beginDate=date(2014,01,01))
        org3 = Organization.objects.create(name="org3")
        OrgAssociations.objects.create(person=p1,organization=org3,beginDate=date(2013,01,10), endDate=date(2013,02,01), presentOrganization=False)
        OrgAssociations.objects.create(person=p2,organization=org3,beginDate=date(2014,01,01))
        ExternalOrgIdentifiers.objects.create(organization=org2,identifierName='other',identifierCode="code1")
        org3.parentOrganization = org2
        org3.save()


    def test_organization(self):
        org1 = Organization.objects.get(name="org1")
        self.assertEqual(org1.hs_scholar_profile_person_members.count(), 0)

        org2 = Organization.objects.get(name="org2")
        self.assertEqual(org2.hs_scholar_profile_person_members.count(), 2)
        associations = OrgAssociations(presentOrganization=True,organization=org2)
        self.assertEqual(associations.presentOrganization, True)
        self.assertEqual(associations.organization, org2)

        org3 = Organization.objects.get(name="org3")
        self.assertEqual(org3.hs_scholar_profile_person_members.count(), 2)
        # need to learn the query languages and query set
        #self.assertEqual(org3..get(presentOrganization=True), 1)

    def test_association(self):
        # need to find a way to get association to test begin data time
        # self.assertEqual(org3.persons.get(familyName='last')., 1)
        p1 = Person.objects.get(familyName="last")
        print(p1.familyName)
        print(p1.organizations.count())
        #print(p.name for p in  p1.organizations)
        self.assertEqual(p1.organizations.count(), 2)
        pass

    def test_association_filter(self):
        # confused... should this be organizations like the related_name= field
        allorg = Person.objects.filter(orgassociations__presentOrganization='true' )
        print(allorg.count())
        self.assertNotEquals(Person.objects.all().count(), allorg.count())

        p1org = Person.objects.filter(familyName__exact='last',orgassociations__presentOrganization='true' )
        self.assertEqual(p1org.count(),1)
        pass

    def test_externalIdentifier(self):
        org2 = Organization.objects.get(name="org2")
        self.assertEqual(org2.externalIdentifiers.count(), 1)

    def test_parent(self):
        org2 =  Organization.objects.get(name="org2")
        org3 = Organization.objects.get(name="org3")
        self.assertEqual(org3.parentOrganization, org2)

pass