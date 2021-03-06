# Generated by Django 2.1.1 on 2018-10-23 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ulesys', '0003_partofexpense_left_to_pay'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartOfLilExpense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.IntegerField(default=0)),
                ('currency', models.CharField(default='', max_length=10)),
                ('part_of_expense', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='ulesys.PartOfExpense')),
            ],
        ),
    ]
