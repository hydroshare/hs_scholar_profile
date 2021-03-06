hs_scholar_profile
===============

Django Mezzanine application to handle user profile information for the Hydroshare project.

This adds a model for

Party
|- Organization
|- Person
|- Scholar (user profile)

Adds ScholarGroup which is a DJango group with  additional properties

Other properties:
    * email
    * address
    * external identifiers

Party is the top level object. Organization and Person can have multiple email, regular mail addresses, and external

Scholar add a user profiles that is a person, that has a user demographics objects.

Thre is an associaton between Organizaitons and People with properties.
Organization              People
          |                 |
        OrganizationAssociation
            beginDate
            endDate
            jobTitle
            presentOrganization(still with organizaiton)

===
h1. URL's
The above entities are acessible at the following URL's (if the config below is followed).

Lists
    /party/organizaitons
    /party/people/
    /party/scholargroups/

Details
    /party/person/(id)
    /party/organization/(id)
    /party/scholargroups/(id)

Scholars are users.

==========
Add the following to enable this applicaiton

settings.py

    INSTALLED_APPS += (hs_scholar_profile,)
    AUTH_PROFILE_MODULE = "hs_scholar_profile.Scholar"

urls.py
    urlpatterns += i18n_patterns("",
        url('^party/', include('hs.hs_user_org.urls')),
    )

 