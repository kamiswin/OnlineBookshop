# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bookshop', '0006_book_related_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='comments',
            field=models.ManyToManyField(related_name='comments_on_this_book', through='Bookshop.Comment', to='Bookshop.Book'),
            preserve_default=True,
        ),
    ]
