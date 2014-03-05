from django.test import TestCase
from hs.hs_user_org.models import Organization, Person, ResearchGroup,ResearchGroupAssociations,ResearchUser
from django.contrib.auth.models import User


__author__ = 'valentin'


class ResearchUserAndGroupTest(TestCase):
    def setUp(self):

        u1 = User.objects.create(username='user1')
        researchUser = ResearchUser.objects.Create(user=u1,giverName="Jon",familyName="Smith")
        rGroup = ResearchGroup.objects.Create(name="ResearchGroup",createdBy=u1)
        ResearchGroupAssociations.objects.Create(persons=[researchUser],group=rGroup)

    def test_ResearchUser(self):
        r1 = ResearchUser.get(givenName="Jon")
        self.assertEqual(r1.user.username, 'user1')
        self.assertEqual(r1.groups.count(), 1)


    pass