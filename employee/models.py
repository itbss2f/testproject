from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse_lazy
import datetime
# from geography.models import ZipCode

# Create your models here.


class Department(models.Model):
    code = models.CharField(max_length=20, null=False)
    name = models.CharField(max_length=30, null=False)
    company_id = models.IntegerField(default=1)
    date_added = models.DateTimeField(null=True)

    class Meta:
        db_table = 'inq_departments'
        ordering = ['id']
        # permission = (("department", "Can access department"),
        #

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Employee(models.Model):
    user_id = models.CharField(max_length=16, null=True)
    company = models.ForeignKey('employee.Company', default=1, null=False)
    code = models.CharField(max_length=30, null=False)
    first_name = models.CharField(max_length=64, null=False)
    middle_name = models.CharField(max_length=64, blank=True, null=True)
    last_name = models.CharField(max_length=64, null=False)
    email = models.EmailField(max_length=128, null=True)
    telnum = models.CharField(max_length=32, null=True, blank=True)
    cphonenum = models.CharField(max_length=32, null=True, blank=True)
    gender = models.IntegerField(null=True)
    dob = models.DateTimeField(null=True)
    pob = models.CharField(max_length=32, null=True)
    religion = models.ForeignKey('employee.Religion', null=True)
    civil_status = models.ForeignKey('employee.Civil_status', default=1, null=False)
    position_level = models.ForeignKey('employee.Levels', null=True)
    designation = models.IntegerField(null=True, blank=True)
    division = models.IntegerField(null=True)
    department = models.ForeignKey('employee.Department', null=True)
    status = models.ForeignKey('employee.Status', null=True)
    date_hired = models.DateField(null=True)
    date_resigned = models.DateTimeField(null=True)
    cardno = models.IntegerField(null=True, blank=True)
    sssno = models.CharField(max_length=16, null=True, blank=True)
    tin = models.CharField(max_length=16, null=True, blank=True)
    pagibig = models.CharField(max_length=16, null=True, blank=True)
    philhealth = models.CharField(max_length=16, null=True, blank=True)
    branch_assigned = models.ForeignKey('employee.Branch', null=True)
    address = models.ForeignKey('employee.Address', null=True)
    nationality = models.ForeignKey('employee.Nationality', default=1, null=False)
    #employee_address = models.ManyToManyField('employee.EmployeeAddress')
    employee_position = models.ManyToManyField('employee.EmployeePosition')
    employee_family = models.ManyToManyField('employee.EmployeeFamily')
    employment_record = models.ManyToManyField('employee.EmploymentRecord')
    employee_primary = models.ManyToManyField('employee.Primary')
    employee_secondary = models.ManyToManyField('employee.Secondary')
    employee_college = models.ManyToManyField('employee.College')
    contactperson = models.ForeignKey('employee.ContactPerson', null=True)
    is_deleted = models.IntegerField(default=0)
    date_entered = models.DateTimeField(default=datetime.datetime.now())
    date_modify = models.DateTimeField(null=True)

    # Example
    # def save(self, *args, **kwargs):
    #     if self.name == "Yoko Ono's blog":
    #         return # Yoko shall never have her own blog!
    #     else:
    #         super().save(*args, **kwargs)  # Call the "real" save() method.

    def save(self, force_insert=False, force_update=False):
        self.first_name = self.first_name.upper()
        self.middle_name = self.middle_name.upper()
        self.last_name = self.last_name.upper()
        self.pob = self.pob.upper()
        self.date_modify = datetime.datetime.now()
        super(Employee, self).save(force_insert, force_update)

    class Meta:
        db_table = 'inq_employees'
        ordering = ['id']
        # permission = (("employee", "Can access employee"),
        #               ("view_employee", "Can view employee"))

    def __str__(self):
        return self.code

    def __unicode__(self):
        return self.code

    # reverse the url and saving without loading the page.
    def get_absolute_url(self):
        return reverse_lazy('employee:update', args=[str(self.pk)])


class EmploymentRecord(models.Model):
    e_emp = models.ForeignKey(Employee, null=True)
    cname = models.CharField(max_length=64, null=True, blank=True)
    yearfrom = models.DateTimeField(null=True)
    yearto = models.DateTimeField(null=True)
    company_id = models.IntegerField(null=True)
    date_entered = models.DateTimeField(default=datetime.datetime.now())
    #date_enteredby = models.ForeignKey(User, default=1, related_name='address_enteredby')
    date_modify = models.DateTimeField(null=True)
    #modify_by = models.ForeignKey(User, default=1, related_name='address_modify')
    is_deleted = models.IntegerField(default=0)


    class Meta:
        db_table = 'inq_employment_record'
        ordering = ['id']

    def __str__(self):
        return self.cname

    def __unicode__(self):
        return self.cname


class Address(models.Model):
    a_house_num = models.CharField(max_length=64, null=True, blank=True)
    a_street_subd = models.CharField(max_length=64, null=True, blank=True)
    a_barangay = models.CharField(max_length=64, null=True, blank=True)
    a_province = models.ForeignKey('employee.Province', null=True, blank=True)
    a_city = models.ForeignKey('employee.Cities', null=True, blank=True)
    # a_zipcode = models.IntegerField(null=True)
    p_house_num = models.CharField(max_length=64, null=True, blank=True)
    p_street_subd = models.CharField(max_length=64, null=True, blank=True)
    p_barangay = models.CharField(max_length=64, null=True, blank=True)
    p_province = models.ForeignKey('employee.Provincial', null=True, blank=True)
    p_city = models.ForeignKey('employee.City', null=True, blank=True)
    # p_zipcode = models.IntegerField(null=True)
    company_id = models.IntegerField(null=True)
    date_entered = models.DateTimeField(default=datetime.datetime.now())
    #date_enteredby = models.ForeignKey(User, default=1, related_name='address_enteredby')
    date_modify = models.DateTimeField(null=True)
    #modify_by = models.ForeignKey(User, default=1, related_name=

    def save(self, force_insert=False, force_update=False):
        self.a_street_subd = self.a_street_subd.title()
        self.a_barangay = self.a_barangay.title()
        self.p_street_subd = self.p_street_subd.title()
        self.p_barangay = self.p_barangay.title()
        super(Address, self).save(force_insert, force_update)

    class Meta:
        db_table = 'inq_address'
        ordering = ['id']

    def __str__(self):
        return self.company_id

    def __unicode__(self):
        return self.company_id


class ContactPerson(models.Model):
    cfirst_name = models.CharField(max_length=64, null=True, blank=True)
    cmiddle_name = models.CharField(max_length=64, blank=True, null=True)
    clast_name = models.CharField(max_length=64, null=True, blank=True)
    ctelnum = models.CharField(max_length=64, null=True, blank=True)
    ccpnum = models.CharField(max_length=64, null=True, blank=True)
    company_id = models.IntegerField(null=True)
    date_entered = models.DateTimeField(default=datetime.datetime.now())
    #date_enteredby = models.ForeignKey(User, default=1, related_name='address_enteredby')
    date_modify = models.DateTimeField(null=True)
    #modify_by = models.ForeignKey(User, default=1, related_name='address_modify')

    def save(self, force_insert=False, force_update=False):
        self.cfirst_name = self.cfirst_name.upper()
        self.cmiddle_name = self.cmiddle_name.upper()
        self.clast_name = self.clast_name.upper()
        super(ContactPerson, self).save(force_insert, force_update)

    class Meta:
        db_table = 'inq_contactperson'
        ordering = ['id']

    def __str__(self):
        return self.cfirst_name

    def __unicode__(self):
        return self.cfirst_name


class EmployeeFamily(models.Model):
    f_emp = models.ForeignKey(Employee, null=True)
    fam_first_name = models.CharField(max_length=64, null=True, blank=True)
    fam_middle_name = models.CharField(max_length=64, blank=True, null=True)
    fam_last_name = models.CharField(max_length=64, null=True, blank=True)
    # fam_telnum = models.CharField(max_length=64, null=True, blank=True)
    # fam_cpnum = models.CharField(max_length=64, null=True, blank=True)
    fam_relation = models.ForeignKey('employee.Relationship', null=True)
    date_entered = models.DateTimeField(default=datetime.datetime.now())
    #date_enteredby = models.ForeignKey(User, default=1, related_name='address_enteredby')
    date_modify = models.DateTimeField(null=True)
    #modify_by = models.ForeignKey(User, default=1, related_name='address_modify')
    is_deleted = models.IntegerField(default=0)

    def save(self, force_insert=False, force_update=False):
        self.fam_first_name = self.fam_first_name.upper()
        self.fam_middle_name = self.fam_middle_name.upper()
        self.fam_last_name = self.fam_last_name.upper()
        super(EmployeeFamily, self).save(force_insert, force_update)

    class Meta:
        db_table = 'inq_employee_family'
        ordering = ['id']

    def __str__(self):
        return self.f_emp

    def __unicode__(self):
        return self.f_emp


class Relationship(models.Model):
    code = models.CharField(max_length=5, null=True)
    name = models.CharField(max_length=30, null=True)
    date_entered = models.DateTimeField(default=datetime.datetime.now())
    #date_enteredby = models.ForeignKey(User, default=1, related_name='address_enteredby')
    date_modify = models.DateTimeField(null=True)
    #modify_by = models.ForeignKey(User, default=1, related_name='address_modify')

    class Meta:
        db_table = 'inq_relation'
        ordering = ['id']

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Religion(models.Model):
    name = models.CharField(max_length=30, null=True)
    date_entered = models.DateTimeField(default=datetime.datetime.now())
    #date_enteredby = models.ForeignKey(User, default=1, related_name='address_enteredby')
    date_modify = models.DateTimeField(null=True)
    #modify_by = models.ForeignKey(User, default=1, related_name='address_modify')
    is_deleted = models.IntegerField(default=0)

    class Meta:
        db_table = 'inq_religion'
        ordering = ['id']

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Company(models.Model):
    code = models.CharField(max_length=8)
    name = models.CharField(max_length=64)
    date_entered = models.DateTimeField(null=True)

    class Meta:
        db_table = 'inq_company'
        ordering = ['id']

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Cities(models.Model):
    name = models.CharField(max_length=64, null=False)
    inter_level = models.CharField(max_length=64, null=True)
    region = models.IntegerField(null=True)
    province = models.IntegerField(null=True)
    zip = models.IntegerField(null=True)
    #date_enteredby = models.ForeignKey(User, default=1, related_name='address_enteredby')
    date_entered = models.DateTimeField(default=datetime.datetime.now())
    #modify_by = models.ForeignKey(User, default=1, related_name='address_modify')
    date_modify = models.DateField(null=True)
    is_deleted = models.IntegerField(default=0)

    class Meta:
        db_table = 'inq_cities'
        ordering = ['id']

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=64, null=False)
    inter_level = models.CharField(max_length=64, null=True)
    region = models.IntegerField(null=True)
    province = models.IntegerField(null=True)
    zip = models.IntegerField(null=True)
    #date_enteredby = models.ForeignKey(User, default=1, related_name='address_enteredby')
    date_entered = models.DateTimeField(default=datetime.datetime.now())
    #modify_by = models.ForeignKey(User, default=1, related_name='address_modify')
    date_modify = models.DateField(null=True)
    is_deleted = models.IntegerField(default=0)

    class Meta:
        db_table = 'inq_cities'
        ordering = ['id']

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name



class Province(models.Model):
    name = models.CharField(max_length=64, null=False)
    region = models.CharField(max_length=64, null=True)
    #date_enteredby = models.ForeignKey(User, default=1, related_name='address_enteredby')
    date_entered = models.DateTimeField(default=datetime.datetime.now())
    #modify_by = models.ForeignKey(User, default=1, related_name='address_modify')
    date_modify = models.DateTimeField(null=True)
    is_deleted = models.IntegerField(default=0)

    class Meta:
        db_table = 'inq_province'
        ordering = ['id']

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Provincial(models.Model):
    name = models.CharField(max_length=64, null=False)
    region = models.CharField(max_length=64, null=True)
    #date_enteredby = models.ForeignKey(User, default=1, related_name='address_enteredby')
    date_entered = models.DateTimeField(default=datetime.datetime.now())
    #modify_by = models.ForeignKey(User, default=1, related_name='address_modify')
    date_modify = models.DateTimeField(null=True)
    is_deleted = models.IntegerField(default=0)

    class Meta:
        db_table = 'inq_province'
        ordering = ['id']

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=64, null=True, blank=True)
    code = models.CharField(max_length=64, null=True, blank=True)
    #date_enteredby = models.ForeignKey(User, default=1, related_name='address_enteredby')
    date_entered = models.DateTimeField(default=datetime.datetime.now())
    #modify_by = models.ForeignKey(User, default=1, related_name='address_modify')
    date_modify = models.DateField(null=True)
    is_deleted = models.IntegerField(default=0)

    class Meta:
        db_table = 'inq_region'
        ordering = ['id']

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Branch(models.Model):
    code = models.CharField(max_length=8)
    name = models.CharField(max_length=64)
    company_id = models.IntegerField()
    date_entered = models.DateTimeField(null=True)

    class Meta:
        db_table = 'inq_branch'
        ordering = ['id']

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


# MasterFile Positions
class Positions(models.Model):
    code = models.CharField(max_length=8)
    name = models.CharField(max_length=64)
    date_added = models.DateTimeField(null=True)
    company_id = models.IntegerField()

    class Meta:
        db_table = 'inq_positions'
        ordering = ['id']

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


# Positions Database
class EmployeePosition(models.Model):
    emp = models.ForeignKey('employee.Employee', null=True)
    position = models.ForeignKey('employee.Positions', null=True, blank=True)
    yearfrom = models.DateField(null=True)
    yearto = models.DateField(null=True)
    company_id = models.IntegerField(default=1)
    date_entered = models.DateTimeField(null=True)
    is_deleted = models.IntegerField(default=0)

    class Meta:
        db_table = 'inq_emp_position'
        ordering = ['id']

    def __str__(self):
        return self.emp

    def __unicode__(self):
        return self.emp


class Levels(models.Model):
    code = models.CharField(max_length=8)
    description = models.CharField(max_length=64)
    date_entered = models.DateTimeField(null=True)
    has_late = models.IntegerField(default=1)
    has_undertime = models.IntegerField(default=1)
    has_overtime = models.IntegerField(default=1)
    has_night_differential = models.IntegerField(default=1)
    is_full_hours_worked = models.IntegerField(default=1)

    class Meta:
        db_table = 'inq_levels'
        ordering = ['id']

    def __str__(self):
        return self.description

    def __unicode__(self):
        return self.description


class Status(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=8)
    name = models.CharField(max_length=64)
    active = models.IntegerField()
    has_leave = models.IntegerField()

    class Meta:
        db_table = 'inq_status'
        ordering = ['id']

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Civil_status(models.Model):
    code = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    date_entered = models.DateTimeField(default=datetime.datetime.now())


    class Meta:
        db_table = 'inq_civil_status'
        ordering = ['id']

    def __str__(self):
        return self.Civil_stat

    def __unicode__(self):
        return self.Civil_stat


class Primary(models.Model):
    emp = models.ForeignKey('employee.Employee', null=True)
    name = models.ForeignKey('employee.MainSchool', null=True)
    year = models.DateField(null=True)
    company_id = models.IntegerField(default=1)
    date_entered = models.DateTimeField(null=True)
    is_deleted = models.IntegerField(default=0)

    class Meta:
        db_table = 'inq_primary'
        ordering = ['id']

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Secondary(models.Model):
    emp = models.ForeignKey('employee.Employee', null=True)
    name = models.ForeignKey('employee.MainSchool', null=True)
    year = models.DateField(null=True)
    company_id = models.IntegerField(default=1)
    date_entered = models.DateTimeField(null=True)
    is_deleted = models.IntegerField(default=0)

    class Meta:
        db_table = 'inq_secondary'
        ordering = ['id']

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class College(models.Model):
    emp = models.ForeignKey('employee.College', null=True)
    name = models.ForeignKey('employee.MainSchool', null=True, blank=True)
    yearfrom = models.DateField(null=True)
    yearto = models.DateField(null=True)
    company_id = models.IntegerField(default=1)
    date_entered = models.DateTimeField(null=True)
    is_deleted = models.IntegerField(default=0)

    class Meta:
        db_table = 'inq_college'
        ordering = ['id']

    def __str__(self):
        return self.emp

    def __unicode__(self):
        return self.emp


# Masterfile Schools(Elementary, Highschool, College/Universities)
class MainSchool(models.Model):
    code = models.CharField(max_length=16)
    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=100, null=True)
    region = models.CharField(max_length=100, null=True)
    company_id = models.IntegerField(default=1)
    date_entered = models.DateTimeField(null=True)
    is_deleted = models.IntegerField(default=0)

    class Meta:
        db_table = 'educ_school'
        ordering = ['id']

    def __str__(self):
        return self.id

    def __unicode__(self):
        return self.id


class Nationality(models.Model):
    name = models.CharField(max_length=64, null=True)
    country = models.CharField(max_length=64, null=True)
    language = models.CharField(max_length=64, null=True)
    date_entered = models.DateTimeField(default=datetime.datetime.now())
    #date_enteredby = models.ForeignKey(User, default=1, related_name='address_enteredby')
    date_modify = models.DateField(null=True)
    #modify_by = models.ForeignKey(User, default=1, related_name='address_modify')

    class Meta:
        db_table = 'inq_nationalities'
        ordering = ['id']

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name











