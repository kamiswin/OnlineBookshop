# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Bookshop', '0003_auto_20141231_0233'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['date']},
        ),
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 3, 4, 20, 1, 484572, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
