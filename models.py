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

PartyModel
|- Organizations
       Includes a Organization Type property
|- Group
   includes a GroupType
   |- ResearchGroup (disabled, model design issue)
|- People
   |- ResearchUser
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




class PartyLocation(models.Model):
    #ID = models.AutoField(primary_key=True)
    mailAddress = models.TextField(verbose_name="Mailing Address")
    streetAddress = models.TextField(verbose_name="Street or Delivery Address", blank=True)
    officePhone = models.CharField(verbose_name="Office or main phone number", blank=True,max_length='30')
    faxPhone = models.CharField(verbose_name="fax phone", blank=True,max_length='30')


class PartyGeolocation(models.Model):
    name = models.CharField(max_length=100)
    geonamesUrl = models.URLField(verbose_name="URL of Geonames reference")
    # add geolocation
    class Meta:
        abstract = True

class City(PartyGeolocation):
    def __init__(self, *args, **kwargs):
        super(City, self).__init__(*args, **kwargs)
        City._meta.get_field('name').verbose_name ="City"

    pass

class Region(PartyGeolocation):
    def __init__(self, *args, **kwargs):
        super(Region, self).__init__(*args, **kwargs)
        Region._meta.get_field('name').verbose_name ="State or Region"

    pass

class Country(PartyGeolocation):
    def __init__(self, *args, **kwargs):
        super(Country, self).__init__(*args, **kwargs)
        Country._meta.get_field('name').verbose_name ="Country"

    pass


class PartyModel(models.Model):
    #ID = models.AutoField(primary_key=True )
    # not fully sure how to use name. USGS uses distinct LDAP Id's here.
    # change to uniqueID
    uniqueCode = models.CharField(verbose_name="A unique name for the record", help_text="Name of party (org or person)",max_length='255')
    name = models.CharField(verbose_name="Full name of Organization or Person", blank=True,max_length='255')
    url = models.URLField(verbose_name="Web Page of Organization or Person", blank=True,max_length='255')
    email = models.EmailField(verbose_name="Contact Email address of Organization or Person", blank=True,max_length='255')
    # is a description on Page, which Person, Organization, and Group inherit from
    #description = models.TextField(verbose_name="Detailed description of Organization or Biography of a Person", blank=True)
    primaryLocation = models.ForeignKey(PartyLocation, null=True)
    notes = models.TextField(blank=True)
    createdDate = models.DateField(auto_now_add=True)
    lastUpdate = models.DateField(auto_now=True)

    class Meta:
        abstract = True





#======================================================================================
# PERSON
# note: Hydroshare User is near end of document
#======================================================================================
class PersonModel(PartyModel):
    givenName = models.CharField(max_length='125') # given+family =name of party needs to be 255
    familyName = models.CharField(max_length='125') # given+family =name of party needs to be 255
    jobTitle = models.CharField(max_length='100')
    # This makes a full org record required.
    # Should this be just a text field?
    #organization = models.ForeignKey(Organization, null=True) # one to many
    cellPhone = models.CharField(verbose_name="Cell Phone", blank=True,max_length='30')  # sciencebase
    #associations = models.ForeignKey(Associations, null=True) # one to many
    # do we want some adviser field.

    def __init__(self, *args, **kwargs):
        super(PersonModel, self).__init__(*args, **kwargs)
        if self.givenName is not None and self.familyName is not None:
            self.name = self.givenName + ' ' + self.familyName

    class Meta:
        abstract = True

class Person(Page, PersonModel):
    def __init__(self, *args, **kwargs):
        super(Person, self).__init__(*args, **kwargs)
    pass


USER_TYPES_CHOICES = (
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


class UserKeywords(models.Model):
    person = models.ForeignKey(Person, related_name="keywords")
    keyword = models.CharField(max_length='100')
    createdDate = models.DateField(auto_now_add=True)
    pass


class UserDemographics(models.Model):
    '''
    This separates the demographics needed by the research project from the user, has a permission
    Allows for Demographics to be optional
    '''
    public = models.BooleanField(default=False, verbose_name="Make My Demographics Public",
                                 help_text="My Demographics are Public")
    userType = models.CharField(choices=USER_TYPES_CHOICES,max_length='255')
    #keywords = models.ForeignKey(UserKeywords) many to one
    city = models.ForeignKey(City, null=True)
    region = models.ForeignKey(Region, null=True)
    country = models.ForeignKey(Country, null=True)
    pass

class OtherNames(models.Model):
    #ID = models.AutoField(primary_key=True)
    # relation will show in PartyModel as otherNames
    persons = models.ForeignKey(to=Person,related_name='otherNames' )
    otherName = models.CharField(verbose_name="Other Name or alias",max_length='255')
    ANNOTATION_TYPE_CHOICE = (
        ("change", "Name Change"),
        ("citation", "Publishing Alias"),
        ("fullname", "Full Name variation"),
        ("other", "other type of alias")
    )
    annotation = models.CharField(verbose_name="type of alias", default="citation",max_length='10')
#=======================================================================================
# ORGANIZATION
# ======================================================================================
# make consistent with CUAHSI
ORG_TYPES_CHOICES = (
    ("commercial", "Commercial/Professional")
    , ("university","University")
    , ("college", "College")
    , ("gov", "Government Organization")
    , ("nonprofit", "Non-profit Organization")
    , ("k12", "School  Kindergarten to 12th Grade")
    , ("cc", "Community College ")
    , ("other", "Other")
    , ("Unspecified", "Unspecified")
)

class OrganizationModel(PartyModel):
    logoUrl = models.ImageField(blank=True, upload_to='orgLogos')
    #smallLogoUrl = models.ImageField()
    parentOrganization = models.ForeignKey('self', null=True)
    organizationType = models.CharField(choices=ORG_TYPES_CHOICES,max_length='14')
    # externalIdentifiers from ExternalOrgIdentifiers

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        abstract = True

class Organization(Page, OrganizationModel):
    persons = models.ManyToManyField(to=Person,through="OrgAssociations", null=True,related_name="organizations")
    pass

class ExternalOrgIdentifiers(models.Model):
    organization = models.ForeignKey(to=Organization, related_name='externalIdentifiers')
    IDENTIFIER_CHOICE = (
                         ("LOC", "Library of Congress")
                         , ("NSF", "National Science Foundation")
                         , ("linked","linked Data URL")
                         , ("twitter", "twitterHandle")
                         , ("ProjectPage", "page for project")
                         , ("other", "other")
    )
    identifierName = models.CharField(choices=IDENTIFIER_CHOICE, verbose_name="User Identities",
                                      help_text="User identities from exernal sites",max_length='10')
    otherName = models.CharField(verbose_name="If other is selected, type of identifier", blank=True,max_length='255')
    identifierCode = models.CharField(verbose_name="Username or Identifier for site",max_length='255')
    createdDate = models.DateField(auto_now_add=True)
    # validation needed. if identifierName =='other' then otherName must be populated.

###########################################################
# ACTIVITIES
# following the pattern of OrcIdXML, activities are a general class
#  for associations, works, etc
#  Presently models,
#     * Associations, which are person-org
#     * adds Workshops (after requirement)
############################################################
class ActivitiesModel(models.Model):
    '''
    this is a base class for users associated with
     Organizations (associations)
     Workshops
     Citations -- not yet implemented. should be separate
    '''
    createdDate = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

    pass


# http://support.orcid.org/knowledgebase/articles/151817-xml-for-affiliations

class OrgAssociations(ActivitiesModel):
    # object to handle a person being in one or more organizations
    organization = models.ForeignKey(Organization)
    person = models.ForeignKey(Person)
    beginDate = models.DateField(verbose_name="begin date of associate")
    endDate = models.DateField(null=True, verbose_name="End date of association. Empty if still with organization")
    jobTitle = models.CharField(verbose_name="Title", blank=True,max_length='100')
    presentOrganization = models.BooleanField(verbose_name="Presently with Organization", default=True,
                                              help_text="You are presently a member of this Organization")

    def __unicode__(self):
        return u'%s %s' % (self.organization.name + self.person.name)

# not a priority
# class Workshops(ActivitiesModel):
#     workshopName = models.CharField(max_length='255')
#     beginDate = models.DateField(verbose_name="begin date of workshop")
#     endDate = models.DateField(null=True, verbose_name="End date of workshop. Empty if one day")
#
#     pass

class GroupModel(models.Model):
    '''This is a collection of persons that is less formal than an organization.


    '''
    # person/user left to specific implementations, since issues with model framework
    # associations are object specific
    # * general group has Persons (and subclass ResearchUser)
    # * ResearchGroup has ResearchUsers only
    #
    name = models.CharField(max_length='100')
    groupDescription = models.TextField()
    # Group purpose, open field
    purpose = models.CharField(blank=True, verbose_name="Purpose - a Short description",
                               help_text="Purpose - a several work description such as: Research Project",
                               max_length=100)
    # GROUP_TYPES_CHOICES = (
    #     ("hydroshare", "Generic Hydroshare Group"),
    #     ("project", "Research Project"),
    #     ("gradProject", "Project as part of a Thesis or Dissertation"),
    #     ("gradCourse", "University Graduate Course"),
    #     ("undergradCourse", "University Undergraduate Course"),
    #     ("k12", "School Activity Kindergarten to 12th Grade"),
    #     ("ccCourse", "Community College Course"),
    #     ("other", "Other"),
    #     ("Unspecified", "Unspecified")
    # )
    # groupType = models.CharField(choices=GROUP_TYPES_CHOICES,max_length='24')
    createdDate = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

class GeneralGroup(Page,GroupModel):
    persons = models.ManyToManyField(to=Person,through='GeneralGroupAssociations',related_name="groups+",)
    pass

class GeneralGroupAssociations(ActivitiesModel):
    # object to handle a person being in one or more organizations
    group = models.ForeignKey(GeneralGroup)
    person = models.ForeignKey(Person)
    beginDate = models.DateField(verbose_name="begin date of associate")
    endDate = models.DateField(null=True, verbose_name="End date of association. Empty if still with organization")
    title = models.CharField(verbose_name="Title or Responsibility", blank=True,max_length='100')

    pass

##############################################################
# HYDROSHARE SPECIFIC TYPES
# instances of User and Organziaton to implement in hydroshare
###############################################################


#=======================================
# USER Profile
#=======================================

class ExternalPersonIdentifiers(models.Model):
    IDENTIFIER_CHOICE = ( ("orcid", "ORCID Identifier")
                          , ("linkedin", "Linked In URL")
                          , ("VIVO", "VIVO Identifier")
                          , ("twitter", "twitterName")
                          , ("rg", "ResearchGate Username")
                          , ("mendeley", "Mendeley username")
                          , ("blog", "blog or personal page")
                          , ("ProjectPage", "page for project")
                          , ("other", "other"))
    person = models.ForeignKey(Person, related_name="externalIdentifiers")
    identifierName = models.CharField(choices=IDENTIFIER_CHOICE, verbose_name="User Identities",
                                      help_text="User identities from external sites",max_length='255')
    otherName = models.CharField(verbose_name="If other is selected, type of identifier", blank=True,max_length='255')
    identifierCode = models.CharField(verbose_name="Username or Identifier for site",max_length='24')
    createdDate = models.DateField(auto_now_add=True)
    # validation needed. if identifierName =='other' then otherName must be populated.


class ResearcherUrls(ExternalPersonIdentifiers):
    '''
    Separate Research ID from other identifiers.
    This will also allow for some validation process for these identifiers
    Note: orcid XML separates Researcher URLs from External Identifiers

    Defined as a proxy class  of ExternalPartyIdentifiers, so the data is stored in the same table
    '''
    class Meta:
        proxy = True

    pass


class ResearchUser(PersonModel):
    user = models.OneToOneField("auth.user")
    demographics = models.OneToOneField(UserDemographics)
    #orcidIdentifier = models.CharField();
    #externalIdentifiers = models.ForeignKey(ExternalPersonIdentifiers, null=True)
    # need a function to handle and store an orcid in external identifiers
    pass

# #===========================
# # researchGroups
# disabled. Getting
# CommandError: One or more models did not validate:
# hs_user_org.researchgroup: 'persons' is a manually-defined m2m relation through model GroupAssociations, which does not have foreign keys to Person and ResearchGroup

# #============================
#
# class ResearchGroup(Page, Group):
#     users = models.ManyToManyField(to=ResearchUser, through='ResearchGroupAssociations', null=True, related_name='research_groups')
#     createdBy = models.ForeignKey(ResearchUser, related_name="groups_created")
#
#
#     # def __init__(self, *args, **kwargs):
#     #     super(HydroshareGroup, self).__init__(*args, **kwargs)
#     #     self.groupType = 'hydroshare'
#
#
#     pass
#     # need to set organizationType to Hydroshare
#
# class ResearchGroupAssociations(ActivitiesModel):
#     # object to handle a person being in one or more organizations
#     hydroshareGroup = models.ForeignKey(ResearchGroup)
#     user = models.ForeignKey(ResearchUser)
#     beginDate = models.DateField(verbose_name="begin date of associate")
#     endDate = models.DateField(null=True, verbose_name="End date of association. Empty if still with organization")
#     title = models.CharField(verbose_name="Title or Responsibility", blank=True,max_length='100')
#
#     pass



############################################################
# DJANGO OPTIONS
# Goes in settings.py
############################################################
# AUTH_PROFILE_MODULE = "hs.hs_user_org.ResearchUser"
#
# ACCOUNTS_PROFILE_FORM_EXCLUDE_FIELDS = (
#     "lastUpdate",
#     "createdDate",
# )

