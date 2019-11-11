from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse, Http404
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from .models import Employee, Company, Department, Positions, Branch, \
    Status, Secondary, Primary, College, Civil_status, Province, Cities, \
    Levels, Religion, Nationality, Address, ContactPerson, EmployeeFamily, \
    EmploymentRecord, MainSchool, EmployeePosition, Provincial, City
from django.db.models import Q
from django.utils.decorators import method_decorator
import datetime
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage


# from django.contrib.auth.decorators import login_required
class ListView(ListView):
    model = Employee
    template_name = 'employee/index.html'
    paginate_by = 30

    def get_queryset(self):
        employee = Employee.objects.all().filter(is_deleted=0).order_by('-pk')
        order = ''

        if self.request.method == 'GET':
            if 'keyword' in self.request.GET:
                employee = employee.filter(Q(first_name__icontains=self.request.GET['keyword']) |
                                           Q(middle_name__icontains=self.request.GET['keyword']) |
                                           Q(last_name__icontains=self.request.GET['keyword']) |
                                           Q(code__icontains=self.request.GET['keyword']))
            if 'order' in self.request.GET:
                if self.request.GET['order'] == 'desc':
                    order = '-'
            if 'sort' in self.request.GET:
                employee = employee.order_by(order + self.request.GET['sort'])

        return employee

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        # Count the Entries List
        context['count'] = self.get_queryset().count()

        if self.request.method == 'GET':
            if 'keyword' in self.request.GET:
                context['keyword'] = self.request.GET['keyword']
            if 'sort' in self.request.GET:
                context['sort'] = self.request.GET['sort']
            if 'order' in self.request.GET:
                context['order'] = self.request.GET['order']

        return context


# @method_decorator(login_required, name='dispatch')
class CreateEmployee(CreateView):
    model = Employee
    template_name = "employee/create.html"
    fields = ['code', 'first_name', 'middle_name', 'last_name', 'email', 'date_hired',
            'company', 'dob', 'pob', 'civil_status', 'gender', 'telnum', 'cphonenum',
            'sssno', 'tin', 'pagibig', 'philhealth', 'religion', 'nationality']
            # 'division', #'college', 'primary', 'secondary', 'cardno']

    #success_url = '/employee'

    def get_context_data(self, **kwargs):
        context = super(CreateEmployee, self).get_context_data(**kwargs)
        context['company'] = Company.objects.all().order_by('id')
        # context['department'] = Department.objects.all().order_by('id')
        # context['positions'] = Positions.objects.all().order_by('id')
        # context['branch'] = Branch.objects.all().order_by('id')
        # context['status'] = Status.objects.all().order_by('id')
        context['province'] = Province.objects.all().order_by('id')
        context['provincial'] = Provincial.objects.all().order_by('id')
        context['religion'] = Religion.objects.all().order_by('id')
        context['nationality'] = Nationality.objects.all().order_by('id')
        context['civil_status'] = Civil_status.objects.all().order_by('id')
        context['cities'] = Cities.objects.all().order_by('id')
        context['city'] = City.objects.all().order_by('id')
        return context

    # def dispatch(self, request, *args, **kwargs):
    #     # if not request.user.has_perm('employee.add_employee'):
    #     #     raise Http404
    #     return super(CreateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        address = Address()
        address.a_house_num = self.request.POST['a_house_num']
        address.a_street_subd = self.request.POST['a_street_subd']
        address.a_barangay = self.request.POST['a_barangay']
        address.a_province_id = self.request.POST['a_province']
        address.a_city_id = self.request.POST['a_city']
        # address.a_zipcode = self.request.POST['a_zipcode']
        address.p_house_num = self.request.POST['p_house_num']
        address.p_street_subd = self.request.POST['p_street_subd']
        address.p_barangay = self.request.POST['p_barangay']
        address.p_province_id = self.request.POST['p_province']
        address.p_city_id = self.request.POST['p_city']
        #address.p_zipcode = self.request.POST['p_zipcode']
        address.company_id = self.request.POST['company']
        address.save()

        self.object = form.save(commit=False)
        self.object.address = address
        self.object.save()

        contactperson = ContactPerson()
        contactperson.cfirst_name = self.request.POST['cfirst_name']
        contactperson.cmiddle_name = self.request.POST['cmiddle_name']
        contactperson.clast_name = self.request.POST['clast_name']
        contactperson.ctelnum = self.request.POST['ctelnum']
        contactperson.ccpnum = self.request.POST['ccphonenum']
        contactperson.company_id = self.request.POST['company']
        contactperson.save()

        self.object = form.save(commit=False)
        self.object.contactperson = contactperson
        self.object.save()

        #employeefamily = EmployeeFamily()
        #employeefamily.f_emp = self.request.POST['f_emp']
        #employeefamily.fam_first_name = self.request.POST['fam_first_name']
        #employeefamily.fam_middle_name = self.request.POST['fam_middle_name']
        #employeefamily.fam_last_name = self.request.POST['fam_last_name']
        #employeefamily.fam_gender = self.request.POST['fam_gender']
        #employeefamily.fam_relation_id = self.request.POST['fam_relation']
        #employeefamily.date_modify = datetime.datetime.now()
        #employeefamily.date_entered = self.request.POST['date_entered']
        #employeefamily.company_id = self.request.POST['company']
        #employeefamily.save()

        #self.object = form.save(commit=False)
        #self.object.employeefamily = employeefamily
        #self.object.save()

        #employmentrecord = EmploymentRecord()
        #employmentrecord.cname = self.request.POST['cname']
        #employmentrecord.yearfrom = self.request.POST['yearfrom']
        #employmentrecord.yearto = self.request.POST['yearto']
        #employmentrecord.company_id = self.request.POST['company']
        #employmentrecord.save()

        #self.object = form.save(commit=False)
        #self.object.employmentrecord = employmentrecord
        #self.object.save()

        return HttpResponseRedirect('/employee/' + str(self.object.id))


class UpdateView(UpdateView):
    model = Employee
    template_name = 'employee/update.html'
    fields = ['date_hired', 'code', 'department', 'status', 'branch_assigned', 'position_level',
            'first_name', 'middle_name', 'last_name', 'email', 'dob', 'pob', 'telnum', 'cphonenum',
            'sssno', 'tin', 'pagibig', 'philhealth', 'civil_status', 'gender', 'religion', 'nationality']
            #'position_class', 'immediate_head', 'dept_section', 'division']

    success_url = '/employee'

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['company'] = Company.objects.all().order_by('id')
        context['department'] = Department.objects.all().order_by('id')
        context['positions'] = Positions.objects.all().order_by('id')
        context['empposition'] = EmployeePosition.objects.all().order_by('id')
        context['branch'] = Branch.objects.all().order_by('id')
        context['status'] = Status.objects.all().order_by('id')
        context['position_level'] = Levels.objects.all().order_by('id')
        context['civil_status'] = Civil_status.objects.all().order_by('id')
        context['province'] = Province.objects.all().order_by('id')
        context['provincial'] = Provincial.objects.all().order_by('id')
        context['religion'] = Religion.objects.all().order_by('id')
        context['nationality'] = Nationality.objects.all().order_by('id')
        context['cities'] = Cities.objects.all().order_by('id')
        context['city'] = City.objects.all().order_by('id')
        context['primary'] = Primary.objects.all().order_by('id')
        context['secondary'] = Secondary.objects.all().order_by('id')
        context['mschool'] = MainSchool.objects.all().order_by('id')
        context['college'] = College.objects.all().order_by('id')
        context['employee_family_father'] = EmployeeFamily.objects.filter(fam_relation=1)
        context['employee_family_Mother'] = EmployeeFamily.objects.filter(fam_relation=2)
        context['employee_family_Brother'] = EmployeeFamily.objects.filter(fam_relation=3)
        context['employee_family_Sister'] = EmployeeFamily.objects.filter(fam_relation=4)
        return context

    def form_valid(self, form):
        address = Address()
        address.a_house_num = self.request.POST['a_house_num']
        address.a_street_subd = self.request.POST['a_street_subd']
        address.a_barangay = self.request.POST['a_barangay']
        address.a_province_id = self.request.POST['a_province']
        address.a_city_id = self.request.POST['a_city']
        # address.a_zipcode = self.request.POST['a_zipcode']
        address.p_house_num = self.request.POST['p_house_num']
        address.p_street_subd = self.request.POST['p_street_subd']
        address.p_barangay = self.request.POST['p_barangay']
        address.p_province_id = self.request.POST['p_province']
        address.p_city_id = self.request.POST['p_city']
        #address.p_zipcode = self.request.POST['p_zipcode']
        address.date_entered = self.request.POST['date_entered']
        address.date_modify = datetime.datetime.now()
        address.company_id = self.request.POST['company']
        address.save()

        self.object = form.save(commit=False)
        self.object.address = address
        self.object.save()

        # employmentrecord = EmploymentRecord()
        # employmentrecord.cname = self.request.POST['cname']
        # employmentrecord.yearfrom = self.request.POST['yearfrom']
        # employmentrecord.yearto = self.request.POST['yearto']
        # employmentrecord.company_id = self.request.POST['company']
        # employmentrecord.save()
        #
        # self.object = form.save(commit=False)
        # self.object.employmentrecord = employmentrecord
        # self.object.save()

        contactperson = ContactPerson()
        contactperson.cfirst_name = self.request.POST['cfirst_name']
        contactperson.cmiddle_name = self.request.POST['cmiddle_name']
        contactperson.clast_name = self.request.POST['clast_name']
        contactperson.ctelnum = self.request.POST['ctelnum']
        contactperson.ccpnum = self.request.POST['ccphonenum']
        #contactperson.company_id = self.request.POST['company']
        contactperson.date_modify = datetime.datetime.now()
        contactperson.date_entered = self.request.POST['date_entered']
        contactperson.company_id = self.request.POST['company']
        contactperson.save()

        self.object = form.save(commit=False)
        self.object.contactperson = contactperson
        self.object.save()

        # employeeposition = EmployeePosition()
        # employeeposition.emp_id = ''  #self.request.POST['']
        # employeeposition.position_id = self.request.POST['employee_position']
        # employeeposition.company_id = self.request.POST['company']
        # #employeeposition.yearfrom = '' #self.request.POST['company']
        # #employeeposition.yearto = '' #self.request.POST['company']
        # #employeeposition.date_entered = '' #self.request.POST['date_entered']
        # employeeposition.save()

        # self.object = form.save(commit=False)
        # self.object.employeeposition = employeeposition
        # self.object.save()

        #employeefamily = EmployeeFamily()
        #employeefamily.f_emp = self.request.POST['f_emp']
        #employeefamily.fam_first_name = self.request.POST['fam_first_name']
        #employeefamily.fam_middle_name = self.request.POST['fam_middle_name']
        #employeefamily.fam_last_name = self.request.POST['fam_last_name']
        #employeefamily.fam_relation_id = self.request.POST['fam_relation']
        #employeefamily.date_modify = datetime.datetime.now()
        #employeefamily.date_entered = self.request.POST['date_entered']
        #employeefamily.company_id = self.request.POST['company']
        #employeefamily.save()

        #self.object = form.save(commit=False)
        #self.object.employeefamily = employeefamily
        #self.object.save()

        #storeupload(request.FILES['medical_his'], sequence, 'txt', upload_directory)

    #      def storeupload(file, file_name, file_extension, upload_directory):
    #      from django.core.files.storage import FileSystemStorage
    #      fs = FileSystemStorage()
    #      filename = fs.save(upload_directory+file_name+'.'+file_extension, file)
    #      fs.url(filename)
    #      return True

        return HttpResponseRedirect('/employee/' + str(self.object.id))


class DeleteView(DeleteView):
    model = Employee
    template_name = 'employee/delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        # self.object.modifyby = self.request.user
        # self.object.modifydate = datetime.datetime.now()
        self.object.is_deleted = 1
        #self.object.status = 'I'
        self.object.save()
        return HttpResponseRedirect('/employee')











