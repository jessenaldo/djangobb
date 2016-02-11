# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('destination', models.CharField(max_length=90)),
                ('description', models.TextField()),
                ('date_from', models.DateTimeField()),
                ('date_to', models.DateTimeField()),
                ('created_by_user', models.ForeignKey(related_name='created_by_user', to=settings.AUTH_USER_MODEL)),
                ('joined_users', models.ManyToManyField(related_name='joined_users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'plans',
            },
        ),
    ]
