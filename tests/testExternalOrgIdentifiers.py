from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import ExternalOrgIdentifiers, OtherNames

__author__ = 'valentin'


class testExternalOrgIdentifiers(TestCase):
    def setUp(self):
        ExternalOrgIdentifiers.objects.create(identifierCode = "testExternalOrg",
              identifierName = "This is a test external org")
        other1 = OtherNames.objects.create(otherName="other1",annotation="other")
        other2 = OtherNames.objects.create(otherName="other2",annotation="fullname")
        org = ExternalOrgIdentifiers.objects.create(identifierCode = "testExternalOrg2",
        identifierName = "This is a test external org", otherName = [other1,other2]
        )

    def test_ExternalOrgIdentifiers(self):
        """just a quick test to learn testing"""
        org1 = ExternalOrgIdentifiers.objects.get(identifierCode="testExternalOrg")
        self.assertEqual(org1.otherName.count(), 0)
        self.assertEqual(org1.identifierName, 'This is a test external org')

    def test_ExternalOrgIdentifiersOtherNames(self):
        """has two other names"""
        org1 = ExternalOrgIdentifiers.objects.get(identifierCode="testExternalOrg2")
        self.assertEqual(org1.otherName.count(), 2)
        self.assertEqual(org1.identifierName, 'This is a test external org')



