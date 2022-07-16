from django.contrib import admin
from .models import Сlients, Contract, One_time_contract, Employee, Support_services, One_time_services, Type_of_service, Scope_of_service



@admin.register(Сlients)
class Admin(admin.ModelAdmin):
    fields = ('name_of_the_organization', 'address', 'contact_person', 'phone_number', )
    list_display = ('name_of_the_organization', 'address', 'contact_person', )
    list_filter = ('name_of_the_organization',)


@admin.register(Contract)
class Admin2(admin.ModelAdmin):
    fields = ('name', 'fk_clients', 'date', 'fk_support_services', 'fk_Scope_of_service', 'fk_employee', 'quantity', 'cost', 'state', 'sum', )
    list_display = ('name', 'fk_clients', 'date', 'fk_support_services', 'fk_employee', 'quantity', 'cost', 'state', 'sum', )
    list_filter = ('name',)


@admin.register(One_time_contract)
class Admin3(admin.ModelAdmin):
    fields = ('name', 'fk_clients', 'date_from', 'date_to', 'fk_one_time_services', 'fk_Scope_of_service', 'fk_employee', 'quantity', 'cost', 'state', )
    list_display = ('name', 'fk_clients', 'date_from', 'date_to', 'fk_one_time_services', 'fk_employee', 'quantity', 'cost', 'state', )
    list_filter = ('name',)

@admin.register(Employee)
class Admin4(admin.ModelAdmin):
    fields = ('working_group_name', )
    list_display = ('working_group_name', )
    list_filter = ('working_group_name',)

@admin.register(Support_services)
class Admin5(admin.ModelAdmin):
    fields = ('name', 'short_name', )
    list_display = ('name', 'short_name', )
    list_filter = ('short_name',)

@admin.register(One_time_services)
class Admin6(admin.ModelAdmin):
    fields = ('name', 'short_name', )
    list_display = ('name', 'short_name', )
    list_filter = ('short_name',)

@admin.register(Type_of_service)
class Admin7(admin.ModelAdmin):
    fields = ('name', )
    list_display = ('name', )
    list_filter = ('name',)

@admin.register(Scope_of_service)
class Admin10(admin.ModelAdmin):
    fields = ('name', )
    list_display = ('name', )
    list_filter = ('name',)

