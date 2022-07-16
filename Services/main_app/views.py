from django.shortcuts import render, redirect, reverse
from .models import Support_services, One_time_services, Сlients, Employee, Contract, One_time_contract, Type_of_service, Scope_of_service
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.generic import View
from .forms import Support_servicesForm, One_time_servicesForm, СlientsForm, EmployeeForm, ContractForm, One_time_contractForm, Type_of_serviceForm, Scope_of_serviceForm, ContactForm
from django.core.mail import EmailMultiAlternatives, send_mail, BadHeaderError, EmailMessage
from django.template.loader import render_to_string, get_template
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.base import View, TemplateView
from django.views.generic.edit import FormView
from .filters import СlientsFilter, Type_of_serviceFilter, One_time_servicesFilter, Support_servicesFilter, EmployeeFilter, Scope_of_serviceFilter, ContractFilter, One_time_contractFilter
import xlwt
import datetime
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
#from tablib import Dataset
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from django.db.models import Sum
import xhtml2pdf.pisa as pisa

  

# Функция добавляния договора
def ContractCreateView (request):
    form = ContractForm()
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            quantity = request.POST['quantity']
            cost = request.POST['cost']
            name = request.POST['name']
            date = request.POST['date']
            state = False


            a = float(quantity)
            b = float(cost)
            if request.method == 'POST':
                form = СlientsForm()
                fk_clients = Сlients.objects.get(pk = request.POST.__getitem__('fk_clients'))
                        
                form = Support_servicesForm()
                fk_support_services = Support_services.objects.get(pk = request.POST.__getitem__('fk_support_services'))

                form = EmployeeForm()
                fk_employee = Employee.objects.get(pk = request.POST.__getitem__('fk_employee'))

                form = Scope_of_serviceForm()
                fk_Scope_of_service = Scope_of_service.objects.get(pk = request.POST.__getitem__('fk_Scope_of_service'))

                sum = a * b
            form = Contract(name=name, date=date, cost=cost, state=state, quantity=quantity, sum=sum, fk_clients = fk_clients, fk_support_services = fk_support_services, fk_employee = fk_employee, fk_Scope_of_service = fk_Scope_of_service)
            form.save()
        return redirect('contract_url')
    context = {'form' : form }
    return render(request, 'main_app/contract_create.html', context)

# Функция добавляния разового договора
def One_time_contractCreateView (request):
    form = One_time_contractForm()
    if request.method == 'POST':
        form = One_time_contractForm(request.POST)
        if form.is_valid():
            quantity = request.POST['quantity']
            cost = request.POST['cost']
            name = request.POST['name']
            date_from = request.POST['date_from']
            date_to = request.POST['date_to']
            state = False


            a = float(quantity)
            b = float(cost)
            if request.method == 'POST':
                form = СlientsForm()
                fk_clients = Сlients.objects.get(pk = request.POST.__getitem__('fk_clients'))
                        
                form = One_time_servicesForm()
                fk_one_time_services = One_time_services.objects.get(pk = request.POST.__getitem__('fk_one_time_services'))

                form = EmployeeForm()
                fk_employee = Employee.objects.get(pk = request.POST.__getitem__('fk_employee'))

                form = Scope_of_serviceForm()
                fk_Scope_of_service = Scope_of_service.objects.get(pk = request.POST.__getitem__('fk_Scope_of_service'))

                sum = a * b
            form = One_time_contract(name=name, date_from=date_from, date_to=date_to, cost=cost, state=state, quantity=quantity, sum=sum, fk_clients = fk_clients, fk_one_time_services = fk_one_time_services, fk_employee = fk_employee, fk_Scope_of_service = fk_Scope_of_service)
            form.save()
        return redirect('one_time_contract_url')
    context = {'form' : form }
    return render(request, 'main_app/one_time_contract_create.html', context)

# Функция отображения услуг поддержки, а также пагинация, поиск и фильтация
@login_required(login_url='login')
def support_service(request):
    support_services = Support_services.objects.all()

    myFilter = Support_servicesFilter(request.GET, queryset=support_services)
    support_services = myFilter.qs
    paginator = Paginator(support_services, 2)
    page = request.GET.get('page')
    try:
        support_services = paginator.page(page)
    except PageNotAnInteger:
        support_services = paginator.page(1)
    except EmptyPage:
        support_services = paginator.page(paginator.num_pages)
    return render(request, 'main_app/support_service.html', context={'support_services': support_services, 'myFilter' :myFilter})

# Функция отображения разовых услуг, а также пагинация, поиск и фильтация
@login_required(login_url='login')
def one_time_service(request):
    one_time_services = One_time_services.objects.all()

    myFilter = One_time_servicesFilter(request.GET, queryset=one_time_services)
    one_time_services = myFilter.qs
    paginator = Paginator(one_time_services, 2)
    page = request.GET.get('page')
    try:
        one_time_services = paginator.page(page)
    except PageNotAnInteger:
        one_time_services = paginator.page(1)
    except EmptyPage:
        one_time_services = paginator.page(paginator.num_pages)
    return render(request, 'main_app/one_time_service.html', context={'one_time_services': one_time_services, 'myFilter' :myFilter})

# Функция просмотра детальной информации
@login_required(login_url='login')
def supp_serv_detail(request, support_service_id):
    try:
        support_service = Support_services.objects.get(pk = support_service_id)
    except Support_services.DoesNotExist:
        raise Http404('Такой услуги поддержки не существует.')
    return render(request, 'main_app/support_service_detail.html', context = {'support_service': support_service})

# Функция изменения данных об услугах поддержки
class Support_servicesUpdateView(View):
    
    def get(self, request, support_service_id):
        support_service = Support_services.objects.get(pk = support_service_id)
        support_service_form = Support_servicesForm(instance = support_service)
        return render(request, 'main_app/support_service_detail.html', context = {'form': support_service_form  ,'data': support_service})

    def post(self, request, support_service_id):
        support_service = Support_services.objects.get(pk = support_service_id)
        support_service_form = Support_servicesForm(request.POST, instance = support_service)

        if support_service_form.is_valid():
            new_obj = support_service_form.save()
            return redirect(new_obj)
        return render(request, 'main_app/support_service_detail.html', context = {'form': support_service_form  ,'data': support_service})

# Функция добавления данных об услугах поддержки 
class Support_serviceCreateView(View):
    
    raise_exeption = True

    def get(self, request, *args, **kwargs):
        form = Support_servicesForm()
        return render(request, 'main_app/support_service_create.html', context = {'form': form})

        
    def post(self, request, *args, **kwargs):
        bound_form = Support_servicesForm(request.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, 'main_app/support_service_create.html', context = {'form': bound_form})


# Функция удаления данных об услугах поддержки
class Support_serviceDelete(View):

    def get(self, request, support_service_id):
        support_service = Support_services.objects.get(pk = support_service_id)
        return render(request, 'main_app/support_service_delete.html', context = {'data': support_service})

    def post(self, request, support_service_id):
        support_service = Support_services.objects.get(pk = support_service_id)
        support_service.delete()
        return redirect(reverse('support_service_url'))

# Функция просмотра детальной информации
@login_required(login_url='login')
def one_time_serv_detail(request, one_time_service_id):
    try:
        one_time_service = One_time_services.objects.get(pk = one_time_service_id)
    except One_time_services.DoesNotExist:
        raise Http404('Такой временной услуги не существует.')
    return render(request, 'main_app/one_time_service_detail.html', context = {'one_time_service': one_time_service})

# Функция обновления данных о разовых услугах
class One_time_servicesUpdateView(View):

    def get(self, request, one_time_service_id):
        one_time_service = One_time_services.objects.get(pk = one_time_service_id)
        one_time_service_form = One_time_servicesForm(instance = one_time_service)
        return render(request, 'main_app/one_time_service_detail.html', context = {'form': one_time_service_form  ,'data': one_time_service})

    def post(self, request, one_time_service_id):
        one_time_service = One_time_services.objects.get(pk = one_time_service_id)
        one_time_service_form = One_time_servicesForm(request.POST, instance = one_time_service)

        if one_time_service_form.is_valid():
            new_obj = one_time_service_form.save()
            return redirect(new_obj)
        return render(request, 'main_app/one_time_service_detail.html', context = {'form': one_time_service_form  ,'data': one_time_service})

# Функция добавления данных о разовых услугах
class One_time_serviceCreateView(View):
    raise_exeption = True

    def get(self, request, *args, **kwargs):
        form = One_time_servicesForm()
        return render(request, 'main_app/one_time_service_create.html', context = {'form': form})

        
    def post(self, request, *args, **kwargs):
        bound_form = One_time_servicesForm(request.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, 'main_app/one_time_service_create.html', context = {'form': bound_form})

# Функция удаления данных о разовых контрактах
class One_time_serviceDelete(View):

    def get(self, request, one_time_service_id):
        one_time_service = One_time_services.objects.get(pk = one_time_service_id)
        return render(request, 'main_app/one_time_service_delete.html', context = {'data': one_time_service})

    def post(self, request, one_time_service_id):
        one_time_service = One_time_services.objects.get(pk = one_time_service_id)
        one_time_service.delete()
        return redirect(reverse('index_url'))

# Функция отображения клиентов, а также пагинация, поиск и фильтация
@login_required(login_url='login')
def client(request):
    clients = Сlients.objects.all() 

    myFilter = СlientsFilter(request.GET, queryset=clients)
    clients = myFilter.qs
    paginator = Paginator(clients, 2)
    page = request.GET.get('page')
    try:
        clients = paginator.page(page)
    except PageNotAnInteger:
        clients = paginator.page(1)
    except EmptyPage:
        clients = paginator.page(paginator.num_pages)
    return render(request, 'main_app/client.html', context={'clients': clients, 'myFilter' :myFilter})

# Функция просмотра детальной инфомации о клиентах
@login_required(login_url='login')
def clients_detail(request, client_id):
    try:
        client = Сlients.objects.get(pk = client_id)
    except Сlients.DoesNotExist:
        raise Http404('Такой организации не существует.')
    return render(request, 'main_app/client_detail.html', context = {'client': client})

# Функция обновления данных о клиентах 
class ClientsUpdateView(View):

    def get(self, request, client_id):
        client = Сlients.objects.get(pk = client_id)
        client_form = СlientsForm(instance = client)
        return render(request, 'main_app/client_detail.html', context = {'form': client_form  ,'data': client})

    def post(self, request, client_id):
        client = Сlients.objects.get(pk = client_id)
        client_form = СlientsForm(request.POST, instance = client)

        if client_form.is_valid():
            new_obj = client_form.save()
            return redirect(new_obj)
        return render(request, 'main_app/client_detail.html', context = {'form': client_form  ,'data': client})

# Функция добавления данных о клиентах
class ClientCreateView(View):
    raise_exeption = True

    def get(self, request, *args, **kwargs):
        form = СlientsForm()
        return render(request, 'main_app/client_create.html', context = {'form': form})

        
    def post(self, request, *args, **kwargs):
        bound_form = СlientsForm(request.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, 'main_app/client_create.html', context = {'form': bound_form})

# Функция удаления данных о клиентах
class СlientDelete(View):

    def get(self, request, client_id):
        client = Сlients.objects.get(pk = client_id)
        return render(request, 'main_app/client_delete.html', context = {'data': client})

    def post(self, request, client_id):
        client = Сlients.objects.get(pk = client_id)
        client.delete()
        return redirect(reverse('index2_url'))

# Функция отображения рабочих групп, а также пагинация, поиск и фильтация
@login_required(login_url='login')
def employee(request):
    employees = Employee.objects.all() 

    myFilter = EmployeeFilter(request.GET, queryset=employees)
    employees = myFilter.qs
    paginator = Paginator(employees, 2)
    page = request.GET.get('page')
    try:
        employees = paginator.page(page)
    except PageNotAnInteger:
        employees = paginator.page(1)
    except EmptyPage:
        employees = paginator.page(paginator.num_pages)
    return render(request, 'main_app/employee.html', context={'employees': employees, 'myFilter' :myFilter})

# Функция просмотра детальной информации о рабочей группе
@login_required(login_url='login')
def emp_detail(request, employee_id):
    try:
        employee = Employee.objects.get(pk = employee_id)
    except Employee.DoesNotExist:
        raise Http404('Сотрудник не существует.')
    return render(request, 'main_app/employee_detail.html', context = {'employee': employee})

# Функция обновления информации о рабочих группах
class EmployeeUpdateView(View):

    def get(self, request, employee_id):
        employee = Employee.objects.get(pk = employee_id)
        employee_form = EmployeeForm(instance = employee)
        return render(request, 'main_app/employee_detail.html', context = {'form': employee_form  ,'data': employee})

    def post(self, request, employee_id):
        employee = Employee.objects.get(pk = employee_id)
        employee_form = EmployeeForm(request.POST, instance = employee)

        if employee_form.is_valid():
            new_obj = employee_form.save()
            return redirect(new_obj)
        return render(request, 'main_app/employee_detail.html', context = {'form': employee_form  ,'data': employee})

# Функция добавления данных о рабочих группах
class EmployeeCreateView(View):
    raise_exeption = True

    def get(self, request, *args, **kwargs):
        form = EmployeeForm()
        return render(request, 'main_app/employee_create.html', context = {'form': form})

        
    def post(self, request, *args, **kwargs):
        bound_form = EmployeeForm(request.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, 'main_app/employee_create.html', context = {'form': bound_form})

# Функция удаления данных о рабочих группах
class EmployeeDelete(View):

    def get(self, request, employee_id):
        employee = Employee.objects.get(pk = employee_id)
        return render(request, 'main_app/employee_delete.html', context = {'data': employee})

    def post(self, request, employee_id):
        employee = Employee.objects.get(pk = employee_id)
        employee.delete()
        return redirect(reverse('employee_url'))

# Функция отображения договоров в архиве, а также пагинация, поиск и фильтация
@login_required(login_url='login')    
def contract_archive(request):
    contracts = Contract.objects.filter(state = True)

    myFilter = ContractFilter(request.GET, queryset=contracts)
    contracts = myFilter.qs
    paginator = Paginator(contracts, 2)
    page = request.GET.get('page')
    try:
        contracts = paginator.page(page)
    except PageNotAnInteger:
        contracts = paginator.page(1)
    except EmptyPage:
        contracts = paginator.page(paginator.num_pages)
    return render(request, 'main_app/contract_archive.html', context={'contracts': contracts, 'myFilter' :myFilter})

# Функция отображения договоров, а также пагинация, поиск и фильтация
@login_required(login_url='login')  
def contract(request):
    contracts = Contract.objects.filter(state = False)

    myFilter = ContractFilter(request.GET, queryset=contracts)
    contracts = myFilter.qs
    paginator = Paginator(contracts, 2)
    page = request.GET.get('page')
    try:
        contracts = paginator.page(page)
    except PageNotAnInteger:
        contracts = paginator.page(1)
    except EmptyPage:
        contracts = paginator.page(paginator.num_pages)
    return render(request, 'main_app/contract.html', {"contracts": contracts,'myFilter': myFilter})

# Функция отображения разовых договоров, а также пагинация, поиск и фильтация
@login_required(login_url='login')  
def one_time_contract(request):
    one_time_contracts = One_time_contract.objects.filter(state = False)

    myFilter = One_time_contractFilter(request.GET, queryset=one_time_contracts)
    one_time_contracts = myFilter.qs
    paginator = Paginator(one_time_contracts, 2)
    page = request.GET.get('page')
    try:
        one_time_contracts = paginator.page(page)
    except PageNotAnInteger:
        one_time_contracts = paginator.page(1)
    except EmptyPage:
        one_time_contracts = paginator.page(paginator.num_pages)
    return render(request, 'main_app/one_time_contract.html', {"one_time_contracts": one_time_contracts,'myFilter': myFilter})

# Функция отображения разовых договоров в архиве, а также пагинация, поиск и фильтация
@login_required(login_url='login')    
def one_time_contract_archive(request):
    one_time_contracts = One_time_contract.objects.filter(state = True)

    myFilter = One_time_contractFilter(request.GET, queryset=one_time_contracts)
    one_time_contracts = myFilter.qs
    paginator = Paginator(one_time_contracts, 2)
    page = request.GET.get('page')
    try:
        one_time_contracts = paginator.page(page)
    except PageNotAnInteger:
        one_time_contracts = paginator.page(1)
    except EmptyPage:
        one_time_contracts = paginator.page(paginator.num_pages)
    return render(request, 'main_app/one_time_contract_archive.html', context={'one_time_contracts': one_time_contracts, 'myFilter' :myFilter})

# Функция просмотра детальной информации о разовых договорах
@login_required(login_url='login')
def one_time_contractt_detail(request, one_time_contract_id):
    try:
        one_time_contract = One_time_contract.objects.get(pk = one_time_contract_id)
    except One_time_contract.DoesNotExist:
        raise Http404('Такой разовый договор не существует.')
    return render(request, 'main_app/one_time_contract_detail.html', context = {'one_time_contract': one_time_contract})

# Функция обновления данных о разовых договорах
class One_time_contractUpdateView(View):

    def get(self, request, one_time_contract_id):
        one_time_contract = One_time_contract.objects.get(pk = one_time_contract_id)
        one_time_contract_form = One_time_contractForm(instance = one_time_contract)
        return render(request, 'main_app/one_time_contract_detail.html', context = {'form': one_time_contract_form  ,'data': one_time_contract})

    def post(self, request, one_time_contract_id):
        one_time_contract = One_time_contract.objects.get(pk = one_time_contract_id)
        one_time_contract_form = One_time_contractForm(request.POST, instance = one_time_contract)

        if one_time_contract_form.is_valid():
            new_obj = one_time_contract_form.save()
            return redirect(new_obj)
        return render(request, 'main_app/one_time_contract_detail.html', context = {'form': one_time_contract_form  ,'data': one_time_contract})


# Функция удаления данных о разовых договорах
class One_time_contractDelete(View):

    def get(self, request, one_time_contract_id):
        one_time_contract = One_time_contract.objects.get(pk = one_time_contract_id)
        return render(request, 'main_app/one_time_contract_delete.html', context = {'data': one_time_contract})

    def post(self, request, one_time_contract_id):
        one_time_contract = One_time_contract.objects.get(pk = one_time_contract_id)
        one_time_contract.delete()
        return redirect(reverse('contract_url'))

# Функция просмотра детальной информации о договорах
@login_required(login_url='login')
def contractt_detail(request, contract_id):
    try:
        contract = Contract.objects.get(pk = contract_id)
    except Contract.DoesNotExist:
        raise Http404('Такой договор не существует.')
    return render(request, 'main_app/contract_detail.html', context = {'contract': contract})

# Функция добавления данных о договорах
class ContractUpdateView(View):

    def get(self, request, contract_id):
        contract = Contract.objects.get(pk = contract_id)
        contract_form = ContractForm(instance = contract)
        return render(request, 'main_app/contract_detail.html', context = {'form': contract_form  ,'data': contract})

    def post(self, request, contract_id):
        contract = Contract.objects.get(pk = contract_id)
        contract_form = ContractForm(request.POST, instance = contract)

        if contract_form.is_valid():
            new_obj = contract_form.save()
            return redirect(new_obj)
        return render(request, 'main_app/contract_detail.html', context = {'form': contract_form  ,'data': contract})



# Функция удаления данных о договорах
class ContractDelete(View):

    def get(self, request, contract_id):
        contract = Contract.objects.get(pk = contract_id)
        return render(request, 'main_app/contract_delete.html', context = {'data': contract})

    def post(self, request, contract_id):
        contract = Contract.objects.get(pk = contract_id)
        contract.delete()
        return redirect(reverse('contract_url'))        

# Функция отображения типов услуг, а также пагинация, поиск и фильтация
@login_required(login_url='login')
def type_of_serv(request):
    type_of_services = Type_of_service.objects.all() 

    myFilter = Type_of_serviceFilter(request.GET, queryset=type_of_services)
    type_of_services = myFilter.qs
    paginator = Paginator(type_of_services, 2)
    page = request.GET.get('page')
    try:
        type_of_services = paginator.page(page)
    except PageNotAnInteger:
        type_of_services = paginator.page(1)
    except EmptyPage:
        type_of_services = paginator.page(paginator.num_pages)
    return render(request, 'main_app/type_of_serv.html', context={'type_of_services': type_of_services, 'myFilter' :myFilter})

# Функция просмотра детальной информации о типах услуг
@login_required(login_url='login')
def type_of_serv_detail(request, type_of_service_id):
    try:
        type_of_service = Type_of_service.objects.get(pk = type_of_service_id)
    except Type_of_service.DoesNotExist:
        raise Http404('Такого типа услуг не существует не существует.')
    return render(request, 'main_app/type_of_service_detail.html', context = {'type_of_service': type_of_service})

# Функция обновления данных о типах услуги
class Type_of_serviceUpdateView(View):

    def get(self, request, type_of_service_id):
        type_of_service = Type_of_service.objects.get(pk = type_of_service_id)
        type_of_service_form = Type_of_serviceForm(instance = type_of_service)
        return render(request, 'main_app/type_of_service_detail.html', context = {'form': type_of_service_form  ,'data': type_of_service})

    def post(self, request, type_of_service_id):
        type_of_service = Type_of_service.objects.get(pk = type_of_service_id)
        type_of_service_form = Type_of_serviceForm(request.POST, instance = type_of_service)

        if type_of_service_form.is_valid():
            new_obj = type_of_service_form.save()
            return redirect(new_obj)
        return render(request, 'main_app/type_of_service_detail.html', context = {'form': type_of_service_form  ,'data': type_of_service})

# Функция отображения информации об используемых средствах
@login_required(login_url='login')
def scope_of_serv(request):
    scope_of_services = Scope_of_service.objects.all() 

    myFilter = Scope_of_serviceFilter(request.GET, queryset=scope_of_services)
    scope_of_services = myFilter.qs
    paginator = Paginator(scope_of_services, 2)
    page = request.GET.get('page')
    try:
        scope_of_services = paginator.page(page)
    except PageNotAnInteger:
        scope_of_services = paginator.page(1)
    except EmptyPage:
        scope_of_services = paginator.page(paginator.num_pages)
    return render(request, 'main_app/scope_of_service.html', context={'scope_of_services': scope_of_services, 'myFilter' :myFilter})

# Функция просмотра детальной информации об используемых средствах
@login_required(login_url='login')
def scope_of_serv_detail(request, scope_of_service_id):
    try:
        scope_of_service = Scope_of_service.objects.get(pk = scope_of_service_id)
    except Scope_of_service.DoesNotExist:
        raise Http404('Такого объема услуги не существует не существует.')
    return render(request, 'main_app/scope_of_service_detail.html', context = {'scope_of_service': scope_of_service})

# Функция добавления данных о типах услуг
class Type_of_serviceCreateView(View):
    raise_exeption = True

    def get(self, request, *args, **kwargs):
        form = Type_of_serviceForm()
        return render(request, 'main_app/type_create.html', context = {'form': form})

        
    def post(self, request, *args, **kwargs):
        bound_form = Type_of_serviceForm(request.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, 'main_app/type_create.html', context = {'form': bound_form})

# Функция удаления данных о типах услуг
class Type_of_serviceDelete(View):

    def get(self, request, type_of_service_id):
        type_of_service = Type_of_service.objects.get(pk = type_of_service_id)
        return render(request, 'main_app/type_of_service_delete.html', context = {'data': type_of_service})

    def post(self, request, type_of_service_id):
        type_of_service = Type_of_service.objects.get(pk = type_of_service_id)
        type_of_service.delete()
        return redirect(reverse('type_of_serv_url'))

# Функция обновления данных об используемых средствах
class Scope_of_serviceUpdateView(View):

    def get(self, request, scope_of_service_id):
        scope_of_service = Scope_of_service.objects.get(pk = scope_of_service_id)
        scope_of_service_form = Scope_of_serviceForm(instance = scope_of_service)
        return render(request, 'main_app/scope_of_service_detail.html', context = {'form': scope_of_service_form  ,'data': scope_of_service})

    def post(self, request, scope_of_service_id):
        scope_of_service = Scope_of_service.objects.get(pk = scope_of_service_id)
        scope_of_service_form = Scope_of_serviceForm(request.POST, instance = scope_of_service)

        if scope_of_service_form.is_valid():
            new_obj = scope_of_service_form.save()
            return redirect(new_obj)
        return render(request, 'main_app/scope_of_service_detail.html', context = {'form': scope_of_service_form  ,'data': scope_of_service})

# Функция добавления данных об используемых средствах
class Scope_of_serviceCreateView(View):
    raise_exeption = True

    def get(self, request, *args, **kwargs):
        form = Scope_of_serviceForm()
        return render(request, 'main_app/scope_create.html', context = {'form': form})

        
    def post(self, request, *args, **kwargs):
        bound_form = Scope_of_serviceForm(request.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, 'main_app/scope_create.html', context = {'form': bound_form})

# Функция удаления данных об используемых средствах
class Scope_of_serviceDelete(View):

    def get(self, request, scope_of_service_id):
        scope_of_service = Scope_of_service.objects.get(pk = scope_of_service_id)
        return render(request, 'main_app/Scope_of_service_delete.html', context = {'data': scope_of_service})

    def post(self, request, scope_of_service_id):
        scope_of_service = Scope_of_service.objects.get(pk = scope_of_service_id)
        scope_of_service.delete()
        return redirect(reverse('scope_of_serv_url'))
        

# Функция отправки сообщения на gmail с этой же почты
@login_required(login_url='login')
def share(request):
    form = ContactForm()
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = EmailMessage(subject, message, 'andrwuITL@gmail.com', ['andrwuITL@gmail.com'])
            email.send()
    else:
        form = ContactForm()
    return render(request, 'main_app/share.html', context ={"form": form})



# Функция авторизации
class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "main_app/login.html"
    success_url = "/"
    
    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

# Функция выхода из аккаунта
def logout_view(request):
    logout(request)
    return redirect('/')


# Функция экспорта данных о клиентах в Excel
def Client_export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="clients.xls"'
 
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Клиенты')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True


    columns = ['Название организации', 'Адрес', 'Контактное лицо', 'Номер телефон', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) 

 
    font_style = xlwt.XFStyle()

    rows = Сlients.objects.all().values_list('name_of_the_organization', 'address', 'contact_person', 'phone_number')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)

    return response

# Функция экспорта данных об услугах поддержки в Excel
def Support_services_export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Support_services.xls"'
 
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Услуги поддержки')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True


    columns = ['Название услуги поддержки',]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) 

 
    font_style = xlwt.XFStyle()

    rows = Support_services.objects.all().values_list('name')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)

    return response

# Функция экспорта данных о разовых услугах в Excel
def One_time_services_export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="One_time_services.xls"'
 
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Разовые услуги')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True


    columns = ['Название разовой услуги',]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) 

 
    font_style = xlwt.XFStyle()

    rows = One_time_services.objects.all().values_list('name')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)

    return response

# Функция экспорта данных о типах услуг в Excel
def Type_of_service_export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Type_of_service.xls"'
 
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Типы услуг')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True


    columns = ['Название типа услуги',]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) 

 
    font_style = xlwt.XFStyle()

    rows = Type_of_service.objects.all().values_list('name')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)

    return response

# Функция экспорта данных о рабочих группах в Excel
def Employee_export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Employee.xls"'
 
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Рабочие группы')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True


    columns = ['Название рабочей группы',]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) 

 
    font_style = xlwt.XFStyle()

    rows = Employee.objects.all().values_list('working_group_name')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)

    return response

# Функция экспорта данных об используемых средствах в Excel
def Scope_of_service_export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Scope_of_service.xls"'
 
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Объем услуг')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True


    columns = ['Название объема услуг',]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) 

 
    font_style = xlwt.XFStyle()

    rows = Scope_of_service.objects.all().values_list('name')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)

    return response

# Функция экспорта данных о договорах в Excel
def Contract_export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Contract.xls"'
 
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Договоры')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True


    columns = ['Название договороа', 'Дата', 'Количество', 'Цена',]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) 

 
    font_style = xlwt.XFStyle()

    rows = Contract.objects.filter(state = False).values_list('name', 'date', 'quantity', 'cost')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)

    return response

# Функция экспорта данных о разовых договорах в Excel
def One_time_contract_export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="One_time_contract.xls"'
 
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Разовые договоры')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Название договороа', 'Дата с', 'Дата по', 'Количество', 'Цена',]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) 

 
    font_style = xlwt.XFStyle()

    rows = One_time_contract.objects.filter(state = False).values_list('name', 'date_from', 'date_to', 'quantity', 'cost')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)

    return response

# Функция экспорта данных о разовых договорах в архиве в Excel
def One_time_contract_archive_export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="One_time_contract_archive.xls"'
 
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Разовые договоры')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Название договороа', 'Дата с', 'Дата по', 'Количество', 'Цена',]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) 

 
    font_style = xlwt.XFStyle()

    rows = One_time_contract.objects.filter(state = True).values_list('name', 'date_from', 'date_to', 'quantity', 'cost')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)

    return response

# Функция экспорта данных о договорах в архиве в Excel
def Contract_archive_export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Contract_archive.xls"'
 
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Договоры')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True


    columns = ['Название договороа', 'Дата', 'Количество', 'Цена',]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) 

 
    font_style = xlwt.XFStyle()

    rows = Contract.objects.filter(state = True).values_list('name', 'date', 'quantity', 'cost')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)

    return response

# Функция экспорта данных о разовых договорах в pdf
def One_time_contract_report_pdf(request):
    one_time_contracts = One_time_contract.objects.filter(state = False)

    template_path = 'main_app/one_time_contract_report.html'
    context = {'one_time_contracts': one_time_contracts}

    response = HttpResponse(content_type='application/pdf')
    
    response['Content-Disposition'] = 'attachment; filename="one_time_contracts.pdf"'

    template = get_template(template_path)
    
    html = template.render(context)

    pisa_status = pisa.CreatePDF(
        html, dest=response, encoding='UTF-8')

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

# Функция экспорта данных о разовых договорах в архиве в pdf
def One_time_contract_archive_report_pdf(request):
    one_time_contracts = One_time_contract.objects.filter(state = True)

    template_path = 'main_app/one_time_contract_report.html'
    context = {'one_time_contracts': one_time_contracts}

    response = HttpResponse(content_type='application/pdf')
    
    response['Content-Disposition'] = 'attachment; filename="one_time_contracts_archive.pdf"'

    template = get_template(template_path)
    
    html = template.render(context)

    pisa_status = pisa.CreatePDF(
        html, dest=response, encoding='UTF-8')

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

# Функция экспорта данных о договорах в pdf
def Contract_report_pdf(request):
    contracts = Contract.objects.filter(state = False)

    template_path = 'main_app/contract_report.html'
    context = {'contracts': contracts}

    response = HttpResponse(content_type='application/pdf')
    
    response['Content-Disposition'] = 'attachment; filename="contracts.pdf"'

    template = get_template(template_path)
    
    html = template.render(context)

    pisa_status = pisa.CreatePDF(
        html, dest=response, encoding='UTF-8')

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

# Функция экспорта данных о договорах в архиве в pdf
def Contract_archive_report_pdf(request):
    contracts = Contract.objects.filter(state = True)

    template_path = 'main_app/contract_report.html'
    context = {'contracts': contracts}

    response = HttpResponse(content_type='application/pdf')
    
    response['Content-Disposition'] = 'attachment; filename="contracts_archive.pdf"'

    template = get_template(template_path)
    
    html = template.render(context)

    pisa_status = pisa.CreatePDF(
        html, dest=response, encoding='UTF-8')

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response