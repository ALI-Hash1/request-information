# Generated by Django 5.1 on 2024-09-13 18:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0003_remove_apirequestlog_user_agent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apirequestlog',
            name='requested_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 9, 13, 21, 39, 48, 250847)),
        ),
    ]
