# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PostMasterTweak.broadcast'
        db.add_column('nest_postmastertweak', 'broadcast',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Virtue.broadcast'
        db.add_column('nest_virtue', 'broadcast',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Flaw.broadcast'
        db.add_column('nest_flaw', 'broadcast',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'PostMasterTweak.broadcast'
        db.delete_column('nest_postmastertweak', 'broadcast')

        # Deleting field 'Virtue.broadcast'
        db.delete_column('nest_virtue', 'broadcast')

        # Deleting field 'Flaw.broadcast'
        db.delete_column('nest_flaw', 'broadcast')


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
        'nest.flaw': {
            'Meta': {'object_name': 'Flaw'},
            'broadcast': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'nest.hasskill': {
            'Meta': {'object_name': 'HasSkill'},
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['nest.NestCharacter']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'characters'", 'to': "orm['nest.Skill']"})
        },
        'nest.item': {
            'Meta': {'object_name': 'Item'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'nest.nestcharacter': {
            'Meta': {'object_name': 'NestCharacter', '_ormbases': ['playerbase.Character']},
            'aura': ('django.db.models.fields.IntegerField', [], {}),
            'character_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['playerbase.Character']", 'unique': 'True', 'primary_key': 'True'}),
            'endurance': ('django.db.models.fields.IntegerField', [], {}),
            'flaws': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'characters'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['nest.Flaw']"}),
            'items': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'characters'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['nest.Item']"}),
            'post_master_tweaks': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'characters'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['nest.PostMasterTweak']"}),
            'skills': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['nest.Skill']", 'null': 'True', 'through': "orm['nest.HasSkill']", 'blank': 'True'}),
            'strength': ('django.db.models.fields.IntegerField', [], {}),
            'virtues': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'characters'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['nest.Virtue']"})
        },
        'nest.postmastertweak': {
            'Meta': {'object_name': 'PostMasterTweak'},
            'broadcast': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'postmasters'", 'to': "orm['nest.Skill']"})
        },
        'nest.skill': {
            'Meta': {'object_name': 'Skill'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'nest.virtue': {
            'Meta': {'object_name': 'Virtue'},
            'broadcast': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'playerbase.character': {
            'Meta': {'object_name': 'Character'},
            'background': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'characters'", 'to': "orm['auth.User']"}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        }
    }

    complete_apps = ['nest']