# Generated by Django 2.1.1 on 2018-11-24 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ulesys', '0018_auto_20181117_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='end_month',
            field=models.CharField(default='1.18', max_length=100),
        ),
    ]