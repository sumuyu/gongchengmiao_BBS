# Generated by Django 2.0.6 on 2018-06-09 18:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='common_member_star',
            name='star_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 9, 18, 16, 22, 792138)),
        ),
    ]
