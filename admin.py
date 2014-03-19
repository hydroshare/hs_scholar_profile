from copy import deepcopy
#from mezzanine.pages.admin import PageAdmin
from mezzanine.core.admin import DisplayableAdmin, TabularDynamicInlineAdmin
from django.contrib import admin
from django.contrib.admin import ModelAdmin
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


class OrgAssociationInline(TabularDynamicInlineAdmin):
    model = Organization.persons.through
    extra = 1
    inlines = (OrgInline)

class OrganizationAdmin( ModelAdmin):
    model = Organization
    inlines = (OrgAssociationInline,)
    #exclude = ('persons',)
    #fieldsets = deepcopy(PageAdmin.fieldsets) #+ person_extra_fieldsets

class PersonAdmin(ModelAdmin):
    model = Person
    #inlines = (OrgAssociationInline, OrgInline)
    pass

admin.site.register(Organization, OrganizationAdmin)

admin.site.register(Person, PersonAdmin)

#######
# ScholarlGroup
##############

class ScholarAssociationInline(TabularDynamicInlineAdmin):
    model = ScholarGroup.persons.through


class ScholarGroupAdmin(ModelAdmin):
    model = ScholarGroup
    inlines = (ScholarAssociationInline,)
    #fieldsets = deepcopy(PageAdmin.fieldsets) #+ person_extra_fieldsets

admin.site.register(ScholarGroup, ScholarGroupAdmin) # opps abstract


admin.site.register(Scholar, DisplayableAdmin) #this is a user profile


