# Generated by Django 2.0.6 on 2018-06-11 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20180611_0645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='common_member_email_send_time',
            name='email_time',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='common_member_email_send_time',
            name='last_send_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
