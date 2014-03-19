__author__ = 'valentin'

from django.utils import unittest

from hs.hs_user_org.tests import personTest, testExternalOrgIdentifiers, organizationTest ,ScholarAndGroupTest
from test import *
from testExternalOrgIdentifiers import  *

def suite():
    tests_loader = unittest.TestLoader().loadTestsFromModule
    test_suites = []
    test_suites.append(tests_loader(testExternalOrgIdentifiers))
    test_suites.append(tests_loader(personTest))
    test_suites.append(tests_loader(organizationTest))
    test_suites.append(tests_loader(ScholarAndGroupTest))
    return unittest.TestSuite(test_suites)

