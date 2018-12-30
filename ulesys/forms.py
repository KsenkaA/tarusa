from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Partner, Order, Service, PartOfExpense, WholeExpense, Service
from django.utils import timezone
from django.contrib.auth.models import User


def get_my_choices_manager():
    all_managers = User.objects.filter(job__manager=True)
    managers = []
    for manager in all_managers:
        managers.append((manager.first_name + " " + manager.last_name, manager.first_name + " " + manager.last_name))
    return managers


def get_my_choices_partner():
    all_partners = Partner.objects.all()
    partners = []
    for manager in all_partners:
        partners.append((manager.name, manager.name))
    return partners


def get_my_choices_orders():
    all_partners = Order.objects.all()
    orders = []
    for order in all_partners:
        orders.append((order.number, order.number))
    return orders


def get_my_choices_services():
    names = []
    for serv in PartOfExpense.objects.all():
        names.append((serv.name, serv.name))
    return names


def get_my_choices_services_num(num):
    names = []
    for service in Service.objects.filter(order=Order.objects.get(number=int(num))):
        for expense in service.expense.all():
            if not expense.payed:
                names.append((expense.name, expense.name))
    return names


def get_my_choices_services_num_all(num):
    names = []
    for service in Service.objects.filter(order=Order.objects.get(number=int(num))):
        names.append((service.name, service.name))
    return names


class OrderForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Сохранить счет'))
        self.fields['manager'] = forms.ChoiceField(
            choices=get_my_choices_manager(), label='Менеджер')
        self.fields['partner'] = forms.ChoiceField(
            choices=get_my_choices_partner(), label='Партнер')
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control selectpicker'
            visible.field.widget.attrs['data-live-search'] = 'true'
        self.fields['created'].widget.attrs['class'] = 'form-control'
        self.fields['created'].widget.attrs['style'] = 'width: 33%; display: inline-block;'
        self.fields['tour_starts'].widget.attrs['class'] = 'form-control'
        self.fields['tour_starts'].widget.attrs['style'] = 'width: 33%; display: inline-block;'
        self.fields['end_month'].widget.attrs['placeholder'] = 'В формате 3.18 (март 2018)'
    created = forms.DateField(label='Дата создания', widget=forms.SelectDateWidget, initial=timezone.now())
    manager = forms.ChoiceField(choices=[], label='Менеджер')
    partner = forms.ChoiceField(choices=[], label='Партнер')
    ref = forms.CharField(label='Референс партнера')
    another_manager = forms.CharField(label='Менеджер клиента')
    last_name = forms.CharField(label='Фамилия клиента')
    end_month = forms.FloatField(label='Месяц окончания поездки')
    comments = forms.CharField(label='Комментарии', widget=forms.Textarea(attrs={'rows': 4}))
    tour_starts = forms.DateField(label='Дата начала тура', widget=forms.SelectDateWidget, initial=timezone.now())


class WholeIncomeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Добавить приход'))
        self.fields['partner'] = forms.ChoiceField(
            choices=get_my_choices_partner(), label='Партнер')
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control selectpicker'
            visible.field.widget.attrs['data-live-search'] = 'true'
    money = forms.IntegerField(label='Сумма')
    currency = forms.CharField(label='Валюта')
    partner = forms.ChoiceField(choices=[], label='Партнер')
    way_to_pay = forms.CharField(label='Способ оплаты')
    file = forms.FileField(label="Прикрепить файл")
    comments = forms.CharField(label='Комментарии')


class PartOfIncomeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.fields['number'] = forms.ChoiceField(
            choices=get_my_choices_orders(), label='Заказ №')
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control selectpicker'
            visible.field.widget.attrs['data-live-search'] = 'true'
    number = forms.ChoiceField(choices=[], label='Заказ №')
    money = forms.IntegerField(label='Сумма')
    currency = forms.CharField(label='Валюта')
    comments = forms.CharField(label='Комментарии')


class PartOfExpenseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.fields['number'] = forms.ChoiceField(
            choices=get_my_choices_orders(), label='Заказ №')
        self.fields['service'] = forms.ChoiceField(choices=get_my_choices_services_num(Order.objects.all()[0].number), label='Услуга')

        if 'number' in self.data:
            number = int(self.data.get('number'))
            self.fields['service'] = forms.ChoiceField(choices=get_my_choices_services(), label='Услуга')
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control selectpicker'
            visible.field.widget.attrs['data-live-search'] = 'true'
    number = forms.ChoiceField(choices=[],label='Заказ №')
    service = forms.ChoiceField(choices=[], label='Услуга')
    money = forms.IntegerField(label='Сумма')
    currency = forms.CharField(label='Валюта')
    comments = forms.CharField(label='Комментарии')


class CreateExpenseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        number = kwargs.pop("number")

        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.fields['number'] = forms.IntegerField(label='Сумма', widget=forms.HiddenInput(), initial=number)
        self.fields['partner'] = forms.ChoiceField(
            choices=get_my_choices_partner(), label='Партнер')
        self.fields['service'] = forms.ChoiceField(choices=get_my_choices_services_num_all(number), label='Услуга')
        if 'number' in self.data:
            self.fields['service'] = forms.ChoiceField(choices=get_my_choices_services(), label='Услуга')
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control selectpicker'
            visible.field.widget.attrs['data-live-search'] = 'true'
    name = forms.CharField(label='Имя')
    service = forms.ChoiceField(choices=[], label='Услуга')
    money = forms.IntegerField(label='Сумма')
    currency = forms.CharField(label='Валюта')
    partner = forms.ChoiceField(choices=[], label='Партнер')
    comments = forms.CharField(label='Комментарии')
    number = forms.IntegerField(label='Сумма', widget=forms.HiddenInput())





