# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-12 12:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('path', models.CharField(blank=True, max_length=100, null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_folders', to='folders.Folder')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='folder',
            unique_together=set([('name', 'parent')]),
        ),
    ]