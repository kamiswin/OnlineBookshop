# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('Bookshop', '0004_auto_20150103_0420'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=2000)),
                ('aid', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('bid', models.ForeignKey(to='Bookshop.Book')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='account',
            name='comments',
            field=models.ManyToManyField(related_name='accounts_commented_on_this_book', through='Bookshop.Comment', to='Bookshop.Book'),
            preserve_default=True,
        ),
    ]
