from django.contrib.contenttypes import generic
from django.contrib.auth.models import User, Group
from django.db import models
from mezzanine.pages.models import Page, RichText
from ga_resources.models import PagePermissionsMixin
# from dublincore.models import QualifiedDublinCoreElement

class AbstractResource(models.Model, PagePermissionsMixin):
    """
    All hydroshare objects inherit from this mixin.  It defines things that must
    be present to be considered a hydroshare resource.  Additionally, all 
    hydroshare resources should inherit from Page.  This gives them what they
    need to be represented in the Mezzanine CMS.  

    In some cases, it is possible that the order of inheritence matters.  Best
    practice dictates that you list pages.Page first and then other classes:

        class MyResourceContentType(pages.Page, hs_core.AbstractResource):
            ...
    """
    public = models.BooleanField(
        help_text='If this is true, the resource is viewable and downloadable by anyone',
        default=True
    )
    owner = models.OneToOneField(
        User,
        help_text='The person who uploaded the resource'
    )
    frozen = models.BooleanField(
        help_text='If this is true, the resource should not be modified',
        default=False
    )
    do_not_distribute = models.BooleanField(
        help_text='If this is true, the resource owner has to designate viewers',
        default=True
    )
    dublin_metadata = generic.GenericRelation(
        'dublincore.QualifiedDublinCoreElement',
        help_text='The dublin core metadata of the resource'
    )

    class Meta: 
        abstract = True
 
class GenericResource(Page, RichText, AbstractResource):
    resource_file = models.FileField(
        help_text='This should be a Bagit file containing the resource itself',
        upload_to='generic_resources',
        blank=True, 
        null=True
    )
    resource_url = models.URLField(
        blank=True, 
        null=True
    )

    class Meta:
        verbose_name = 'Generic Hydroshare Resource'
