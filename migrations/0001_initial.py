# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'City'
        db.create_table(u'hs_user_org_city', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('geonamesUrl', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'hs_user_org', ['City'])

        # Adding model 'Region'
        db.create_table(u'hs_user_org_region', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('geonamesUrl', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'hs_user_org', ['Region'])

        # Adding model 'Country'
        db.create_table(u'hs_user_org_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('geonamesUrl', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'hs_user_org', ['Country'])

        # Adding model 'Person'
        db.create_table(u'hs_user_org_person', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pages.Page'], unique=True, primary_key=True)),
            ('uniqueCode', self.gf('django.db.models.fields.CharField')(max_length='255')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='255')),
            ('url', self.gf('django.db.models.fields.URLField')(max_length='255', blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('createdDate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('lastUpdate', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('givenName', self.gf('django.db.models.fields.CharField')(max_length='125')),
            ('familyName', self.gf('django.db.models.fields.CharField')(max_length='125')),
            ('jobTitle', self.gf('django.db.models.fields.CharField')(max_length='100')),
        ))
        db.send_create_signal(u'hs_user_org', ['Person'])

        # Adding model 'PersonEmail'
        db.create_table(u'hs_user_org_personemail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length='30', blank=True)),
            ('phone_type', self.gf('django.db.models.fields.CharField')(max_length='30', blank=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(related_name='email_addresses', to=orm['hs_user_org.Person'])),
        ))
        db.send_create_signal(u'hs_user_org', ['PersonEmail'])

        # Adding model 'PersonLocation'
        db.create_table(u'hs_user_org_personlocation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('address_type', self.gf('django.db.models.fields.CharField')(max_length=24)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(related_name='mail_addresses', to=orm['hs_user_org.Person'])),
        ))
        db.send_create_signal(u'hs_user_org', ['PersonLocation'])

        # Adding model 'PersonPhone'
        db.create_table(u'hs_user_org_personphone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length='30')),
            ('phone_type', self.gf('django.db.models.fields.CharField')(max_length='30')),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(related_name='phone_numbers', to=orm['hs_user_org.Person'])),
        ))
        db.send_create_signal(u'hs_user_org', ['PersonPhone'])

        # Adding model 'UserKeywords'
        db.create_table(u'hs_user_org_userkeywords', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(related_name='keywords', to=orm['hs_user_org.Person'])),
            ('keyword', self.gf('django.db.models.fields.CharField')(max_length='100')),
            ('createdDate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'hs_user_org', ['UserKeywords'])

        # Adding model 'UserDemographics'
        db.create_table(u'hs_user_org_userdemographics', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('public', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('userType', self.gf('django.db.models.fields.CharField')(max_length='255')),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hs_user_org.City'], null=True)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hs_user_org.Region'], null=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hs_user_org.Country'], null=True)),
        ))
        db.send_create_signal(u'hs_user_org', ['UserDemographics'])

        # Adding model 'OtherNames'
        db.create_table(u'hs_user_org_othernames', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('persons', self.gf('django.db.models.fields.related.ForeignKey')(related_name='otherNames', to=orm['hs_user_org.Person'])),
            ('otherName', self.gf('django.db.models.fields.CharField')(max_length='255')),
            ('annotation', self.gf('django.db.models.fields.CharField')(default='citation', max_length='10')),
        ))
        db.send_create_signal(u'hs_user_org', ['OtherNames'])

        # Adding model 'Organization'
        db.create_table(u'hs_user_org_organization', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pages.Page'], unique=True, primary_key=True)),
            ('uniqueCode', self.gf('django.db.models.fields.CharField')(max_length='255')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='255')),
            ('url', self.gf('django.db.models.fields.URLField')(max_length='255', blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('createdDate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('lastUpdate', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('logoUrl', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('parentOrganization', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hs_user_org.Organization'], null=True)),
            ('organizationType', self.gf('django.db.models.fields.CharField')(max_length='14')),
        ))
        db.send_create_signal(u'hs_user_org', ['Organization'])

        # Adding model 'OrganizationEmail'
        db.create_table(u'hs_user_org_organizationemail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length='30', blank=True)),
            ('phone_type', self.gf('django.db.models.fields.CharField')(max_length='30', blank=True)),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(related_name='email_addresses', to=orm['hs_user_org.Organization'])),
        ))
        db.send_create_signal(u'hs_user_org', ['OrganizationEmail'])

        # Adding model 'OrganizationLocation'
        db.create_table(u'hs_user_org_organizationlocation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('address_type', self.gf('django.db.models.fields.CharField')(max_length=24)),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(related_name='mail_addresses', to=orm['hs_user_org.Organization'])),
        ))
        db.send_create_signal(u'hs_user_org', ['OrganizationLocation'])

        # Adding model 'OrganizationPhone'
        db.create_table(u'hs_user_org_organizationphone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length='30')),
            ('phone_type', self.gf('django.db.models.fields.CharField')(max_length='30')),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(related_name='phone_numbers', to=orm['hs_user_org.Organization'])),
        ))
        db.send_create_signal(u'hs_user_org', ['OrganizationPhone'])

        # Adding model 'ExternalOrgIdentifiers'
        db.create_table(u'hs_user_org_externalorgidentifiers', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(related_name='externalIdentifiers', to=orm['hs_user_org.Organization'])),
            ('identifierName', self.gf('django.db.models.fields.CharField')(max_length='10')),
            ('otherName', self.gf('django.db.models.fields.CharField')(max_length='255', blank=True)),
            ('identifierCode', self.gf('django.db.models.fields.CharField')(max_length='255')),
            ('createdDate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'hs_user_org', ['ExternalOrgIdentifiers'])

        # Adding model 'OrgAssociations'
        db.create_table(u'hs_user_org_orgassociations', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('createdDate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hs_user_org.Organization'])),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hs_user_org.Person'])),
            ('beginDate', self.gf('django.db.models.fields.DateField')()),
            ('endDate', self.gf('django.db.models.fields.DateField')(null=True)),
            ('jobTitle', self.gf('django.db.models.fields.CharField')(max_length='100', blank=True)),
            ('presentOrganization', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'hs_user_org', ['OrgAssociations'])

        # Adding model 'ExternalIdentifiers'
        db.create_table(u'hs_user_org_externalidentifiers', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('identifierName', self.gf('django.db.models.fields.CharField')(max_length='255')),
            ('otherName', self.gf('django.db.models.fields.CharField')(max_length='255', blank=True)),
            ('identifierCode', self.gf('django.db.models.fields.CharField')(max_length='24')),
            ('createdDate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'hs_user_org', ['ExternalIdentifiers'])

        # Adding model 'Scholar'
        db.create_table(u'hs_user_org_scholar', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('person', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['hs_user_org.Person'], unique=True)),
            ('demographics', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hs_user_org.UserDemographics'], null=True)),
        ))
        db.send_create_signal(u'hs_user_org', ['Scholar'])

        # Adding model 'ScholarExternalIdentifiers'
        db.create_table(u'hs_user_org_scholarexternalidentifiers', (
            (u'externalidentifiers_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['hs_user_org.ExternalIdentifiers'], unique=True, primary_key=True)),
            ('scholar', self.gf('django.db.models.fields.related.ForeignKey')(related_name='external_identifiers', to=orm['hs_user_org.Scholar'])),
        ))
        db.send_create_signal(u'hs_user_org', ['ScholarExternalIdentifiers'])

        # Adding model 'ScholarGroup'
        db.create_table(u'hs_user_org_scholargroup', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pages.Page'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='100')),
            ('groupDescription', self.gf('django.db.models.fields.TextField')()),
            ('purpose', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('createdDate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('createdBy', self.gf('django.db.models.fields.related.OneToOneField')(related_name='creator_of', unique=True, to=orm['hs_user_org.Scholar'])),
        ))
        db.send_create_signal(u'hs_user_org', ['ScholarGroup'])

        # Adding model 'ScholarGroupAssociations'
        db.create_table(u'hs_user_org_scholargroupassociations', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('createdDate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hs_user_org.ScholarGroup'])),
            ('scholar', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hs_user_org.Scholar'])),
            ('beginDate', self.gf('django.db.models.fields.DateField')()),
            ('endDate', self.gf('django.db.models.fields.DateField')(null=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length='100', blank=True)),
        ))
        db.send_create_signal(u'hs_user_org', ['ScholarGroupAssociations'])


    def backwards(self, orm):
        # Deleting model 'City'
        db.delete_table(u'hs_user_org_city')

        # Deleting model 'Region'
        db.delete_table(u'hs_user_org_region')

        # Deleting model 'Country'
        db.delete_table(u'hs_user_org_country')

        # Deleting model 'Person'
        db.delete_table(u'hs_user_org_person')

        # Deleting model 'PersonEmail'
        db.delete_table(u'hs_user_org_personemail')

        # Deleting model 'PersonLocation'
        db.delete_table(u'hs_user_org_personlocation')

        # Deleting model 'PersonPhone'
        db.delete_table(u'hs_user_org_personphone')

        # Deleting model 'UserKeywords'
        db.delete_table(u'hs_user_org_userkeywords')

        # Deleting model 'UserDemographics'
        db.delete_table(u'hs_user_org_userdemographics')

        # Deleting model 'OtherNames'
        db.delete_table(u'hs_user_org_othernames')

        # Deleting model 'Organization'
        db.delete_table(u'hs_user_org_organization')

        # Deleting model 'OrganizationEmail'
        db.delete_table(u'hs_user_org_organizationemail')

        # Deleting model 'OrganizationLocation'
        db.delete_table(u'hs_user_org_organizationlocation')

        # Deleting model 'OrganizationPhone'
        db.delete_table(u'hs_user_org_organizationphone')

        # Deleting model 'ExternalOrgIdentifiers'
        db.delete_table(u'hs_user_org_externalorgidentifiers')

        # Deleting model 'OrgAssociations'
        db.delete_table(u'hs_user_org_orgassociations')

        # Deleting model 'ExternalIdentifiers'
        db.delete_table(u'hs_user_org_externalidentifiers')

        # Deleting model 'Scholar'
        db.delete_table(u'hs_user_org_scholar')

        # Deleting model 'ScholarExternalIdentifiers'
        db.delete_table(u'hs_user_org_scholarexternalidentifiers')

        # Deleting model 'ScholarGroup'
        db.delete_table(u'hs_user_org_scholargroup')

        # Deleting model 'ScholarGroupAssociations'
        db.delete_table(u'hs_user_org_scholargroupassociations')


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
        u'hs_user_org.city': {
            'Meta': {'object_name': 'City'},
            'geonamesUrl': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'hs_user_org.country': {
            'Meta': {'object_name': 'Country'},
            'geonamesUrl': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'hs_user_org.externalidentifiers': {
            'Meta': {'object_name': 'ExternalIdentifiers'},
            'createdDate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifierCode': ('django.db.models.fields.CharField', [], {'max_length': "'24'"}),
            'identifierName': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'otherName': ('django.db.models.fields.CharField', [], {'max_length': "'255'", 'blank': 'True'})
        },
        u'hs_user_org.externalorgidentifiers': {
            'Meta': {'object_name': 'ExternalOrgIdentifiers'},
            'createdDate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifierCode': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'identifierName': ('django.db.models.fields.CharField', [], {'max_length': "'10'"}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'externalIdentifiers'", 'to': u"orm['hs_user_org.Organization']"}),
            'otherName': ('django.db.models.fields.CharField', [], {'max_length': "'255'", 'blank': 'True'})
        },
        u'hs_user_org.organization': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Organization', '_ormbases': [u'pages.Page']},
            'createdDate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'lastUpdate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'logoUrl': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'organizationType': ('django.db.models.fields.CharField', [], {'max_length': "'14'"}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'parentOrganization': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hs_user_org.Organization']", 'null': 'True'}),
            'persons': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'organizations'", 'null': 'True', 'through': u"orm['hs_user_org.OrgAssociations']", 'to': u"orm['hs_user_org.Person']"}),
            'uniqueCode': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': "'255'", 'blank': 'True'})
        },
        u'hs_user_org.organizationemail': {
            'Meta': {'object_name': 'OrganizationEmail'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'email_addresses'", 'to': u"orm['hs_user_org.Organization']"}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': "'30'", 'blank': 'True'}),
            'phone_type': ('django.db.models.fields.CharField', [], {'max_length': "'30'", 'blank': 'True'})
        },
        u'hs_user_org.organizationlocation': {
            'Meta': {'object_name': 'OrganizationLocation'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'address_type': ('django.db.models.fields.CharField', [], {'max_length': '24'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mail_addresses'", 'to': u"orm['hs_user_org.Organization']"})
        },
        u'hs_user_org.organizationphone': {
            'Meta': {'object_name': 'OrganizationPhone'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'phone_numbers'", 'to': u"orm['hs_user_org.Organization']"}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': "'30'"}),
            'phone_type': ('django.db.models.fields.CharField', [], {'max_length': "'30'"})
        },
        u'hs_user_org.orgassociations': {
            'Meta': {'object_name': 'OrgAssociations'},
            'beginDate': ('django.db.models.fields.DateField', [], {}),
            'createdDate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'endDate': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jobTitle': ('django.db.models.fields.CharField', [], {'max_length': "'100'", 'blank': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hs_user_org.Organization']"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hs_user_org.Person']"}),
            'presentOrganization': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'hs_user_org.othernames': {
            'Meta': {'object_name': 'OtherNames'},
            'annotation': ('django.db.models.fields.CharField', [], {'default': "'citation'", 'max_length': "'10'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otherName': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'persons': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'otherNames'", 'to': u"orm['hs_user_org.Person']"})
        },
        u'hs_user_org.person': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Person', '_ormbases': [u'pages.Page']},
            'createdDate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'familyName': ('django.db.models.fields.CharField', [], {'max_length': "'125'"}),
            'givenName': ('django.db.models.fields.CharField', [], {'max_length': "'125'"}),
            'jobTitle': ('django.db.models.fields.CharField', [], {'max_length': "'100'"}),
            'lastUpdate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'uniqueCode': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': "'255'", 'blank': 'True'})
        },
        u'hs_user_org.personemail': {
            'Meta': {'object_name': 'PersonEmail'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'email_addresses'", 'to': u"orm['hs_user_org.Person']"}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': "'30'", 'blank': 'True'}),
            'phone_type': ('django.db.models.fields.CharField', [], {'max_length': "'30'", 'blank': 'True'})
        },
        u'hs_user_org.personlocation': {
            'Meta': {'object_name': 'PersonLocation'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'address_type': ('django.db.models.fields.CharField', [], {'max_length': '24'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mail_addresses'", 'to': u"orm['hs_user_org.Person']"})
        },
        u'hs_user_org.personphone': {
            'Meta': {'object_name': 'PersonPhone'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'phone_numbers'", 'to': u"orm['hs_user_org.Person']"}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': "'30'"}),
            'phone_type': ('django.db.models.fields.CharField', [], {'max_length': "'30'"})
        },
        u'hs_user_org.region': {
            'Meta': {'object_name': 'Region'},
            'geonamesUrl': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'hs_user_org.scholar': {
            'Meta': {'object_name': 'Scholar'},
            'demographics': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hs_user_org.UserDemographics']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['hs_user_org.Person']", 'unique': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'hs_user_org.scholarexternalidentifiers': {
            'Meta': {'object_name': 'ScholarExternalIdentifiers', '_ormbases': [u'hs_user_org.ExternalIdentifiers']},
            u'externalidentifiers_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['hs_user_org.ExternalIdentifiers']", 'unique': 'True', 'primary_key': 'True'}),
            'scholar': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'external_identifiers'", 'to': u"orm['hs_user_org.Scholar']"})
        },
        u'hs_user_org.scholargroup': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'ScholarGroup', '_ormbases': [u'pages.Page']},
            'createdBy': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'creator_of'", 'unique': 'True', 'to': u"orm['hs_user_org.Scholar']"}),
            'createdDate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'groupDescription': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'100'"}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'persons': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'groups'", 'symmetrical': 'False', 'through': u"orm['hs_user_org.ScholarGroupAssociations']", 'to': u"orm['hs_user_org.Scholar']"}),
            'purpose': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'hs_user_org.scholargroupassociations': {
            'Meta': {'object_name': 'ScholarGroupAssociations'},
            'beginDate': ('django.db.models.fields.DateField', [], {}),
            'createdDate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'endDate': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hs_user_org.ScholarGroup']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'scholar': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hs_user_org.Scholar']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': "'100'", 'blank': 'True'})
        },
        u'hs_user_org.userdemographics': {
            'Meta': {'object_name': 'UserDemographics'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hs_user_org.City']", 'null': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hs_user_org.Country']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hs_user_org.Region']", 'null': 'True'}),
            'userType': ('django.db.models.fields.CharField', [], {'max_length': "'255'"})
        },
        u'hs_user_org.userkeywords': {
            'Meta': {'object_name': 'UserKeywords'},
            'createdDate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyword': ('django.db.models.fields.CharField', [], {'max_length': "'100'"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'keywords'", 'to': u"orm['hs_user_org.Person']"})
        },
        u'pages.page': {
            'Meta': {'ordering': "(u'titles',)", 'object_name': 'Page'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_menus': ('mezzanine.pages.fields.MenusField', [], {'default': '(1, 2, 3)', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'children'", 'null': 'True', 'to': u"orm['pages.Page']"}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'titles': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['hs_user_org']