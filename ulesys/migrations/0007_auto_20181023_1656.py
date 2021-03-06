# Generated by Django 2.1.1 on 2018-10-23 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ulesys', '0006_partofexpense_order_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='partoflilexpense',
            name='whole_expense',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='ulesys.WholeExpense'),
        ),
        migrations.AlterField(
            model_name='partofexpense',
            name='whole_expense',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ulesys.WholeExpense'),
        ),
    ]
