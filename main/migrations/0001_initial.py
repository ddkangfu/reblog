# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60, verbose_name='\u6807\u9898')),
                ('slug', models.SlugField(help_text=b"Used to build the entry's URL.", max_length=255, verbose_name=b'slug', unique_for_date=b'creation_date')),
                ('status', models.IntegerField(default=0, db_index=True, verbose_name=b'status', choices=[(0, b'draft'), (1, b'hidden'), (2, b'published')])),
                ('start_publication', models.DateTimeField(help_text=b'Start date of publication.', null=True, verbose_name=b'start publication', db_index=True, blank=True)),
                ('end_publication', models.DateTimeField(help_text=b'End date of publication.', null=True, verbose_name=b'end publication', db_index=True, blank=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True, help_text=b"Used to build the entry's URL.", verbose_name=b'creation date', db_index=True)),
                ('last_update', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'last update')),
            ],
            options={
                'ordering': ['-creation_date'],
            },
            bases=(models.Model,),
        ),
    ]
