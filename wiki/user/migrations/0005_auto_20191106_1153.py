# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-11-06 11:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_userprofile_login_tiem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='login_tiem',
            new_name='login_time',
        ),
    ]
