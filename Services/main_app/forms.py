from django import forms
from .models import Support_services, One_time_services, Сlients, Employee, Contract, One_time_contract, Type_of_service, Scope_of_service

class ContactForm(forms.Form):
    subject = forms.CharField(label='Тема',max_length=80, min_length=5)
    message = forms.CharField(label='Cообщение', widget=forms.Textarea, max_length=600, required=False)



class Support_servicesForm(forms.ModelForm):
    
    class Meta:
        model = Support_services
        fields = ('name', 'short_name', )
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'short_name': forms.TextInput(attrs={'class':'form-control'})
        }

class One_time_servicesForm(forms.ModelForm):
    
    class Meta:
        model = One_time_services
        fields = ('name', 'short_name', )
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'short_name': forms.TextInput(attrs={'class':'form-control'})
        }

class СlientsForm(forms.ModelForm):
    
    class Meta:
        model = Сlients
        fields = ('name_of_the_organization', 'address', 'contact_person', 'phone_number', )
        widgets = {
            'name_of_the_organization': forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'contact_person': forms.TextInput(attrs={'class':'form-control'}),
            'phone_number': forms.TextInput(attrs={'class':'form-control'})
        }

class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = ('working_group_name', )
        widgets = {
            'working_group_name': forms.TextInput(attrs={'class':'form-control'})
        }

class ContractForm(forms.ModelForm):
    
    class Meta:
        model = Contract
        fields = ('name', 'fk_clients', 'date', 'fk_support_services', 'fk_employee', 'fk_Scope_of_service', 'quantity', 'cost', 'state', )
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'fk_clients': forms.Select(attrs={'class':'form-control'}),
            'date': forms.DateInput(attrs={'class':'form-control'}),
            'fk_support_services': forms.Select(attrs={'class':'form-control'}),
            'fk_employee': forms.Select(attrs={'class':'form-control'}),
            'fk_Scope_of_service': forms.Select(attrs={'class':'form-control'}),
            'quantity': forms.TextInput(attrs={'class':'form-control'}),
            'cost': forms.TextInput(attrs={'class':'form-control'}),
            
        }

class One_time_contractForm(forms.ModelForm):
    
    class Meta:
        model = One_time_contract
        fields = ('name', 'fk_clients', 'date_from', 'date_to', 'fk_one_time_services', 'fk_employee', 'fk_Scope_of_service', 'quantity', 'cost', 'state', )
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'fk_clients': forms.Select(attrs={'class':'form-control'}),
            'date_from': forms.DateInput(attrs={'class':'form-control'}),
            'date_to': forms.DateInput(attrs={'class':'form-control'}),
            'fk_one_time_services': forms.Select(attrs={'class':'form-control'}),
            'fk_employee': forms.Select(attrs={'class':'form-control'}),
            'fk_Scope_of_service': forms.Select(attrs={'class':'form-control'}),
            'quantity': forms.TextInput(attrs={'class':'form-control'}),
            'cost': forms.TextInput(attrs={'class':'form-control'}),
        }

class Type_of_serviceForm(forms.ModelForm):
    
    class Meta:
        model = Type_of_service
        fields = ('name', )
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),

        }

class Scope_of_serviceForm(forms.ModelForm):
    
    class Meta:
        model = Scope_of_service
        fields = ('name', )
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'})
        }