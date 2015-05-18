# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tratamiento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cara',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=128)),
            ],
        ),
        migrations.AlterField(
            model_name='detalleprestacion',
            name='cara',
            field=models.ForeignKey(blank=True, to='tratamiento.Cara', null=True),
        ),
    ]
