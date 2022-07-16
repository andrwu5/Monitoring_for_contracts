import django_filters
from django_filters import DateFilter, CharFilter

from .models import Сlients, Type_of_service, One_time_services, Support_services, Employee, Scope_of_service, Contract, One_time_contract


class СlientsFilter(django_filters.FilterSet):
    name_of_the_organization = CharFilter(field_name='name_of_the_organization', lookup_expr='icontains', label='Название организации')
    address = CharFilter(field_name='address', lookup_expr='icontains', label='Адрес')
    contact_person = CharFilter(field_name='contact_person', lookup_expr='icontains', label='Контактное лицо')


    class Meta:
        model = Сlients
        fields ='__all__'
        exclude = ['phone_number']

class Type_of_serviceFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains', label='Название типа')

    class Meta:
        model = Type_of_service
        fields ='__all__'

class One_time_servicesFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains', label='Название')

    class Meta:
        model = One_time_services
        fields ='__all__'
        exclude = ['short_name']

class Support_servicesFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains', label='Название')

    class Meta:
        model = Support_services
        fields ='__all__'
        exclude = ['short_name']

class EmployeeFilter(django_filters.FilterSet):
    working_group_name = CharFilter(field_name='working_group_name', lookup_expr='icontains', label='Название')

    class Meta:
        model = Employee
        fields ='__all__'

class Scope_of_serviceFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains', label='Название')

    class Meta:
        model = Scope_of_service
        fields ='__all__'

class ContractFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains', label='Название')

    class Meta:
        model = Contract
        fields ='__all__'
        exclude = ['cost', 'state', 'quantity', 'fk_Scope_of_service', 'sum']

class One_time_contractFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains', label='Название')

    class Meta:
        model = One_time_contract
        fields ='__all__'
        exclude = ['cost', 'state', 'quantity', 'fk_Scope_of_service', 'sum']