from copy import deepcopy
from mezzanine.pages.admin import PageAdmin
from mezzanine.core.admin import DisplayableAdmin, TabularDynamicInlineAdmin, OwnableAdmin
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from django.forms import ModelForm
from .models import *



class PersonInline(admin.TabularInline):
    model = Person


#####
# Org
# #####
#person_extra_fieldsets = ((None, {"fields": ("dob",)}),)

class OrgInline (admin.TabularInline):
    model = Organization
    list_display = ('name',"organizationType")


# class OrgAssociationInline(TabularDynamicInlineAdmin):
#     model = Organization.persons.through
#     extra = 1
#     inlines = (OrgInline)

#class OrganizationAdmin( ModelAdmin):
class OrganizationAdmin(DisplayableAdmin):
    model = Organization
    #inlines = (OrgAssociationInline,)
    list_display = ("id","name","organizationType","parentOrganization","url",)
    list_display_links = ("id",)
    list_editable = ("name","organizationType","parentOrganization","url")
    ordering = ("organizationType","name",)
    fieldsets = (
        (None, {
            "fields": ("name","organizationType","parentOrganization","url"),
                }),
    )
    #exclude = ('persons',)
    #fieldsets = deepcopy(PageAdmin.fieldsets) #+ person_extra_fieldsets

class PersonAssociationInline(TabularDynamicInlineAdmin):
    model = Person.organizations.through
    extra = 1
    inlines = (OrgInline)

class PersonAdmin(DisplayableAdmin):
    model = Person
    inlines = (PersonAssociationInline,)# OrgInline)
    list_display = ("id","name","familyName","givenName","jobTitle",)
    list_display_links = ("id",)
    list_editable = ("givenName","familyName","name","jobTitle",)
    ordering = ("familyName","givenName",)
    fieldsets = (
        (None, {
            "fields": ("givenName","familyName","name","jobTitle",),
                }),
    )
    #filter_horizontal = ('organizations',)
    pass

admin.site.register(Organization, OrganizationAdmin)

admin.site.register(Person, PersonAdmin)

#######
# ScholarlGroup
##############
# class ScholarGroupInline (admin.TabularInline):
#     model = ScholarGroup
#
# class ScholarAssociationInline(TabularDynamicInlineAdmin):
#     model = ScholarGroup.scholars.through
#     inlines = (ScholarGroupInline,)
#

class ScholarGroupAdmin(ModelAdmin):
    model = ScholarGroup
#    inlines = (ScholarAssociationInline,)
    #fieldsets = deepcopy(PageAdmin.fieldsets) #+ person_extra_fieldsets
#
# class ScholarGroupInline (admin.TabularInline):
#     model = ScholarGroup

admin.site.register(ScholarGroup, ScholarGroupAdmin)


# user Profile
# depreciated in django 1,7 used by mezz: AUTH_PROFILE_MODULE = "hs_user_org.Scholar"
# When tried,
#     django.core.exceptions.ImproperlyConfigured:
#    'ScholarAdmin.filter_horizontal' refers to field 'groups' that is missing from model 'hs_user_org.Scholar'.

# class ScholarProfileInline (admin.StackedInline):
#     model = Scholar
#
# class ScholarDemographicsInline (admin.StackedInline):
#     model = UserDemographics
#
# class AuthGroupInline(ModelAdmin):
#     model = Group
#     pass
#
# class ScholarAdmin(UserAdmin):
#     inlines = (ScholarProfileInline,ScholarDemographicsInline,AuthGroupInline)
#     #exclude = ('groups',)
#
# admin.site.unregister(User)
# admin.site.register(Scholar, ScholarAdmin) #this is a user profile

# PROFILE VERSION
# class ScholarDemographicsInline (admin.StackedInline):
#     model = UserDemographics
#
# class AuthGroupInline(ModelAdmin):
#     model = Group
#     pass
#
# class ScholarAdmin(UserAdmin):
#     inlines = (ScholarDemographicsInline,)
#     #exclude = ('groups',)
# admin.site.register(Scholar, ScholarAdmin)


