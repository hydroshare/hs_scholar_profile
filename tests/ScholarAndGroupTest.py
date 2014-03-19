from django.test import TestCase
from hs.hs_user_org.models import Organization, Person, ScholarGroup,ScholarGroupAssociations,Scholar
from django.contrib.auth.models import User
from datetime import date

__author__ = 'valentin'


class ScholarAndGroupTest(TestCase):
    def setUp(self):

        u1 = User.objects.create(username='user1')
        p1 = Person.objects.create(givenName="first", familyName="last", name="First Last")
        scholar = Scholar.objects.create(user=u1,person= p1)
        rGroup = ScholarGroup.objects.create(name="ResearchGroup",createdBy=scholar)
        ScholarGroupAssociations.objects.create(scholar=scholar,group=rGroup, beginDate=date(2013,01,10))

    def test_ScholarUser(self):

        rq = Scholar.objects.filter(person__givenName="first")
        self.assertEqual(rq.count(),1)
        firstOne = rq.first()
        self.assertEqual(firstOne.user.username, 'user1')
        self.assertEqual(firstOne.groups.count(), 1)


    pass