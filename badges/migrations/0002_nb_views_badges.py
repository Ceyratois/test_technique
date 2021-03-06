# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-16 19:36
from __future__ import unicode_literals

from django.db import migrations


badge_types_to_create = {
    "views_10": "local",
    "views_1000": "local",
    "views_1000000": "local",
    "models_1": "global",
    "models_5": "global",
    "models_10": "global"
}


def forwards_func(apps, schema_editor):
    """Create new badge types db objects."""
    
    BadgeType = apps.get_model("badges", "BadgeType")
    db_alias = schema_editor.connection.alias
    
    badge_types_list = [] 
    for identifier, category in badge_types_to_create.iteritems():
        badge_types_list.append(BadgeType(identifier=identifier, category=category))
    
    BadgeType.objects.using(db_alias).bulk_create(badge_types_list)


def reverse_func(apps, schema_editor):
    """Delete created badge types."""

    BadgeType = apps.get_model("badges", "BadgeType")
    db_alias = schema_editor.connection.alias
    for identifier, category in badge_types_to_create.iteritems():
        BadgeType.objects.using(db_alias).filter(identifier=identifier, category=category).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('badges', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]