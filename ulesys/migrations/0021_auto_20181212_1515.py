# Generated by Django 2.1.1 on 2018-12-12 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ulesys', '0020_getpayedday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='getpayedday',
            name='order',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='get_payed_days', to='ulesys.Order'),
        ),
    ]
