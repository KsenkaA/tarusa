from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Partner(models.Model):
    name = models.CharField(
        max_length=100,
        default=''
    )
    address = models.CharField(
        max_length=200,
        default=''
    )
    vat = models.CharField(
        max_length=100,
        default=''
    )
    phones = models.CharField(
        max_length=100,
        default=''
    )
    email = models.EmailField
    notes = models.CharField(
        max_length=1000,
        default=''
    )

    def __str__(self):
        return str(self.name)


class Order(models.Model):
    created = models.DateField(default=datetime.now)
    tour_starts = models.DateField(default=datetime.now)
    number = models.IntegerField(
        default=-1,
    )
    manager = models.ForeignKey(
        User,
        default=0,
        blank=True,
        null=True,
        on_delete=models.SET_DEFAULT,
        related_name='orders'
    )
    partner = models.ForeignKey(
        Partner,
        default='',
        on_delete=models.SET_DEFAULT,
        related_name='orders'
    )
    ref = models.CharField(
        default='',
        max_length=20
    )
    another_manager = models.CharField(
        max_length=30,
        default='Не указан'
    )
    last_name = models.CharField(
        max_length=30,
        default='Не указана'
    )
    end_month = models.CharField(
        max_length=100,
        default='1.18',
    )
    comments = models.CharField(
        max_length=9000,
        default='',
    )
    price = models.CharField(
        max_length=100,
        default='',
    )
    file_base = models.CharField(
        max_length=1000,
        default='',
    )
    def __str__(self):
        return str(self.number)


class Service(models.Model):
    name = models.CharField(
        max_length=100,
        default=''
    )
    price_for_buyer = models.IntegerField(
        default=0,
    )
    real_price = models.IntegerField(
        default=0,
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='services'
    )

    def __str__(self):
        return str(self.name)


class WholeIncome(models.Model):
    money = models.IntegerField(
        default=0,
    )
    currency = models.CharField(
        max_length=10,
        default=''
    )
    created = models.DateField(auto_now_add=True, blank=True)
    way_to_pay = models.CharField(
        max_length=30,
        default=''
    )
    partner = models.ForeignKey(
        Partner,
        default='',
        on_delete=models.SET_DEFAULT,
        related_name='incomes'
    )
    file = models.FileField(upload_to='media/')
    comments = models.CharField(
        max_length=500,
        default=''
    )
    def __str__(self):
        return str(self.created)


class PartOfIncome(models.Model):
    whole_income = models.ForeignKey(
        WholeIncome,
        on_delete=models.CASCADE,
        related_name='incomes'
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='incomes'
    )
    money = models.IntegerField(
        default=0,
    )
    currency = models.CharField(
        max_length=10,
        default=''
    )
    comments = models.CharField(
        max_length=500,
        default=''
    )


class WholeExpense(models.Model):
    money = models.IntegerField(
        default=0,
    )
    currency = models.CharField(
        max_length=10,
        default=''
    )
    created = models.DateField(auto_now_add=True)
    way_to_pay = models.CharField(
        max_length=30,
        default=''
    )
    partner = models.ForeignKey(
        Partner,
        default='',
        on_delete=models.SET_DEFAULT,
        related_name='expenses'
    )
    file = models.FileField(upload_to='media/')
    comments = models.CharField(
        max_length=500,
        default=''
    )

    def __str__(self):
        return str(self.created)


class PartOfExpense(models.Model):
    whole_expense = models.ForeignKey(
        WholeExpense,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    name = models.CharField(
        max_length=100,
        default=''
    )
    left_to_pay = models.IntegerField(
        default=0,
    )
    money = models.IntegerField(
        default=0,
    )
    currency = models.CharField(
        max_length=10,
        default=''
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name='expense'
    )
    payed = models.BooleanField(default=False)
    order_number = models.IntegerField(
        default=-1,
    )
    partner = models.ForeignKey(
        Partner,
        default='',
        blank=True,
        null=True,
        on_delete=models.SET_DEFAULT,
        related_name='exp_names'
    )
    comments = models.CharField(
        max_length=500,
        default=''
    )


class PartOfLilExpense(models.Model):
    whole_expense = models.ForeignKey(
        WholeExpense,
        on_delete=models.CASCADE,
        related_name='expenses',
        blank=True,
        null=True,
    )
    part_of_expense = models.ForeignKey(
        PartOfExpense,
        on_delete=models.CASCADE,
        related_name='expenses',
        blank=True,
        null=True,
    )
    money = models.IntegerField(
        default=0,
    )
    currency = models.CharField(
        max_length=10,
        default=''
    )
    comments = models.CharField(
        max_length=500,
        default=''
    )


class PayDay(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='pay_days',
        blank=True,
        null=True,
    )
    part_of_expense = models.ForeignKey(
        PartOfExpense,
        on_delete=models.CASCADE,
        related_name='pay_days',
        blank=True,
        null=True,
    )
    percent = models.IntegerField(
        default=0,
    )
    date = models.DateField(default=datetime.now)


class GetPayedDay(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='get_payed_days',
        blank=True,
        null=True,
    )
    percent = models.IntegerField(
        default=0,
    )
    date = models.DateField(default=datetime.now)


class Job(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    manager = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    fin_manager = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Job.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.job.save()
