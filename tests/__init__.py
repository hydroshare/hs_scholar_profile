__author__ = 'valentin'

from django.utils import unittest

from hydroshare2.hs.hs_user_org.tests import personTest, testExternalOrgIdentifiers
from test import *
from testExternalOrgIdentifiers import  *

def suite():
    tests_loader = unittest.TestLoader().loadTestsFromModule
    test_suites = []
    test_suites.append(tests_loader(testExternalOrgIdentifiers))
    test_suites.append(tests_loader(personTest))

    return unittest.TestSuite(test_suites)

