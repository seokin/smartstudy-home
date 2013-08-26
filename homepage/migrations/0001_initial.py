# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Crew'
        db.create_table(u'homepage_crew', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nick_en', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('nick_ko', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('title_en', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('title_ko', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('name_ko', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('uid', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('picture_big', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('comment_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('comment_ko', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('home', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('facebook', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('github', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal(u'homepage', ['Crew'])

        # Adding model 'App'
        db.create_table(u'homepage_app', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title_en', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('title_ko', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('subtitle_en', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('subtitle_ko', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('icon', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('appid_appstore_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('appid_appstore_ko', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('appid_playstore_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('appid_playstore_ko', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('desc_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('desc_ko', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('desc_more_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('desc_more_ko', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('launched', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'homepage', ['App'])

        # Adding model 'AppImage'
        db.create_table(u'homepage_appimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('app', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['homepage.App'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'homepage', ['AppImage'])

        # Adding model 'AppCategory'
        db.create_table(u'homepage_appcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('title_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('title_ko', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'homepage', ['AppCategory'])

        # Adding M2M table for field app on 'AppCategory'
        m2m_table_name = db.shorten_name(u'homepage_appcategory_app')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('appcategory', models.ForeignKey(orm[u'homepage.appcategory'], null=False)),
            ('app', models.ForeignKey(orm[u'homepage.app'], null=False))
        ))
        db.create_unique(m2m_table_name, ['appcategory_id', 'app_id'])

        # Adding model 'Testimonial'
        db.create_table(u'homepage_testimonial', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('tldr', self.gf('django.db.models.fields.TextField')()),
            ('desc', self.gf('django.db.models.fields.TextField')()),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'homepage', ['Testimonial'])

        # Adding model 'Job'
        db.create_table(u'homepage_job', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('desc', self.gf('django.db.models.fields.TextField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'homepage', ['Job'])

        # Adding model 'Resume'
        db.create_table(u'homepage_resume', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='D', max_length=1)),
            ('apply_to', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['homepage.Job'])),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=255, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('contact', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('desc', self.gf('jsonfield.fields.JSONField')(default={})),
            ('attachment', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('applied', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'homepage', ['Resume'])

        # Adding model 'ResumeRating'
        db.create_table(u'homepage_resumerating', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('resume', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['homepage.Resume'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
            ('desc', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'homepage', ['ResumeRating'])

        # Adding model 'Poster'
        db.create_table(u'homepage_poster', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('desc', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'homepage', ['Poster'])


    def backwards(self, orm):
        # Deleting model 'Crew'
        db.delete_table(u'homepage_crew')

        # Deleting model 'App'
        db.delete_table(u'homepage_app')

        # Deleting model 'AppImage'
        db.delete_table(u'homepage_appimage')

        # Deleting model 'AppCategory'
        db.delete_table(u'homepage_appcategory')

        # Removing M2M table for field app on 'AppCategory'
        db.delete_table(db.shorten_name(u'homepage_appcategory_app'))

        # Deleting model 'Testimonial'
        db.delete_table(u'homepage_testimonial')

        # Deleting model 'Job'
        db.delete_table(u'homepage_job')

        # Deleting model 'Resume'
        db.delete_table(u'homepage_resume')

        # Deleting model 'ResumeRating'
        db.delete_table(u'homepage_resumerating')

        # Deleting model 'Poster'
        db.delete_table(u'homepage_poster')


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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'homepage.app': {
            'Meta': {'object_name': 'App'},
            'appid_appstore_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'appid_appstore_ko': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'appid_playstore_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'appid_playstore_ko': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'desc_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'desc_ko': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'desc_more_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'desc_more_ko': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'launched': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'subtitle_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'subtitle_ko': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title_ko': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'homepage.appcategory': {
            'Meta': {'object_name': 'AppCategory'},
            'app': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['homepage.App']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_ko': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'homepage.appimage': {
            'Meta': {'object_name': 'AppImage'},
            'app': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': u"orm['homepage.App']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'homepage.crew': {
            'Meta': {'ordering': "['name_ko']", 'object_name': 'Crew'},
            'comment_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'comment_ko': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'github': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'home': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_ko': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'nick_en': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'nick_ko': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'picture_big': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'title_ko': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'homepage.job': {
            'Meta': {'object_name': 'Job'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'desc': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'homepage.poster': {
            'Meta': {'object_name': 'Poster'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'homepage.resume': {
            'Meta': {'object_name': 'Resume'},
            'applied': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'apply_to': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['homepage.Job']"}),
            'attachment': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'desc': ('jsonfield.fields.JSONField', [], {'default': '{}'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '1'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        u'homepage.resumerating': {
            'Meta': {'object_name': 'ResumeRating'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {}),
            'resume': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['homepage.Resume']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'homepage.testimonial': {
            'Meta': {'object_name': 'Testimonial'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'desc': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tldr': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['homepage']