# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obrasocial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obrasocial',
            name='observaciones',
            field=models.TextField(max_length=1024, null=True, blank=True),
        ),
    ]
