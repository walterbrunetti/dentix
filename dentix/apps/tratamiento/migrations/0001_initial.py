# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0001_initial'),
        ('presentacion', '0001_initial'),
        ('prestacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetallePrestacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cara', models.SmallIntegerField(blank=True, null=True, choices=[(1, b'Distal'), (2, b'Mesial'), (3, b'Oclusal'), (4, b'Incisal')])),
            ],
        ),
        migrations.CreateModel(
            name='Diente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=128)),
                ('nro_diente', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Tratamiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('estado', models.SmallIntegerField(choices=[(1, b'Finalizado'), (2, b'En Proceso'), (3, b'Suspendido')])),
                ('foto_f3', models.FileField(null=True, upload_to=b'uploads_imgs', blank=True)),
                ('observaciones', models.TextField(max_length=1024, null=True, blank=True)),
                ('paciente', models.ForeignKey(to='paciente.Paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Visita',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('observaciones', models.TextField(max_length=1024, null=True, blank=True)),
                ('tratamiento', models.ForeignKey(to='tratamiento.Tratamiento')),
            ],
        ),
        migrations.AddField(
            model_name='detalleprestacion',
            name='diente',
            field=models.ForeignKey(blank=True, to='tratamiento.Diente', null=True),
        ),
        migrations.AddField(
            model_name='detalleprestacion',
            name='ficha',
            field=models.ForeignKey(blank=True, to='presentacion.Ficha', null=True),
        ),
        migrations.AddField(
            model_name='detalleprestacion',
            name='prestacion',
            field=models.ForeignKey(to='prestacion.Prestacion'),
        ),
        migrations.AddField(
            model_name='detalleprestacion',
            name='tratamiento',
            field=models.ForeignKey(to='tratamiento.Tratamiento'),
        ),
    ]
