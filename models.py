from django.contrib.contenttypes import generic
from django.contrib.auth.models import User, Group
from django.db import models
from mezzanine.pages.models import Page,Displayable, RichText
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
   |- Scholar
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




class PartyLocationModel(models.Model):
    #ID = models.AutoField(primary_key=True)
    ADDRESS_TYPE_CHOICES = (
        ("mailing", "Mailing Address. For mail. Can be a PO Box"),
    ("street", "Street Address. "),
    ("shipping","Shipping Address. Address where packages are shipped to"),
    ("office","Office Address. For a person, includes details of the office number")
    )
    address = models.TextField(verbose_name="Multi-line Address",)
    address_type = models.CharField(choices=ADDRESS_TYPE_CHOICES, verbose_name="Type of Address",max_length=24 )

    class Meta:
        abstract = True

class PartyPhoneModel(models.Model):
    PHONE_TYPE_CHOICES = (("main", "Main Line for a company"),
                            ("office", "Office Phone Number"),
                            ("cell", "Cell Phone. "),
                            ("fax", "Fax"),
                            ("other", "Other Phone Numbe"),
    )
    phone_number = models.CharField(verbose_name="Office or main phone number", blank=False,max_length='30')
    phone_type = models.CharField(choices=PHONE_TYPE_CHOICES, max_length='30')

    class Meta:
        abstract = True

class PartyEmailModel(models.Model):
    ADDRESS_TYPE_CHOICES = (("work", "Work Email"),
                            ("personal", "personal email"),
                            ("mailing_list", "email for a mailing list. Use for groups "),
                            ("support", "Support email"),
                            ("other", "Other email"),
    )
    phone_number = models.CharField(verbose_name="Office or main phone number", blank=True,max_length='30')
    phone_type = models.CharField(verbose_name="fax phone", blank=True,max_length='30')

    class Meta:
        abstract = True

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
    name = models.CharField(verbose_name="Full name of Organization or Person", blank=False,max_length='255')
    url = models.URLField(verbose_name="Web Page of Organization or Person", blank=True,max_length='255')
    # MULTIPLE Emails
    #email = models.ForeignKey(PartyEmail, null=True)
    # is a description on Page, which Person, Organization, and Group inherit from
    #description = models.TextField(verbose_name="Detailed description of Organization or Biography of a Person", blank=True)
    #primaryLocation = models.ForeignKey(PartyLocation, null=True)
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
    # name is the only required field: Science spec
    # fields from vcard.
    givenName = models.CharField(max_length='125') # given+family =name of party needs to be 255
    familyName = models.CharField(max_length='125') # given+family =name of party needs to be 255
    jobTitle = models.CharField(max_length='100')
    # This makes a full org record required.
    # Should this be just a text field?
    #organization = models.ForeignKey(Organization, null=True) # one to many
    #cellPhone = models.CharField(verbose_name="Cell Phone", blank=True,max_length='30')  # sciencebase
    #associations = models.ForeignKey(Associations, null=True) # one to many
    # do we want some adviser field.

    def __init__(self, *args, **kwargs):
        super(PersonModel, self).__init__(*args, **kwargs)
        if self.givenName is not None and self.familyName is not None:
            self.name = self.givenName + ' ' + self.familyName

    class Meta:
        abstract = True



class Person(Displayable, PersonModel):
    def __init__(self, *args, **kwargs):
        super(Person, self).__init__(*args, **kwargs)
    pass

class PersonEmail(PartyEmailModel):
    person = models.ForeignKey(to=Person, related_name="email_addresses")
    pass

class PersonLocation(PartyLocationModel):
    person = models.ForeignKey(to=Person, related_name="mail_addresses")
    pass

class PersonPhone(PartyPhoneModel):
    person = models.ForeignKey(to=Person, related_name="phone_numbers")
    pass





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

class OrganizationModel(PartyModel):
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
    logoUrl = models.ImageField(blank=True, upload_to='orgLogos')
    #smallLogoUrl = models.ImageField()
    parentOrganization = models.ForeignKey('self', null=True)
    organizationType = models.CharField(choices=ORG_TYPES_CHOICES,max_length='14')
    # externalIdentifiers from ExternalOrgIdentifiers

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        abstract = True

class Organization(Displayable, OrganizationModel):
    persons = models.ManyToManyField(Person,through="OrgAssociations", null=True,related_name="organizations")
    pass



class OrganizationEmail(PartyEmailModel):
    organization = models.ForeignKey(to=Organization, related_name="email_addresses")
    pass

class OrganizationLocation(PartyLocationModel):
    organization = models.ForeignKey(to=Organization, related_name="mail_addresses")
    pass

class OrganizationPhone(PartyPhoneModel):
    organization = models.ForeignKey(to=Organization, related_name="phone_numbers")
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




##############################################################
# HYDROSHARE SPECIFIC TYPES
# instances of User and Organziaton to implement in hydroshare
###############################################################

class ExternalIdentifiers(models.Model):

    identifierName = models.CharField(help_text="User identities from external sites",max_length='255')
    otherName = models.CharField(verbose_name="If other is selected, type of identifier", blank=True,max_length='255')
    identifierCode = models.CharField(verbose_name="Username or Identifier for site",max_length='24')
    createdDate = models.DateField(auto_now_add=True)

#=======================================
# USER Profile
#=======================================




class Scholar(models.Model):
    user = models.OneToOneField("auth.user")
    person = models.OneToOneField(Person)
    demographics = models.ForeignKey(UserDemographics, verbose_name="Demographic Properties", null=True)
    #orcidIdentifier = models.OneToOneField(ResearcherUrls,) # not sure if this will work
    #external_identifiers = models.ForeignKey(ScholarExternalIdentifiers, null=True)
    # need a function to handle and store an orcid in external identifiers
    pass

class ScholarExternalIdentifiers(ExternalIdentifiers):

    scholar = models.ForeignKey(Scholar, related_name="external_identifiers",
                               help_text="Researcher URL's, blogs, social identifiers")
    #identifierName = models.CharField(choices=IDENTIFIER_CHOICE, verbose_name="User Identities",
    #                                 help_text="User identities from external sites",max_length='255')
    #otherName = models.CharField(verbose_name="If other is selected, type of identifier", blank=True,max_length='255')
    #identifierCode = models.CharField(verbose_name="Username or Identifier for site",max_length='24')
    #createdDate = models.DateField(auto_now_add=True)
    # validation needed. if identifierName =='other' then otherName must be populated.
    def __init__(self, *args, **kwargs):
        IDENTIFIER_CHOICE = ( ("orcid", "ORCID Identifier")
                          , ("linkedin", "Linked In URL")
                          , ("VIVO", "VIVO Identifier")
                          , ("twitter", "twitterName")
                          , ("rg", "ResearchGate Username")
                          , ("mendeley", "Mendeley username")
                          , ("blog", "blog or personal page")
                          , ("ProjectPage", "page for project")
                          , ("other", "other"))
        idField = self._meta.get_field('identifierName').choices = IDENTIFIER_CHOICE
        idField.choices = IDENTIFIER_CHOICE
        idField.verbose_name="User Identities"
        idField.help_text="User identities from external sites"
        super(ScholarExternalIdentifiers, self).__init__(*args, **kwargs)

# #===========================
# # researchGroups
# disabled. Getting
# CommandError: One or more models did not validate:
# hs_user_org.researchgroup: 'persons' is a manually-defined m2m relation through model GroupAssociations, which does not have foreign keys to Person and ResearchGroup

# #============================
class ScholarGroupModel(models.Model):
    '''This is a collection of scholars that is less formal than an organization.


    '''
    # person/user left to specific implementations, since issues with model framework
    # associations are object specific
    # * general group has Persons (and subclass Scholar)
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

class ScholarGroup(Displayable,ScholarGroupModel):
    persons = models.ManyToManyField(to=Scholar,through='ScholarGroupAssociations',related_name="groups",)
    createdBy = models.OneToOneField(Scholar,related_name='creator_of')
    pass

class ScholarGroupAssociations(ActivitiesModel):
    # object to handle a person being in one or more organizations
    group = models.ForeignKey(ScholarGroup)
    scholar = models.ForeignKey(Scholar)
    beginDate = models.DateField(verbose_name="begin date of associate")
    endDate = models.DateField(null=True, verbose_name="End date of association. Empty if still with organization")
    title = models.CharField(verbose_name="Title or Responsibility", blank=True,max_length='100')

    pass
# class ResearchGroup(Page, Group):
#     users = models.ManyToManyField(to=Scholar, through='ResearchGroupAssociations', null=True, related_name='research_groups')
#     createdBy = models.ForeignKey(Scholar, related_name="groups_created")
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
#     user = models.ForeignKey(Scholar)
#     beginDate = models.DateField(verbose_name="begin date of associate")
#     endDate = models.DateField(null=True, verbose_name="End date of association. Empty if still with organization")
#     title = models.CharField(verbose_name="Title or Responsibility", blank=True,max_length='100')
#
#     pass



############################################################
# DJANGO OPTIONS
# Goes in settings.py
############################################################
# AUTH_PROFILE_MODULE = "hs.hs_user_org.Scholar"
#
# ACCOUNTS_PROFILE_FORM_EXCLUDE_FIELDS = (
#     "lastUpdate",
#     "createdDate",
# )

