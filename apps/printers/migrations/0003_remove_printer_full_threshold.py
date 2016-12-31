# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('printers', '0002_auto_20161026_2229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='printer',
            name='full_threshold',
        ),
    ]
