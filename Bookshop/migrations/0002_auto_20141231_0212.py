# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('Bookshop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopCart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number_of_book', models.IntegerField()),
                ('aid', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('bid', models.ForeignKey(to='Bookshop.Book')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='account',
            name='shop_cart',
            field=models.ManyToManyField(to='Bookshop.Book', through='Bookshop.ShopCart'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='account',
            name='recommend_books',
            field=models.ManyToManyField(related_name='accounts_should_recommend_this_book', to='Bookshop.Book'),
            preserve_default=True,
        ),
    ]
