from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Value, Count, F
from django.db.models.functions import Concat
from datetime import datetime

from .models import *
from company.models import *
import json
from employee.forms import *

from django.db import transaction

class EmployeeView(View):
    
    def get(self, request):
        employees = Employee.objects.all()
        for employee in employees:
            employee.position = Position.objects.get(pk=employee.position_id)
            # print(employee.position)
        show = {'employees': employees}
        return render(request, "employee.html", show)
    
class PositionView(View):
    
    def get(self, request):
        position_list = Position.objects.annotate(employee_count=Count('employee')).order_by('id')
        show = {'positions': position_list}
        return render(request, "position.html", show)
    
class ProjectView(View):
    def get(self, request):
        project_list = Project.objects.all()
        show = {'projects': project_list}
        return render(request, "project.html", show)
    
    def delete(self, request, project_id):
        project = Project.objects.get(id=project_id)
        project.delete()
        return JsonResponse({'messgage': 'Already delete project'})

class ProjectDetailView(View):
    def get(self, request, project_id):
        getproject = Project.objects.get(id=project_id)
        show = {'project': getproject}
        return render(request, "project_detail.html", show)
    
    def put(self, request, project_id, staff_id):
        getproject = Project.objects.get(id=project_id)
        getstaff = Employee.objects.get(id=staff_id)
        getproject.staff.add(getstaff)
        return JsonResponse({'message': 'Add staff success'})
    
    def delete(self, request, project_id, staff_id):
        getproject = Project.objects.get(id=project_id)
        getstaff = Employee.objects.get(id=staff_id)
        getproject.staff.remove(getstaff)
        return JsonResponse({'message': 'Kick staff success'})
    
class Employee_FormView(View):

    @transaction.atomic
    def post(self, request):
        form = EmployeeForm(request.POST)
        print(form.errors)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            gender = form.cleaned_data["gender"]
            birth_date = form.cleaned_data["birth_date"]
            hire_date = form.cleaned_data["hire_date"]
            salary = form.cleaned_data["salary"]

            position = form.cleaned_data["position"].id
            print(position)

            salary = form.cleaned_data["salary"]
            new_employee = Employee.objects.create(first_name=first_name, last_name=last_name, gender=gender, birth_date=birth_date, hire_date=hire_date, salary=salary, position_id=position)

            location = form.cleaned_data["location"]
            district = form.cleaned_data["district"]
            province = form.cleaned_data["province"]
            postal_code = form.cleaned_data["postal_code"]
            EmployeeAddress.objects.create(employee=new_employee, location=location, district=district, province=province, postal_code=postal_code)

            return redirect("employee")
        else:
            print(form.errors)
            return render(request, "employee_form.html", {"form": form})

    def get(self, request):
        form = EmployeeForm()
        return render(request, "employee_form.html", {"form": form})

class Project_FormView(View):
    def post(self, request):
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project')
        else:
            return render(request, "project_form.html", {"form": form})

        
    def get(self, request):
        form = ProjectForm()
        return render(request, "project_form.html", {"form": form})
    
class Edit_Project_FormView(View):
    def get(self, request, project_id):
        getproject = Project.objects.get(id=project_id)
        form = EditProjectForm(instance=getproject)
        return render(request, "project_detail.html", {"form": form, 'project': getproject})
    
    def post(self, request, project_id):
        getproject_edit = Project.objects.get(id=project_id)
        form = EditProjectForm(request.POST, instance=getproject_edit)
        if form.is_valid():
            form.save()
            return redirect('project_form_edit', project_id)
        else:
            print(form.errors)
            return render(request, "project_detail.html", {"form": form})


    