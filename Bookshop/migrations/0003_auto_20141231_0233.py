# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bookshop', '0002_auto_20141231_0212'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.CharField(default='English', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='page_number',
            field=models.IntegerField(default=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.FloatField(default=11.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.CharField(default="People's Publishing House", max_length=1000),
            preserve_default=False,
        ),
    ]
