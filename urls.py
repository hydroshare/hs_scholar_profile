from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

from . import api, views

urlpatterns = patterns('',
    url(r'^organizations/', views.OrganizationList.as_view(), name="OrganizationList"),
    url(r'^people/', views.PersonList.as_view(), name="PersonList"),
    #url(r'^scholar/', api.scholar.urls),
    url(r'^scholargroups/', views.ScholarGroupList.as_view(), name='ScholarGroupList'),
    )

urlpatterns += patterns('',
    url(r'^person/(?P<pk>\d+)/$', views.PersonDetail.as_view(), name="PersonDetail"),
    url(r'^organization/(?P<pk>\d+)/$', views.OrganizationDetail.as_view(), name="OrganizationDetail"),
    url(r'^scholargroup/(?P<pk>\d+)/$', views.ScholarGroupDetail.as_view(), name="ScholarGroupDetail"),
    )