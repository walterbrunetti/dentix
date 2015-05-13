# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ObraSocial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=128)),
                ('telefono', models.CharField(max_length=128, null=True, blank=True)),
                ('direccion', models.CharField(max_length=128, null=True, blank=True)),
                ('observaciones', models.CharField(max_length=1024, null=True, blank=True)),
            ],
        ),
    ]
