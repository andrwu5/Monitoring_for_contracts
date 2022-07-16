from django.urls import path
from . import views
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = [

    path('', views.contract, name = 'contract_url'),
    path('one_time_contract', views.one_time_contract, name = 'one_time_contract_url'),
    path('one_time_contract_archive', views.one_time_contract_archive, name = 'one_time_contract_archive_url'),
    path('support_service', views.support_service, name = 'support_service_url'),
    path('contract_archive', views.contract_archive, name = 'contract_archive_url'),
    path('one_time_service', views.one_time_service, name = 'one_time_service_url'),
    path('client', views.client, name = 'client_url'),
    path('employee', views.employee, name = 'employee_url'),
    path('type_of_serv', views.type_of_serv, name = 'type_of_serv_url'),
    path('scope_of_serv', views.scope_of_serv, name = 'scope_of_serv_url'),
    path('share', views.share, name = 'share_url'),
    url(r'^login', views.LoginFormView.as_view(), name='login'),
    path('logout/', views.logout_view, name="logout"),
    path('support_service/create', views.Support_serviceCreateView.as_view(), name = 'support_service_create_url'),
    path('support_service/<int:support_service_id>', views.supp_serv_detail, name = 'supp_serv_detail_url'),
    path('support_service/<int:support_service_id>/update', views.Support_servicesUpdateView.as_view(), name = 'support_service_update_url'),
    path('support_service/<int:support_service_id>/delete', views.Support_serviceDelete.as_view(), name="support_service_delete_url"),
    path('one_time_service/create', views.One_time_serviceCreateView.as_view(), name = 'one_time_service_create_url'), 
    path('one_time_service/<int:one_time_service_id>', views.one_time_serv_detail, name = 'one_time_serv_detail_url'),
    path('one_time_service/<int:one_time_service_id>/update', views.One_time_servicesUpdateView.as_view(), name = 'one_time_service_update_url'),
    path('one_time_service/<int:one_time_service_id>/delete', views.One_time_serviceDelete.as_view(), name="one_time_service_delete_url"), 
    path('client/create', views.ClientCreateView.as_view(), name = 'client_create_url'),
    path('client/<int:client_id>', views.clients_detail, name = 'clients_detail_url'),
    path('client/<int:client_id>/update', views.ClientsUpdateView.as_view(), name = 'client_update_url'),
    path('client/<int:client_id>/delete', views.СlientDelete.as_view(), name="client_delete_url"),
    path('employee/create', views.EmployeeCreateView.as_view(), name = 'employee_create_url'),
    path('employee/<int:employee_id>', views.emp_detail, name = 'emp_detail_url'),
    path('employee/<int:employee_id>/update', views.EmployeeUpdateView.as_view(), name = 'emp_update_url'),
    path('employee/<int:employee_id>/delete', views.EmployeeDelete.as_view(), name="employee_delete_url"),
    path('contract/create', views.ContractCreateView, name = 'contract_create_url'),
    path('contract/<int:contract_id>', views.contractt_detail, name = 'contractt_detail_url'),
    path('contract/<int:contract_id>/update', views.ContractUpdateView.as_view(), name = 'contract_update_url'),
    path('contract/<int:contract_id>/delete', views.ContractDelete.as_view(), name="contract_delete_url"), 
    path('one_time_contract/create', views.One_time_contractCreateView, name = 'one_time_contract_create_url'),
    path('one_time_contract/<int:one_time_contract_id>', views.one_time_contractt_detail, name = 'one_time_contractt_detail_url'),
    path('one_time_contract/<int:one_time_contract_id>/update', views.One_time_contractUpdateView.as_view(), name = 'one_time_contract_update_url'),
    path('one_time_contract/<int:one_time_contract_id>/delete', views.One_time_contractDelete.as_view(), name="one_time_contract_delete_url"), 
    path('type_of_service/create', views.Type_of_serviceCreateView.as_view(), name = 'type_create_url'),
    path('type_of_service/<int:type_of_service_id>', views.type_of_serv_detail, name = 'type_of_serv_detail_url'),
    path('type_of_service/<int:type_of_service_id>/update', views.Type_of_serviceUpdateView.as_view(), name = 'type_of_serv_update_url'),
    path('type_of_service/<int:type_of_service_id>/delete', views.Type_of_serviceDelete.as_view(), name="type_of_service_delete_url"),
    path('scope_of_service/create', views.Scope_of_serviceCreateView.as_view(), name = 'scope_create_url'),
    path('scope_of_service/<int:scope_of_service_id>', views.scope_of_serv_detail, name = 'scope_of_serv_detail_url'),
    path('scope_of_service/<int:scope_of_service_id>/update', views.Scope_of_serviceUpdateView.as_view(), name = 'scope_of_serv_update_url'),
    path('scope_of_service/<int:scope_of_service_id>/delete', views.Scope_of_serviceDelete.as_view(), name="Scope_of_service_delete_url"),
    path('Client_export_excel', views.Client_export_excel, name="Client_export-excel"),
    path('Support_services_export_excel', views.Support_services_export_excel, name="Support_services_export-excel"),
    path('One_time_services_export_excel', views.One_time_services_export_excel, name="One_time_services_export-excel"),
    path('Type_of_service_export_excel', views.Type_of_service_export_excel, name="Type_of_service_export-excel"),
    path('Employee_export_excel', views.Employee_export_excel, name="Employee_export-excel"),
    path('Scope_of_service_export_excel', views.Scope_of_service_export_excel, name="Scope_of_service_export-excel"),
    path('Contract_export_excel', views.Contract_export_excel, name="Contract_export-excel"),
    path('One_time_contract_export_excel', views.One_time_contract_export_excel, name="One_time_contract_export-excel"),
    path('One_time_contract_archive_export_excel', views.One_time_contract_archive_export_excel, name="One_time_contract_archive_export-excel"),
    path('Contract_archive_export_excel', views.Contract_archive_export_excel, name="Contract_archive_export-excel"),
    path('One_time_contract_report_pdf', views.One_time_contract_report_pdf, name="One_time_contract_report-pdf"),
    path('One_time_contract_archive_report_pdf', views.One_time_contract_archive_report_pdf, name="One_time_contract_archive_report-pdf"),
    path('Contract_report_pdf', views.Contract_report_pdf, name="Contract_report-pdf"),
    path('Contract_archive_report_pdf', views.Contract_archive_report_pdf, name="Contract_archive_report-pdf"),

]