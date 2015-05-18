# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presentacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha',
            name='copago',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='estado',
            field=models.SmallIntegerField(choices=[(1, b'Pendiente'), (2, b'Pagado'), (3, b'No Pagado')]),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='estampilla',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='foto_f1',
            field=models.FileField(null=True, upload_to=b'dentix/uploads_imgs', blank=True),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='importe_cobrado',
            field=models.DecimalField(max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='importe_estimado',
            field=models.DecimalField(max_digits=10, decimal_places=2),
        ),
    ]
