from copy import deepcopy
from mezzanine.pages.admin import PageAdmin
from django.contrib.gis import admin
from .models import *

admin.site.register(Person, PageAdmin)

#####
# Org
# #####
person_extra_fieldsets = ((None, {"fields": ("dob",)}),)

class PersonInline(admin.TabularInline):
    model = Person

class OrganizationAdmin(PageAdmin):
    inlines = (PersonInline,)
    fieldsets = deepcopy(PageAdmin.fieldsets) + person_extra_fieldsets

admin.site.register(Organization, OrganizationAdmin)

#######
# GeneralGroup
##############
class GeneralGroupAdmin(PageAdmin):
    inlines = (PersonInline,)
    fieldsets = deepcopy(PageAdmin.fieldsets) + person_extra_fieldsets

admin.site.register(GeneralGroup, PageAdmin) # opps abstract

#admin.site.register(ResearchUser, PageAdmin) this is a user profile

