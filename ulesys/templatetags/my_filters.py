from django.template.defaultfilters import register
import openpyxl
from datetime import datetime


@register.filter(name='lookup')
def lookup(dict, index):
    if index in dict:
        return dict[index]
    return ''


@register.filter(name='percent')
def percent(price, payed):
    print(price, payed)
    percent = str((int(payed)/int(price))*100)
    percent = percent.split('.')
    return percent[0] + '.' + percent[1][:1]


@register.filter(name='index')
def index(arr, index):
    return arr[index]


@register.filter(name='len')
def len(arr):
    return len(arr)
