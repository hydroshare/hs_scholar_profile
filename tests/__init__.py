__author__ = 'valentin'

from django.utils import unittest

from . import personTest, testExternalOrgIdentifiers, organizationTest ,ScholarAndGroupTest,UserProfileTest,UserOrgViewTests
from test import *
from testExternalOrgIdentifiers import  *

def suite():
    tests_loader = unittest.TestLoader().loadTestsFromModule
    test_suites = []
    test_suites.append(tests_loader(testExternalOrgIdentifiers))
    test_suites.append(tests_loader(personTest))
    test_suites.append(tests_loader(organizationTest))
    test_suites.append(tests_loader(ScholarAndGroupTest))
    test_suites.append(tests_loader(UserProfileTest))
    test_suites.append(tests_loader(UserOrgViewTests))
    return unittest.TestSuite(test_suites)

