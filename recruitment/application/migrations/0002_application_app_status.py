# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='app_status',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
