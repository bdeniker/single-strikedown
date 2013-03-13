# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NestCharacter'
        db.create_table('nest_nestcharacter', (
            ('character_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['playerbase.Character'], unique=True, primary_key=True)),
            ('strength', self.gf('django.db.models.fields.IntegerField')()),
            ('endurance', self.gf('django.db.models.fields.IntegerField')()),
            ('aura', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('nest', ['NestCharacter'])

        # Adding M2M table for field virtues on 'NestCharacter'
        db.create_table('nest_nestcharacter_virtues', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('nestcharacter', models.ForeignKey(orm['nest.nestcharacter'], null=False)),
            ('virtue', models.ForeignKey(orm['nest.virtue'], null=False))
        ))
        db.create_unique('nest_nestcharacter_virtues', ['nestcharacter_id', 'virtue_id'])

        # Adding M2M table for field flaws on 'NestCharacter'
        db.create_table('nest_nestcharacter_flaws', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('nestcharacter', models.ForeignKey(orm['nest.nestcharacter'], null=False)),
            ('flaw', models.ForeignKey(orm['nest.flaw'], null=False))
        ))
        db.create_unique('nest_nestcharacter_flaws', ['nestcharacter_id', 'flaw_id'])

        # Adding M2M table for field post_master_tweaks on 'NestCharacter'
        db.create_table('nest_nestcharacter_post_master_tweaks', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('nestcharacter', models.ForeignKey(orm['nest.nestcharacter'], null=False)),
            ('postmastertweak', models.ForeignKey(orm['nest.postmastertweak'], null=False))
        ))
        db.create_unique('nest_nestcharacter_post_master_tweaks', ['nestcharacter_id', 'postmastertweak_id'])

        # Adding M2M table for field items on 'NestCharacter'
        db.create_table('nest_nestcharacter_items', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('nestcharacter', models.ForeignKey(orm['nest.nestcharacter'], null=False)),
            ('item', models.ForeignKey(orm['nest.item'], null=False))
        ))
        db.create_unique('nest_nestcharacter_items', ['nestcharacter_id', 'item_id'])

        # Adding model 'Skill'
        db.create_table('nest_skill', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('nest', ['Skill'])

        # Adding model 'HasSkill'
        db.create_table('nest_hasskill', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('character', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nest.NestCharacter'])),
            ('skill', self.gf('django.db.models.fields.related.ForeignKey')(related_name='characters', to=orm['nest.Skill'])),
            ('level', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('nest', ['HasSkill'])

        # Adding model 'Virtue'
        db.create_table('nest_virtue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('level', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('nest', ['Virtue'])

        # Adding model 'Flaw'
        db.create_table('nest_flaw', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('level', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('nest', ['Flaw'])

        # Adding model 'PostMasterTweak'
        db.create_table('nest_postmastertweak', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('level', self.gf('django.db.models.fields.IntegerField')()),
            ('skill', self.gf('django.db.models.fields.related.ForeignKey')(related_name='postmasters', to=orm['nest.Skill'])),
        ))
        db.send_create_signal('nest', ['PostMasterTweak'])

        # Adding model 'Item'
        db.create_table('nest_item', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('nest', ['Item'])


    def backwards(self, orm):
        # Deleting model 'NestCharacter'
        db.delete_table('nest_nestcharacter')

        # Removing M2M table for field virtues on 'NestCharacter'
        db.delete_table('nest_nestcharacter_virtues')

        # Removing M2M table for field flaws on 'NestCharacter'
        db.delete_table('nest_nestcharacter_flaws')

        # Removing M2M table for field post_master_tweaks on 'NestCharacter'
        db.delete_table('nest_nestcharacter_post_master_tweaks')

        # Removing M2M table for field items on 'NestCharacter'
        db.delete_table('nest_nestcharacter_items')

        # Deleting model 'Skill'
        db.delete_table('nest_skill')

        # Deleting model 'HasSkill'
        db.delete_table('nest_hasskill')

        # Deleting model 'Virtue'
        db.delete_table('nest_virtue')

        # Deleting model 'Flaw'
        db.delete_table('nest_flaw')

        # Deleting model 'PostMasterTweak'
        db.delete_table('nest_postmastertweak')

        # Deleting model 'Item'
        db.delete_table('nest_item')


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