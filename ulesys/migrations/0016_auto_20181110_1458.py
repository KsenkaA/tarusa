# Generated by Django 2.1.1 on 2018-11-10 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ulesys', '0015_order_tour_starts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='end_month',
            field=models.FloatField(default=1.2019),
        ),
    ]
