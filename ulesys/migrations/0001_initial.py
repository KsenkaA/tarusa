# Generated by Django 2.1.1 on 2018-10-13 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GetPayedDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_pr', models.IntegerField(default=0)),
                ('second_pr', models.IntegerField(default=0)),
                ('third_pr', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=-1)),
                ('ref', models.CharField(default='', max_length=20)),
                ('another_manager', models.CharField(default='Не указан', max_length=30)),
                ('last_name', models.CharField(default='Не указана', max_length=30)),
                ('end_month', models.IntegerField(default=0)),
                ('comments', models.CharField(default='', max_length=9000)),
                ('manager', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='orders', to='ulesys.Manager')),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('address', models.CharField(default='', max_length=200)),
                ('vat', models.CharField(default='', max_length=100)),
                ('phones', models.CharField(default='', max_length=100)),
                ('notes', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='PartOfExpense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.IntegerField(default=0)),
                ('currency', models.CharField(default='', max_length=10)),
                ('payed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PartOfIncome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.IntegerField(default=0)),
                ('currency', models.CharField(default='', max_length=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incomes', to='ulesys.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('price_for_buyer', models.IntegerField(default=0)),
                ('real_price', models.IntegerField(default=0)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='ulesys.Order')),
            ],
        ),
        migrations.CreateModel(
            name='WholeExpense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.IntegerField(default=0)),
                ('currency', models.CharField(default='', max_length=10)),
                ('created', models.DateField(auto_now_add=True)),
                ('way_to_pay', models.CharField(default='', max_length=30)),
                ('file', models.FileField(upload_to='media/')),
                ('partner', models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='expenses', to='ulesys.Partner')),
            ],
        ),
        migrations.CreateModel(
            name='WholeIncome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.IntegerField(default=0)),
                ('currency', models.CharField(default='', max_length=10)),
                ('created', models.DateField(auto_now_add=True)),
                ('way_to_pay', models.CharField(default='', max_length=30)),
                ('file', models.FileField(upload_to='media/')),
                ('partner', models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='incomes', to='ulesys.Partner')),
            ],
        ),
        migrations.AddField(
            model_name='partofincome',
            name='whole_income',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incomes', to='ulesys.WholeIncome'),
        ),
        migrations.AddField(
            model_name='partofexpense',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expense', to='ulesys.Service'),
        ),
        migrations.AddField(
            model_name='partofexpense',
            name='whole_expense',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='ulesys.WholeExpense'),
        ),
        migrations.AddField(
            model_name='order',
            name='partner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='orders', to='ulesys.Partner'),
        ),
        migrations.AddField(
            model_name='getpayedday',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_payed', to='ulesys.Order'),
        ),
    ]
