from django.contrib.contenttypes import generic
from django.contrib.auth.models import User, Group
from django.db import models
from mezzanine.pages.models import Page, RichText
from mezzanine.core.models import Ownable
from hs_core.models import AbstractResource

# user content models to handle organizations and people
# modeled after
# sciencebase.gov: https://my.usgs.gov/confluence/display/sciencebase/ScienceBase+Directory+Services
# orcid: https://github.com/ORCID/ORCID-Source/blob/master/orcid-model/src/main/resources/README.md#orcid-xsd-information

#==================================================================
'''

User and Organization Hierarchy

Party
|- Organizations
       Includes a Organization Type property
|- Group
   includes a GroupType
   |- hydroshareGroup
|- People
   |- HydroshareUser
       user field contains Django User Properties

ExternalIdentifiers
|- ResearcherUrls


Activity
|- Assocations
   this associates user with organizations
|- Workshop

PersonDemographics
  This separates the demographics needed by the research project from the user, has a permission

'''
#===================================================================

class OtherNames(models.Model):
    #ID = models.AutoField(primary_key=True)
    otherName = models.CharField(verbose_name="Other Name or alias")
    ANNOTATION_TYPE_CHOICE = (
        ("change", "Name Change"),
        ("citation", "Publishing Alias"),
        ("fullname", "Full Name variation"),
        ("other", "other type of alias")
    )
    annotation = models.CharField(verbose_name="type of alias", default="citation")


class PartyLocation(models.Model):
    #ID = models.AutoField(primary_key=True)
    mailAddress = models.TextField(verbose_name="Mailing Address")
    streetAddress = models.TextField(verbose_name="Street or Delivery Address", blank=True)
    officePhone = models.CharField(verbose_name="Office or main phone number", blank=True)
    faxPhone = models.CharField(verbose_name="fax phone", blank=True)

class Party(models.Model):
    #ID = models.AutoField(primary_key=True )
    # not fully sure how to use name. USGS uses distinct LDAP Id's here.
    name = models.CharField(verbose_name="A unique name for the record", help_text="Name of party (org or person)")
    creditName = models.CharField(verbose_name="An optional label to display instead of the record name.", blank=True)
    url = models.URLField(verbose_name="Web Page of Organization or Person", blank=True)
    email = models.EmailField(verbose_name="Contact Email address of Organization or Person", blank=True)
    description = models.TextField(verbose_name="", blank=True)
    otherNames = models.ForeignKey(OtherNames, null=True)  # alias in sciencebase
    primaryLocation = models.ForeignKey(PartyLocation, null=True)
    notes = models.TextField(blank=True)
    createdDate = models.DateField(auto_now_add=True)
    lastUpdate = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Group(models.Model):
    ''' Groups that users are associated with.

    Note:
      Done to differentiate virtual hydroshare groups from real organizations
    '''
    name = models.CharField()
    description = models.TextField()
    GROUP_TYPES_CHOICES = (
        ("hydroshare", "Generic Hydroshare Group"),
        ("project", "Research Project"),
        ("gradProject", "Project as part of a Thesis or Dissertation"),
        ("gradCourse", "University Graduate Course"),
        ("undergradCourse", "University Undergraduate Course"),
        ("k12", "School Activity Kindergarten to 12th Grade"),
        ("ccCourse", "Community College Course"),
        ("other", "Other"),
        ("Unspecified", "Unspecified")
    )
    groupType = models.CharField(choices=GROUP_TYPES_CHOICES)
    createdDate = models.DateField(auto_created=True)

    class Meta:
        abstract = True



#=======================================================================================
# ORGANIZATION
# ======================================================================================
ORG_TYPES_CHOICES = (
    ("commercial", "Commercial/Professional")
    , ("gov", "Government Organization")
    , ("nonprofit", "Non-profit Organization")
    , ("k12", "School  Kindergarten to 12th Grade")
    , ("ccCourse", "Community College ")
    , ("other", "Other")
    , ("Unspecified", "Unspecified")
)


class ExternalOrgIdentifiers(models.Model):
    IDENTIFIER_CHOICE = (
                         ("LOC", "Library of Congress")
                         , ("NSF", "National Science Foundation")
                         , ("twitter", "twitterHandle")
                         , ("ProjectPage", "page for project")
                         , ("other", "other")
    )
    identifierName = models.CharField(choices=IDENTIFIER_CHOICE, verbose_name="User Identities",
                                      help_text="User identities from exernal sites")
    otherName = models.CharField(verbose_name="If other is selected, type of identifier", blank=True)
    identifierCode = models.CharField(verbose_name="Username or Identifier for site")
    createdDate = models.DateField(auto_now_add=True)
    # validation needed. if identifierName =='other' then otherName must be populated.


class Organization(Party):
    logoUrl = models.ImageField(blank=True)
    #smallLogoUrl = models.ImageField()
    parentOrganization = models.ForeignKey('self', null=True)
    organizationType = models.CharField(choices=ORG_TYPES_CHOICES)

###########################################################
# ACTIVITIES
# following the pattern of OrcIdXML, activities are a general class
#  for associations, works, etc
#  Presently models,
#     * Associations, which are person-org
#     * adds Workshops (after requirement)
#
###########################################################
class Activities(models.Model):
    '''
    this is a base class for users associated with
     Organizations (associations)
     Workshops
     Citations -- not yet implemented. should be separate
    '''
    createdDate = models.DateField(auto_created=True)

    class Meta:
        abstract = True

    pass


# http://support.orcid.org/knowledgebase/articles/151817-xml-for-affiliations

class Associations(Activities):
    # object to handle a person being in one or more organizations
    organization = models.ManyToManyField(Organization)
    beginDate = models.DateField(verbose_name="begin date of associate")
    endDate = models.DateField(null=True, verbose_name="End date of association. Empty if still with organization")
    jobTitle = models.CharField(verbose_name="Title", blank=True)
    presentOrganization = models.BooleanField(verbose_name="Presently with Organization", default=True,
                                              help_text="You are presently a member of this Organization")
    pass


class Workshops(Activities):
    workshopName = models.CharField()
    beginDate = models.DateField(verbose_name="begin date of workshop")
    endDate = models.DateField(null=True, verbose_name="End date of workshop. Empty if one day")

    pass
#======================================================================================
# PERSON
# note: Hydroshare User is near end of document
#======================================================================================
class Person(Party):
    givenName = models.CharField()
    familyName = models.CharField()
    jobTitle = models.CharField()
    # This makes a full org record required.
    # Should this be just a text field?
    organization = models.ForeignKey(Organization)
    cellPhone = models.CharField(verbose_name="Cell Phone", blank=True)  # sciencebase
    associations = models.ForeignKey(Associations)
    # do we want some adviser field.

    def __init__(self, *args, **kwargs):
        super(Person, self).__init__(*args, **kwargs)
        if self.givenName is not None and self.familyName is not None:
            self.name = self.givenName + self.familyName




PERSON_TYPES_CHOICES = (
    ("faculty", "University Faculty" )
    , ("research", "University Professional or Research Staff")
    , ("postdoc", "Post-Doctoral Fellow")
    , ("grad", "University Graduate Student")
    , ("undergrad", "University Undergraduate Student")
    , ("commercial", "Commercial/Professional")
    , ("gov", "Government Official")
    , ("nonprofit", "Non-profit Organizations")
    , ("k12", "School Student Kindergarten to 12th Grade")
    , ("ccfaculty", "Community College Faculty")
    , ("ccstudent", "Community College Student")
    , ("other", "Other")
    , ("Unspecified", "Unspecified")
)


class PersonKeywords(models.Model):
    keyword = models.CharField()
    createdDate = models.DateField(auto_now_add=True)
    pass


class PersonDemographics(models.Model):
    '''
    This separates the demographics needed by the research project from the user, has a permission
    Allows for Demographics to be optional
    '''
    public = models.BooleanField(default=False, verbose_name="Make My Demographics Public",
                                 help_text="My Demographics are Public")
    personType = models.CharField(choices=PERSON_TYPES_CHOICES)
    AGE_CHOICES = (("under_17", "you age is Under 17")
                   , ("18_29", "you are between 18-29")
                   , ("30_39", "you are between 30-39")
                   , ("40_49", "you are between 40-49")
                   , ("51_59", "you are between 50-59")
                   , ("over_60", "you are over 60")
    )
    age = models.CharField(max_length=8, choices=AGE_CHOICES)
    keywords = models.ForeignKey(PersonKeywords)
    pass



##############################################################
# HYDROSHARE SPECIFIC TYPES
# instances of User and Organziaton to implement in hydroshare
###############################################################


#=======================================
# USER Profile
#=======================================

class ExternalPartyIdentifiers(models.Model):
    IDENTIFIER_CHOICE = ( ("orcid", "ORCID Identifier")
                          , ("linkedin", "Linked In URL")
                          , ("VIVO", "VIVO Identifier")
                          , ("twitter", "twitterName")
                          , ("rg", "ResearchGate Username")
                          , ("mendeley", "Mendeley username")
                          , ("blog", "blog or personal page")
                          , ("ProjectPage", "page for project")
                          , ("other", "other"))
    identifierName = models.CharField(choices=IDENTIFIER_CHOICE, verbose_name="User Identities",
                                      help_text="User identities from external sites")
    otherName = models.CharField(verbose_name="If other is selected, type of identifier", blank=True)
    identifierCode = models.CharField(verbose_name="Username or Identifier for site")
    createdDate = models.DateField(auto_now_add=True)
    # validation needed. if identifierName =='other' then otherName must be populated.


class ResearcherUrls(ExternalPartyIdentifiers):
    '''
    Separate Research ID from other identifiers.
    This will also allow for some validation process for these identifiers
    Note: orcid XML separates Researcher URLs from External Identifiers

    Defined as a proxy class  of ExternalPartyIdentifiers, so the data is stored in the same table
    '''
    class Meta:
        abstract = True

    pass


class HydoshareUser(Person):
    user = models.OneToOneField("auth.user")
    demographics = models.OneToOneField(PersonDemographics)
    #orcidIdentifier = models.CharField();
    externalIdentifiers = models.ForeignKey(ExternalPartyIdentifiers, null=True)
    # need a function to handle and store an orcid in external identifiers
    pass

#===========================
# groups
#============================
class HydroshareGroup(Group):
    createdBy = models.ForeignKey(HydoshareUser)

    # def __init__(self, *args, **kwargs):
    #     self._meta.get_field('groupType').default = 'hydroshare'
    #     super(HydroshareGroup, self).__init__(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super(HydroshareGroup, self).__init__(*args, **kwargs)
        self.groupType = 'hydroshare'


    pass
    # need to set organizationType to Hydroshare


class HydroshareWorkshop(Workshops, Group):
    ''' Multiple inheritance?
    '''
    pass

############################################################
# DJANGO OPTIONS
############################################################
AUTH_PROFILE_MODULE = "hs.hs_user_org.HydoshareUser"

ACCOUNTS_PROFILE_FORM_EXCLUDE_FIELDS = (
    "lastUpdate",
    "createdDate",
)

