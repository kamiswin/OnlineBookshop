# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bookshop', '0005_auto_20150108_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='related_books',
            field=models.ManyToManyField(related_name='related_books_rel_+', to='Bookshop.Book'),
            preserve_default=True,
        ),
    ]
