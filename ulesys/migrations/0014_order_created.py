# Generated by Django 2.1.1 on 2018-11-06 16:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ulesys', '0013_auto_20181029_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]