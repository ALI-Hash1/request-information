# Generated by Django 5.1 on 2024-09-09 14:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0002_alter_apirequestlog_requested_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apirequestlog',
            name='user_agent',
        ),
        migrations.AlterField(
            model_name='apirequestlog',
            name='requested_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 9, 9, 17, 48, 16, 560795)),
        ),
    ]
