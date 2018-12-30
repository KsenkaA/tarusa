from django.template.defaultfilters import register

@register.filter(name='index')
def index(arr, index):
    return arr[index]

@register.filter(name='len')
def len(arr):
    return len(arr)