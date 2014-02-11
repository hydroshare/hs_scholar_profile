from django.test import TestCase
from django.contrib.auth import get_user_model
#from django_webtest import WebTest
from .models import Organization, Person, OtherNames


__author__ = 'valentin'


class TestPerson(TestCase):
    aPerson = Person.objects.create(firstName='first',
                          lastName='last',
                          name="First Last"
                          )
    anAlias = OtherNames.objects.create(alias="differentLastName, first", annotation="OtherName" )
    aPerson.otherNames_set.add(anAlias)


    pass