from django.db import models
from django.shortcuts import reverse 

class Сlients(models.Model):

    name_of_the_organization = models.CharField(verbose_name = 'Название организации', max_length=50)
    address = models.CharField(verbose_name = 'Адрес', max_length=60)
    contact_person = models.CharField(verbose_name = 'Контактное лицо', max_length=30)
    phone_number = models.BigIntegerField(verbose_name = 'Номер телефона')

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиент"

    def __str__(self):
        return self.contact_person

    def get_absolute_url(self):
        return reverse("clients_detail_url", kwargs={"client_id": self.pk})

    def get_update_url(self):
        return reverse("client_update_url", kwargs={"client_id": self.pk})

    def get_delete_url(self):
        return reverse("client_delete_url", kwargs={"client_id": self.pk})

class Employee(models.Model):

    working_group_name = models.CharField(verbose_name = 'Имя', max_length=30)

    class Meta:
        verbose_name = "Рабочая группа"
        verbose_name_plural = "Рабочая группа"

    def __str__(self):
        return self.working_group_name
    
    def get_absolute_url(self):
        return reverse("emp_detail_url", kwargs={"employee_id": self.pk})
    
    def get_update_url(self):
        return reverse("emp_update_url", kwargs={"employee_id": self.pk})

    def get_delete_url(self):
        return reverse("employee_delete_url", kwargs={"employee_id": self.pk})

class Scope_of_service(models.Model):

    name = models.CharField(verbose_name = 'Название', max_length=50)

    class Meta:
        verbose_name = "Объем услуги"
        verbose_name_plural = "Объем услуги"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("scope_of_serv_detail_url", kwargs={"scope_of_service_id": self.pk})
    
    def get_update_url(self):
        return reverse("scope_of_serv_update_url", kwargs={"scope_of_service_id": self.pk})
    
    def get_delete_url(self):
        return reverse("Scope_of_service_delete_url", kwargs={"scope_of_service_id": self.pk})

class Type_of_service(models.Model):

    name = models.CharField(verbose_name = 'Название', max_length=30)

    class Meta:
        verbose_name = "тип услуги"
        verbose_name_plural = "тип услуги"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("type_of_serv_detail_url", kwargs={"type_of_service_id": self.pk})

    def get_update_url(self):
        return reverse("type_of_serv_update_url", kwargs={"type_of_service_id": self.pk})
    
    def get_delete_url(self):
        return reverse("type_of_service_delete_url", kwargs={"type_of_service_id": self.pk})

class Support_services(models.Model):

    name = models.CharField(verbose_name = 'Название', max_length=50)
    short_name = models.CharField(verbose_name = 'Краткое наименование', max_length=25)
   

    
    class Meta:
        verbose_name = "Услуга поддержки"
        verbose_name_plural = "Услуга поддержки"

    def __str__(self):
        return self.short_name

    def get_absolute_url(self):
        return reverse("supp_serv_detail_url", kwargs={"support_service_id": self.pk})

    def get_update_url(self):
        return reverse("support_service_update_url", kwargs={"support_service_id": self.pk})
    
    def get_delete_url(self):
        return reverse("support_service_delete_url", kwargs={"support_service_id": self.pk})

class One_time_services(models.Model):

    name = models.CharField(verbose_name = 'Название', max_length=50)
    short_name = models.CharField(verbose_name = 'Краткое наименование', max_length=25)
    

    
    class Meta:
        verbose_name = "Разовая Услуга"
        verbose_name_plural = "Разовая Услуга"

    def __str__(self):
        return self.short_name

    def get_absolute_url(self):
        return reverse("one_time_serv_detail_url", kwargs={"one_time_service_id": self.pk})

    def get_update_url(self):
        return reverse("one_time_service_update_url", kwargs={"one_time_service_id": self.pk})
    
    def get_delete_url(self):
        return reverse("one_time_service_delete_url", kwargs={"one_time_service_id": self.pk})

class Contract(models.Model):

    name = models.CharField(verbose_name = 'Название', max_length=30)
    date = models.DateField(verbose_name = 'Дата')
    cost = models.FloatField(verbose_name = 'Цена', max_length=9)
    state = models.BooleanField(verbose_name = 'Статус', default=True)
    quantity = models.IntegerField(verbose_name = 'Количество')
    fk_clients = models.ForeignKey(Сlients, verbose_name= 'Клиент', on_delete=models.SET_NULL, blank=True, null=True)
    fk_support_services = models.ForeignKey(Support_services, verbose_name= 'Услуга поддержки', on_delete=models.SET_NULL, blank=True, null=True)
    fk_employee = models.ForeignKey(Employee, verbose_name= 'Рабочая группа', on_delete=models.SET_NULL, blank=True, null=True)
    fk_Scope_of_service = models.ForeignKey(Scope_of_service, verbose_name= 'Объем услуги', on_delete=models.SET_NULL, blank=True, null=True)
    sum = models.FloatField(verbose_name = 'Сумма', null=True)
    class Meta:
        verbose_name = "Договор"
        verbose_name_plural = "Договор"
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("contractt_detail_url", kwargs={"contract_id": self.pk})

    def get_update_url(self):
        return reverse("contract_update_url", kwargs={"contract_id": self.pk})
    
    def get_delete_url(self):
        return reverse("contract_delete_url", kwargs={"contract_id": self.pk})

class One_time_contract(models.Model):

    name = models.CharField(verbose_name = 'Название', max_length=30)
    date_from = models.DateField(verbose_name = 'Дата с')
    date_to = models.DateField(verbose_name = 'Дата по')
    state = models.BooleanField(verbose_name = 'Статус', default=True)
    cost = models.FloatField(verbose_name = 'Цена', max_length=9)
    quantity = models.IntegerField(verbose_name = 'Количество')
    fk_clients = models.ForeignKey(Сlients, verbose_name= 'Клиент', on_delete=models.SET_NULL, blank=True, null=True)
    fk_one_time_services = models.ForeignKey(One_time_services, verbose_name= 'Разовая услуга', on_delete=models.SET_NULL, blank=True, null=True)
    fk_Scope_of_service = models.ForeignKey(Scope_of_service, verbose_name= 'Объем услуги', on_delete=models.SET_NULL, blank=True, null=True)
    fk_employee = models.ForeignKey(Employee, verbose_name= 'Рабочая группа', on_delete=models.SET_NULL, blank=True, null=True)
    sum = models.FloatField(verbose_name = 'Сумма', null=True)
    class Meta:
        verbose_name = "Разовый договор"
        verbose_name_plural = "Разовый договор"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("one_time_contractt_detail_url", kwargs={"one_time_contract_id": self.pk})    

    def get_update_url(self):
        return reverse("one_time_contract_update_url", kwargs={"one_time_contract_id": self.pk})

    def get_delete_url(self):
        return reverse("one_time_contract_delete_url", kwargs={"one_time_contract_id": self.pk})





