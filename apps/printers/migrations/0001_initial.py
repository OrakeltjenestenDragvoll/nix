# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PaperLogEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
                ('paper_text', models.TextField()),
                ('paper_remaining', models.BigIntegerField()),
                ('last_read', models.BigIntegerField()),
                ('low_threshold', models.BigIntegerField()),
                ('medium_threshold', models.BigIntegerField()),
                ('full_threshold', models.BigIntegerField()),
                ('status', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
