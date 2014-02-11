from django.contrib.contenttypes import generic
from django.contrib.auth.models import User, Group
from django.db import models
from mezzanine.pages.models import Page, RichText
from mezzanine.core.models import Ownable
from hs_core.models import AbstractResource

# user content models to handle organizations and people
# modeled after sciencebase.gov: https://my.usgs.gov/confluence/display/sciencebase/ScienceBase+Directory+Services
# orcid

# Name
# DisplayName
# DisplayText
# URL
# Email
# Description
# Rich Description HTML
# Aliases
# Active
# Primary Location
#===================================================================
class Party(models.Model):
    #ID = models.AutoField(primary_key=True )
    # not fully sure how to use name. USGS uses distinct LDAP Id's here.
    name = models.CharField(verbose_name="A unique name for the record",help_text="Name of party (org or person)")
    creditName = models.CharField(verbose_name="An optional label to display instead of the record name.",blank=True)
    url = models.URLField(verbose_name="Web Page of Organization or Person",blank=True)
    email = models.EmailField(verbose_name="Contact Email address of Organization or Person",blank=True)
    description = models.TextField(verbose_name="",blank=True)
    otherNames = models.ForeignKey(OtherNames, null=True)
    primaryLocation = models.ForeignKey(PartyLocation, null=True)
    notes = models.TextField(blank=True)
    createdDate = models.DateField(auto_now_add=True)
    lastUpdate = models.DateField(auto_now=True)

class OtherNames (models.Model):
    #ID = models.AutoField(primary_key=True)
    alias = models.CharField(verbose_name="Alias")
    annotation = models.CharField(verbose_name="type of alias")

class PartyLocation (models.Model):
    #ID = models.AutoField(primary_key=True)
    mailAddress = models.TextField(verbose_name="Mailing Address")
    streetAddress = models.TextField( verbose_name="Street or Delivery Address",blank=True)
    officePhone = models.CharField(verbose_name="Office or main phone number",blank=True)
    faxPhone = models.CharField(verbose_name="fax phone", blank=True)

#=======================================================================================
# ORGANIZATION
# ======================================================================================
ORG_TYPES_CHOICES = (
        ("hydroshare"	,"Hydroshare Group" )
        ,("project","Research Project")
        ,("gradProject","Project as part of a Thesis or Dissertation")
        ,("gradCourse","University Graduate Course")
        ,("undergradCourse","University Undergraduate Course")
        ,("commercial","Commercial/Professional")
        ,("gov","Government Organization")
        ,("nonprofit", "Non-profit Organization")
        ,("k12","School Activity Kindergarten to 12th Grade")
        ,("ccCourse", "Community College Course")
        ,("other", "Other")
        ,("Unspecified","Unspecified")
     )
class Organization (Party):
    logoUrl = models.ImageField(blank=True)
    #smallLogoUrl = models.ImageField()
    parentOrganization =  models.ForeignKey( Party, null=True)
    organizationType = models.CharField(choices=ORG_TYPES_CHOICES)

#======================================================================================
# PERSON
# note: Hydroshare User is near end of document
#======================================================================================
class Person (Party):
    givenName = models.CharField()
    familyName = models.CharField()
    jobTitle = models.CharField()
    # This makes a full org record required.
    # Should this be just a text field?
    organization = models.ForeignKey(Organization)
    cellPhone = models.CharField(verbose_name="Cell Phone", blank=True) # sciencebase
    associations = models.ForeignKey(Associations)
# do we want some adviser field.


PERSON_TYPES_CHOICES = (
        ("faculty"	,"University Faculty" )
        ,("research","University Professional or Research Staff")
        ,("postdoc","Post-Doctoral Fellow")
        ,("grad","University Graduate Student")
        ,("undergrad","University Undergraduate Student")
        ,("commercial","Commercial/Professional")
        ,("gov","Government Official")
        ,("nonprofit", "Non-profit Organizations")
        ,("k12","School Student Kindergarten to 12th Grade")
        ,("ccfaculty", "Community College Faculty")
        ,("ccstudent", "Community College Student")
        ,("other", "Other")
        ,("Unspecified","Unspecified")
     )


class PersonKeywords(models.Model):
    keyword = models.CharField()
    createdDate = models.DateField(auto_now_add=True)
    pass


class PersonDemographics(models.Model):
    # spliting in order to make demographics optional
    public = models.BooleanField(verbose_name="Make My Demographics Public", help_text="My Demographics are Public")
    personType = models.CharField(choice=PERSON_TYPES_CHOICES)
    AGE_CHOICES = ( ("under_17", "you age is Under 17")
                    ,("18_29", "you are between 18-29")
                    ,("30_39", "you are between 30-39")
                    , ("40_49", "you are between 40-49")
                    , ("51_59", "you are between 50-59")
                    , ("over_60", "you are over 60")
    )
    age = models.CharField(max_length=8,choices=AGE_CHOICES)
    keywords = models.ForeignKey(PersonKeywords)
    pass




###########################################################
# ACTIVITIES
# following the pattern of OrcIdXML, activities are a general class
#  for associations, works, etc
#  Presently models,
#     * Associations, which are person-org
#     * adds Workshops (after requirement)
#
###########################################################
class Activities (models.Model):
    pass
# http://support.orcid.org/knowledgebase/articles/151817-xml-for-affiliations

class Associations(Activities):
    # object to handle a person being in one or more organizations
    organization = models.ManyToManyField(Organization)
    beginDate = models.DateField(verbose_name="begin date of associate")
    endDate = models.DateField(null=True, verbose_name="End date of association. Empty if still with organization")
    jobTitle = models.CharField(verbose_name="Title", blank=True)
    presentOrganization=models.BooleanField(verbose_name="Presently with Organization",  default=True, help_text="You are presently a member of this Organization")
    pass

class Workshops (Activities):
    workshopName = models.CharField()
    beginDate = models.DateField(verbose_name="begin date of workshop")
    endDate = models.DateField(null=True, verbose_name="End date of workshop. Empty if one day")
    pass
##############################################################
# HYDROSHARE SPECIFIC TYPES
# instances of User and Organziaton to implement in hydroshare
###############################################################

class HydroshareGroup (Organization):
    pass
    # need to set organizationType to Hydroshare

#=======================================
# USER Profile
#=======================================

class ExternalPartyIdentifers (models.Model):
    IDENTIFIER_CHOICE = ( ("orcid", "ORCID Identifier")
    ,("linkedin", "Linked In URL")
    , ("twitter", "twitterName")
    , ("rg", "ResearchGate Username")
    ,("mendeley", "Mendeley username")
    ,("blog", "blog or personal page")
    ,("ProjectPage", "page for project")
    ,("other", "other"))
    identifierName = models.CharField(choices=IDENTIFIER_CHOICE,verbose_name="User Identities",
                                      help_text="User identities from exernal sites" )
    otherName = models.CharField(verbose_name="If other is selected, type of identifier", blank=True)
    identifierCode = models.CharField(verbose_name="Username or Identifier for site")
    createdDate = models.DateField(auto_now_add=True)
    # validation needed. if identifierName =='other' then otherName must be populated.

class ResearcherUrls(ExternalPartyIdentifers):
    # orcid XML separates Researher URLs from External Identifiers
    pass

class HydoshareUser (Person):
    user = models.OneToOneField("auth.user")
    demographics = models.OneToOneField( PersonDemographics)
    #orcidIdentifier = models.CharField();
    externalIdentifiers = models.ForeignKey(ExternalPartyIdentifers, null=True)
    pass

############################################################
# DJANGO OPTIONS
############################################################
AUTH_PROFILE_MODULE = "hs_user_org.HydoshareUser"

ACCOUNTS_PROFILE_FORM_EXCLUDE_FIELDS = (
    "lastUpdate",
    "createdDate",
)

