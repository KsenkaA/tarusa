# Generated by Django 2.1.1 on 2018-12-25 06:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ulesys', '0023_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='manager',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='orders', to=settings.AUTH_USER_MODEL),
        ),
    ]