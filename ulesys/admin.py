from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class JobInline(admin.StackedInline):
    model = models.Job
    can_delete = False
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (JobInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


class PartOfExpenseInline(admin.TabularInline):
    model = models.PartOfExpense
    extra = 1


class PartOfExpenseInServiceInline(admin.TabularInline):
    model = models.PartOfExpense
    extra = 1


class ServiceAdmin(admin.ModelAdmin):
    inlines = [PartOfExpenseInServiceInline]


class OrderAdmin(admin.ModelAdmin):
    list_display = ('created', 'number', 'partner', 'ref', 'price', 'end_month', 'last_name', 'manager', 'another_manager', 'comments', )


class WholeExpenseAdmin(admin.ModelAdmin):
    inlines = [PartOfExpenseInline]
    list_display = ('created', 'money', 'currency', 'way_to_pay', 'partner')


class PartOfExpenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'money', 'left_to_pay', 'currency', 'service', 'partner', 'payed')

admin.site.register(models.Partner)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.Service, ServiceAdmin)
admin.site.register(models.WholeIncome)
admin.site.register(models.PartOfIncome)
admin.site.register(models.PayDay)
admin.site.register(models.WholeExpense, WholeExpenseAdmin)
admin.site.register(models.PartOfExpense, PartOfExpenseAdmin)
admin.site.register(models.PartOfLilExpense)
admin.site.register(models.GetPayedDay)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
# Register your models here.
