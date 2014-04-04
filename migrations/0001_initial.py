# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'City'
        db.create_table(u'hs_scholar_profile_city', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('geonamesUrl', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'hs_scholar_profile', ['City'])

        # Adding model 'Region'
        db.create_table(u'hs_scholar_profile_region', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('geonamesUrl', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'hs_scholar_profile', ['Region'])

        # Adding model 'Country'
        db.create_table(u'hs_scholar_profile_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('geonamesUrl', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'hs_scholar_profile', ['Country'])

        # Adding model 'Organization'
        db.create_table(u'hs_scholar_profile_organization', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            (u'keywords_string', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True)),
            ('_meta_title', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('gen_description', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('publish_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('expiry_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('short_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('in_sitemap', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('uniqueCode', self.gf('django.db.models.fields.CharField')(max_length='255')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='255')),
            ('url', self.gf('django.db.models.fields.URLField')(max_length='255', blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('createdDate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('lastUpdate', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('logoUrl', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('parentOrganization', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hs_scholar_profile.Organization'], null=True, blank=True)),
            ('organizationType', self.gf('django.db.models.fields.CharField')(max_length='14')),
        ))
        db.send_create_signal(u'hs_scholar_profile', ['Organization'])

        # Adding model 'Person'
        db.create_table(u'hs_scholar_profile_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            (u'keywords_string', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True)),
            ('_meta_title', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('gen_description', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('publish_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('expiry_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('short_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('in_sitemap', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('uniqueCode', self.gf('django.db.models.fields.CharField')(max_length='255')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='255')),
            ('url', self.gf('django.db.models.fields.URLField')(max_length='255', blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('createdDate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('lastUpdate', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('givenName', self.gf('django.db.models.fields.CharField')(max_length='125')),
            ('familyName', self.gf('django.db.models.fields.CharField')(max_length='125')),
            ('jobTitle', self.gf('django.db.models.fields.CharField')(max_length='100', blank=True)),
        ))
        db.send_create_signal(u'hs_scholar_profile', ['Person'])

        # Adding model 'PersonEmail'
        db.create_table(u'hs_scholar_profile_personemail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length='30', blank=True)),
            ('phone_type', self.gf('django.db.models.fields.CharField')(max_length='30', blank=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='email_addresses', null=True, to=orm['hs_scholar_profile.Person'])),
        ))
        db.send_create_signal(u'hs_scholar_profile', ['PersonEmail'])

        # Adding model 'PersonLocation'
        db.create_table(u'hs_scholar_profile_personlocation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('address_type', self.gf('django.db.models.fields.CharField')(max_length=24)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='mail_addresses', null=True, to=orm['hs_scholar_profile.Person'])),
        ))
        db.send_create_signal(u'hs_scholar_profile', ['PersonLocation'])

        # Adding model 'PersonPhone'
        db.create_table(u'hs_scholar_profile_personphone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length='30')),
            ('phone_type', self.gf('django.db.models.fields.CharField')(max_length='30')),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='phone_numbers', null=True, to=orm['hs_scholar_profile.Person'])),
        ))
        db.send_create_signal(u'hs_scholar_profile', ['PersonPhone'])

        # Adding model 'UserKeywords'
        db.create_table(u'hs_scholar_profile_userkeywords', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(related_name='keywords', to=orm['hs_scholar_profile.Person'])),
            ('keyword', self.gf('django.db.models.fields.CharField')(max_length='100')),
            ('createdDate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'hs_scholar_profile', ['UserKeywords'])

        # Adding model 'UserDemographics'
        db.create_table(u'hs_scholar_profile_userdemographics', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('public', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('userType', self.gf('django.db.models.fields.CharField')(max_length='255')),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hs_scholar_profile.City'], null=True, blank=True)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hs_scholar_profile.Region'], null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hs_scholar_profile.Country'], null=True, blank=True)),
        ))
        db.send_create_signal(u'hs_scholar_profile', ['UserDemographics'])

        # Adding model 'OtherNames'
        db.create_table(u'hs_scholar_profile_othernames', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('persons', self.gf('django.db.models.fields.related.ForeignKey')(related_name='otherNames', to=orm['hs_scholar_profile.Person'])),
            ('otherName', self.gf('django.db.models.fields.CharField')(max_length='255')),
            ('annotation', self.gf('django.db.models.fields.CharField')(default='citation', max_length='10')),
        ))
        db.send_create_signal(u'hs_scholar_profile', ['OtherNames'])

        # Adding model 'OrganizationEmail'
        db.create_table(u'hs_scholar_profile_organizationemail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length='30', blank=True)),
            ('phone_type', self.gf('django.db.models.fields.CharField')(max_length='30', blank=True)),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(related_name='email_addresses', to=orm['hs_scholar_profile.Organization'])),
        ))
        db.send_create_signal(u'hs_scholar_profile', ['OrganizationEmail'])

        # Adding model 'OrganizationLocation'
        db.create_table(u'hs_scholar_profile_organizationlocation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('address_type', self.gf('django.db.models.fields.CharField')(max_length=24)),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(related_name='mail_addresses', to=orm['hs_scholar_profile.Organization'])),
        ))
        db.send_create_signal(u'hs_scholar_profile', ['OrganizationLocation'])

        # Adding model 'OrganizationPhone'
        db.create_table(u'hs_scholar_profile_organizationphone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length='30')),
            ('phone_type', self.gf('django.db.models.fields.CharField')(max_length='30')),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(related_name='phone_numbers', to=orm['hs_scholar_profile.Organization'])),
        ))
        db.send_create_signal(u'hs_scholar_profile', ['OrganizationPhone'])

        # Adding model 'ExternalOrgIdentifiers'
        db.create_table(u'hs_scholar_profile_externalorgidentifiers', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(related_name='externalIdentifiers', to=orm['hs_scholar_profile.Organization'])),
            ('identifierName', self.gf('django.db.models.fields.CharField')(max_length='10')),
            ('otherName', self.gf('django.db.models.fields.CharField')(max_length='255', blank=True)),
            ('identifierCode', self.gf('django.db.models.fields.CharField')(max_length='255')),
            ('createdDate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'hs_scholar_profile', ['ExternalOrgIdentifiers'])

        # Adding model 'OrgAssociations'
        db.create_table(u'hs_scholar_profile_orgassociations', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('createdDate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hs_scholar_profile.Organization'])),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hs_scholar_profile.Person'])),
            ('beginDate', self.gf('django.db.models.fields.DateField')()),
            ('endDate', self.gf('django.db.models.fields.DateField')(null=True)),
            ('jobTitle', self.gf('django.db.models.fields.CharField')(max_length='100', blank=True)),
            ('presentOrganization', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'hs_scholar_profile', ['OrgAssociations'])

        # Adding model 'ExternalIdentifiers'
        db.create_table(u'hs_scholar_profile_externalidentifiers', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('identifierName', self.gf('django.db.models.fields.CharField')(max_length='255')),
            ('otherName', self.gf('django.db.models.fields.CharField')(max_length='255', blank=True)),
            ('identifierCode', self.gf('django.db.models.fields.CharField')(max_length='24')),
            ('createdDate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'hs_scholar_profile', ['ExternalIdentifiers'])

        # Adding model 'Scholar'
        db.create_table(u'hs_scholar_profile_scholar', (
            (u'person_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['hs_scholar_profile.Person'], unique=True, primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('demographics', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hs_scholar_profile.UserDemographics'], null=True, blank=True)),
        ))
        db.send_create_signal(u'hs_scholar_profile', ['Scholar'])

        # Adding model 'ScholarExternalIdentifiers'
        db.create_table(u'hs_scholar_profile_scholarexternalidentifiers', (
            (u'externalidentifiers_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['hs_scholar_profile.ExternalIdentifiers'], unique=True, primary_key=True)),
            ('scholar', self.gf('django.db.models.fields.related.ForeignKey')(related_name='external_identifiers', to=orm['hs_scholar_profile.Scholar'])),
        ))
        db.send_create_signal(u'hs_scholar_profile', ['ScholarExternalIdentifiers'])

        # Adding model 'ScholarGroup'
        db.create_table(u'hs_scholar_profile_scholargroup', (
            (u'group_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.Group'], unique=True, primary_key=True)),
            (u'keywords_string', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True)),
            ('_meta_title', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('gen_description', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('publish_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('expiry_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('short_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('in_sitemap', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('groupDescription', self.gf('django.db.models.fields.TextField')()),
            ('purpose', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('createdDate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('createdBy', self.gf('django.db.models.fields.related.OneToOneField')(related_name='creator_of', unique=True, to=orm['hs_scholar_profile.Scholar'])),
        ))
        db.send_create_signal(u'hs_scholar_profile', ['ScholarGroup'])


    def backwards(self, orm):
        # Deleting model 'City'
        db.delete_table(u'hs_scholar_profile_city')

        # Deleting model 'Region'
        db.delete_table(u'hs_scholar_profile_region')

        # Deleting model 'Country'
        db.delete_table(u'hs_scholar_profile_country')

        # Deleting model 'Organization'
        db.delete_table(u'hs_scholar_profile_organization')

        # Deleting model 'Person'
        db.delete_table(u'hs_scholar_profile_person')

        # Deleting model 'PersonEmail'
        db.delete_table(u'hs_scholar_profile_personemail')

        # Deleting model 'PersonLocation'
        db.delete_table(u'hs_scholar_profile_personlocation')

        # Deleting model 'PersonPhone'
        db.delete_table(u'hs_scholar_profile_personphone')

        # Deleting model 'UserKeywords'
        db.delete_table(u'hs_scholar_profile_userkeywords')

        # Deleting model 'UserDemographics'
        db.delete_table(u'hs_scholar_profile_userdemographics')

        # Deleting model 'OtherNames'
        db.delete_table(u'hs_scholar_profile_othernames')

        # Deleting model 'OrganizationEmail'
        db.delete_table(u'hs_scholar_profile_organizationemail')

        # Deleting model 'OrganizationLocation'
        db.delete_table(u'hs_scholar_profile_organizationlocation')

        # Deleting model 'OrganizationPhone'
        db.delete_table(u'hs_scholar_profile_organizationphone')

        # Deleting model 'ExternalOrgIdentifiers'
        db.delete_table(u'hs_scholar_profile_externalorgidentifiers')

        # Deleting model 'OrgAssociations'
        db.delete_table(u'hs_scholar_profile_orgassociations')

        # Deleting model 'ExternalIdentifiers'
        db.delete_table(u'hs_scholar_profile_externalidentifiers')

        # Deleting model 'Scholar'
        db.delete_table(u'hs_scholar_profile_scholar')

        # Deleting model 'ScholarExternalIdentifiers'
        db.delete_table(u'hs_scholar_profile_scholarexternalidentifiers')

        # Deleting model 'ScholarGroup'
        db.delete_table(u'hs_scholar_profile_scholargroup')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'hs_scholar_profile.city': {
            'Meta': {'object_name': 'City'},
            'geonamesUrl': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'hs_scholar_profile.country': {
            'Meta': {'object_name': 'Country'},
            'geonamesUrl': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'hs_scholar_profile.externalidentifiers': {
            'Meta': {'object_name': 'ExternalIdentifiers'},
            'createdDate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifierCode': ('django.db.models.fields.CharField', [], {'max_length': "'24'"}),
            'identifierName': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'otherName': ('django.db.models.fields.CharField', [], {'max_length': "'255'", 'blank': 'True'})
        },
        u'hs_scholar_profile.externalorgidentifiers': {
            'Meta': {'object_name': 'ExternalOrgIdentifiers'},
            'createdDate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifierCode': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'identifierName': ('django.db.models.fields.CharField', [], {'max_length': "'10'"}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'externalIdentifiers'", 'to': u"orm['hs_scholar_profile.Organization']"}),
            'otherName': ('django.db.models.fields.CharField', [], {'max_length': "'255'", 'blank': 'True'})
        },
        u'hs_scholar_profile.organization': {
            'Meta': {'object_name': 'Organization'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'createdDate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'lastUpdate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'logoUrl': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'organizationType': ('django.db.models.fields.CharField', [], {'max_length': "'14'"}),
            'parentOrganization': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hs_scholar_profile.Organization']", 'null': 'True', 'blank': 'True'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'uniqueCode': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': "'255'", 'blank': 'True'})
        },
        u'hs_scholar_profile.organizationemail': {
            'Meta': {'object_name': 'OrganizationEmail'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'email_addresses'", 'to': u"orm['hs_scholar_profile.Organization']"}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': "'30'", 'blank': 'True'}),
            'phone_type': ('django.db.models.fields.CharField', [], {'max_length': "'30'", 'blank': 'True'})
        },
        u'hs_scholar_profile.organizationlocation': {
            'Meta': {'object_name': 'OrganizationLocation'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'address_type': ('django.db.models.fields.CharField', [], {'max_length': '24'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mail_addresses'", 'to': u"orm['hs_scholar_profile.Organization']"})
        },
        u'hs_scholar_profile.organizationphone': {
            'Meta': {'object_name': 'OrganizationPhone'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'phone_numbers'", 'to': u"orm['hs_scholar_profile.Organization']"}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': "'30'"}),
            'phone_type': ('django.db.models.fields.CharField', [], {'max_length': "'30'"})
        },
        u'hs_scholar_profile.orgassociations': {
            'Meta': {'object_name': 'OrgAssociations'},
            'beginDate': ('django.db.models.fields.DateField', [], {}),
            'createdDate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'endDate': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jobTitle': ('django.db.models.fields.CharField', [], {'max_length': "'100'", 'blank': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hs_scholar_profile.Organization']"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hs_scholar_profile.Person']"}),
            'presentOrganization': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'hs_scholar_profile.othernames': {
            'Meta': {'object_name': 'OtherNames'},
            'annotation': ('django.db.models.fields.CharField', [], {'default': "'citation'", 'max_length': "'10'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otherName': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'persons': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'otherNames'", 'to': u"orm['hs_scholar_profile.Person']"})
        },
        u'hs_scholar_profile.person': {
            'Meta': {'object_name': 'Person'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'createdDate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'familyName': ('django.db.models.fields.CharField', [], {'max_length': "'125'"}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'givenName': ('django.db.models.fields.CharField', [], {'max_length': "'125'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'jobTitle': ('django.db.models.fields.CharField', [], {'max_length': "'100'", 'blank': 'True'}),
            u'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'lastUpdate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'organizations': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'hs_scholar_profile_person_members'", 'null': 'True', 'through': u"orm['hs_scholar_profile.OrgAssociations']", 'to': u"orm['hs_scholar_profile.Organization']"}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'uniqueCode': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': "'255'", 'blank': 'True'})
        },
        u'hs_scholar_profile.personemail': {
            'Meta': {'object_name': 'PersonEmail'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'email_addresses'", 'null': 'True', 'to': u"orm['hs_scholar_profile.Person']"}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': "'30'", 'blank': 'True'}),
            'phone_type': ('django.db.models.fields.CharField', [], {'max_length': "'30'", 'blank': 'True'})
        },
        u'hs_scholar_profile.personlocation': {
            'Meta': {'object_name': 'PersonLocation'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'address_type': ('django.db.models.fields.CharField', [], {'max_length': '24'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'mail_addresses'", 'null': 'True', 'to': u"orm['hs_scholar_profile.Person']"})
        },
        u'hs_scholar_profile.personphone': {
            'Meta': {'object_name': 'PersonPhone'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'phone_numbers'", 'null': 'True', 'to': u"orm['hs_scholar_profile.Person']"}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': "'30'"}),
            'phone_type': ('django.db.models.fields.CharField', [], {'max_length': "'30'"})
        },
        u'hs_scholar_profile.region': {
            'Meta': {'object_name': 'Region'},
            'geonamesUrl': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'hs_scholar_profile.scholar': {
            'Meta': {'object_name': 'Scholar', '_ormbases': [u'hs_scholar_profile.Person']},
            'demographics': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hs_scholar_profile.UserDemographics']", 'null': 'True', 'blank': 'True'}),
            u'person_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['hs_scholar_profile.Person']", 'unique': 'True', 'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'hs_scholar_profile.scholarexternalidentifiers': {
            'Meta': {'object_name': 'ScholarExternalIdentifiers', '_ormbases': [u'hs_scholar_profile.ExternalIdentifiers']},
            u'externalidentifiers_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['hs_scholar_profile.ExternalIdentifiers']", 'unique': 'True', 'primary_key': 'True'}),
            'scholar': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'external_identifiers'", 'to': u"orm['hs_scholar_profile.Scholar']"})
        },
        u'hs_scholar_profile.scholargroup': {
            'Meta': {'object_name': 'ScholarGroup', '_ormbases': [u'auth.Group']},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'createdBy': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'creator_of'", 'unique': 'True', 'to': u"orm['hs_scholar_profile.Scholar']"}),
            'createdDate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'groupDescription': ('django.db.models.fields.TextField', [], {}),
            u'group_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.Group']", 'unique': 'True', 'primary_key': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'purpose': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        u'hs_scholar_profile.userdemographics': {
            'Meta': {'object_name': 'UserDemographics'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hs_scholar_profile.City']", 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hs_scholar_profile.Country']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hs_scholar_profile.Region']", 'null': 'True', 'blank': 'True'}),
            'userType': ('django.db.models.fields.CharField', [], {'max_length': "'255'"})
        },
        u'hs_scholar_profile.userkeywords': {
            'Meta': {'object_name': 'UserKeywords'},
            'createdDate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyword': ('django.db.models.fields.CharField', [], {'max_length': "'100'"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'keywords'", 'to': u"orm['hs_scholar_profile.Person']"})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['hs_scholar_profile']