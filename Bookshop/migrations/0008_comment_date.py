# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Bookshop', '0007_auto_20150108_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 8, 14, 47, 23, 992507, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
