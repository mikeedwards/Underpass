# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LevelPost'
        db.create_table('core_levelpost', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('inline_ordering_position', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('level', self.gf('django.db.models.fields.related.ForeignKey')(related_name='posts', to=orm['core.Level'])),
            ('post_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='level_posts', to=orm['core.PostType'])),
        ))
        db.send_create_signal('core', ['LevelPost'])

        # Adding model 'Level'
        db.create_table('core_level', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('inline_ordering_position', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('kit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='levels', to=orm['core.Kit'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='levels', to=orm['auth.User'])),
        ))
        db.send_create_signal('core', ['Level'])

        # Adding model 'Kit'
        db.create_table('core_kit', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='kits', to=orm['auth.User'])),
        ))
        db.send_create_signal('core', ['Kit'])

        # Adding model 'LevelPlank'
        db.create_table('core_levelplank', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('inline_ordering_position', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('level', self.gf('django.db.models.fields.related.ForeignKey')(related_name='planks', to=orm['core.Level'])),
            ('post_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='level_planks', to=orm['core.PostType'])),
            ('body', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('core', ['LevelPlank'])

        # Adding field 'PostType.created'
        db.add_column('core_posttype', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Adding field 'PostType.modified'
        db.add_column('core_posttype', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Adding field 'Bridge.created'
        db.add_column('core_bridge', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Adding field 'Bridge.modified'
        db.add_column('core_bridge', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Adding field 'Bridge.level'
        db.add_column('core_bridge', 'level',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='bridges', to=orm['core.Level']),
                      keep_default=False)

        # Adding field 'Post.created'
        db.add_column('core_post', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Adding field 'Post.modified'
        db.add_column('core_post', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Adding field 'Post.inline_ordering_position'
        db.add_column('core_post', 'inline_ordering_position',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Plank.created'
        db.add_column('core_plank', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Adding field 'Plank.modified'
        db.add_column('core_plank', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Adding field 'Plank.inline_ordering_position'
        db.add_column('core_plank', 'inline_ordering_position',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'LevelPost'
        db.delete_table('core_levelpost')

        # Deleting model 'Level'
        db.delete_table('core_level')

        # Deleting model 'Kit'
        db.delete_table('core_kit')

        # Deleting model 'LevelPlank'
        db.delete_table('core_levelplank')

        # Deleting field 'PostType.created'
        db.delete_column('core_posttype', 'created')

        # Deleting field 'PostType.modified'
        db.delete_column('core_posttype', 'modified')

        # Deleting field 'Bridge.created'
        db.delete_column('core_bridge', 'created')

        # Deleting field 'Bridge.modified'
        db.delete_column('core_bridge', 'modified')

        # Deleting field 'Bridge.level'
        db.delete_column('core_bridge', 'level_id')

        # Deleting field 'Post.created'
        db.delete_column('core_post', 'created')

        # Deleting field 'Post.modified'
        db.delete_column('core_post', 'modified')

        # Deleting field 'Post.inline_ordering_position'
        db.delete_column('core_post', 'inline_ordering_position')

        # Deleting field 'Plank.created'
        db.delete_column('core_plank', 'created')

        # Deleting field 'Plank.modified'
        db.delete_column('core_plank', 'modified')

        # Deleting field 'Plank.inline_ordering_position'
        db.delete_column('core_plank', 'inline_ordering_position')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.bridge': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Bridge'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'bridges'", 'to': "orm['core.Level']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'bridges'", 'to': "orm['auth.User']"})
        },
        'core.kit': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Kit'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'kits'", 'to': "orm['auth.User']"})
        },
        'core.level': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Level'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inline_ordering_position': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'kit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'levels'", 'to': "orm['core.Kit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'levels'", 'to': "orm['auth.User']"})
        },
        'core.levelplank': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'LevelPlank'},
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inline_ordering_position': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'level': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'planks'", 'to': "orm['core.Level']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'post_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'level_planks'", 'to': "orm['core.PostType']"})
        },
        'core.levelpost': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'LevelPost'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inline_ordering_position': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'level': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'posts'", 'to': "orm['core.Level']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'post_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'level_posts'", 'to': "orm['core.PostType']"})
        },
        'core.plank': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Plank'},
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'bridge': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'planks'", 'to': "orm['core.Bridge']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inline_ordering_position': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'post_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'planks'", 'to': "orm['core.PostType']"})
        },
        'core.post': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Post'},
            'bridge': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'posts'", 'to': "orm['core.Bridge']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inline_ordering_position': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'post_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'posts'", 'to': "orm['core.PostType']"})
        },
        'core.posttype': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'PostType'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['core']