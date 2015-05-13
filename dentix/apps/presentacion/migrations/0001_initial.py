# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ficha',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('foto_f1', models.FileField(null=True, upload_to=b'uploads_imgs', blank=True)),
                ('copago', models.DecimalField(max_digits=16, decimal_places=2)),
                ('estampilla', models.DecimalField(max_digits=16, decimal_places=2)),
                ('importe_estimado', models.DecimalField(max_digits=16, decimal_places=2)),
                ('importe_cobrado', models.DecimalField(max_digits=16, decimal_places=2)),
                ('estado', models.SmallIntegerField(choices=[(1, b'Pendiente'), (2, b'Pagado'), (2, b'No Pagado')])),
                ('paciente', models.ForeignKey(to='paciente.Paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Presentacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('entidad', models.SmallIntegerField(choices=[(1, b'Asor'), (2, b'Ale vanucci')])),
            ],
        ),
        migrations.AddField(
            model_name='ficha',
            name='presentacion',
            field=models.ForeignKey(to='presentacion.Presentacion'),
        ),
    ]
