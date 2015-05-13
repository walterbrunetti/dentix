# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obrasocial', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dni', models.IntegerField()),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('fecha_nacimiento', models.DateField()),
                ('domicilio', models.CharField(max_length=200, null=True, blank=True)),
                ('telefono', models.CharField(max_length=200)),
                ('celular', models.CharField(max_length=200, null=True, blank=True)),
                ('sexo', models.SmallIntegerField(choices=[(1, b'masculino'), (2, b'femenino')])),
                ('email', models.CharField(max_length=200, null=True, blank=True)),
                ('obra_social', models.ForeignKey(to='obrasocial.ObraSocial')),
            ],
        ),
    ]
