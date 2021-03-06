# Generated by Django 2.0.6 on 2018-06-11 06:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20180610_0324'),
    ]

    operations = [
        migrations.CreateModel(
            name='common_member_email_send_time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_time', models.IntegerField()),
                ('last_send_time', models.TimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='common_member_action_log',
            name='dateline',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='common_member_star',
            name='star_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='member_crime',
            name='dateline',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
