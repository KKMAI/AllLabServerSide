from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from django.db.models import Value, Count, F
from django.db.models.functions import Concat

from datetime import datetime

from .models import *

import json

class IndexView(View):
    def get(self, request):
        # employee_list = Employee.objects.annotate(fullname=Concat('first_name', Value(" "), 'last_name'))

        employee_list = Employee.objects.all()
        # print(Employee.get_full_name)
        

        return render(request, "employee.html", {
            "employee_list" : employee_list,
            "total" : Employee.objects.all().count(),
            # "fullname" : Employee.objects.annotate(fullname=Concat('first_name', Value(" "), 'last_name'))
        })

class PositionView(View):
    def get(self, request):
        position_list = Position.objects.annotate(employee_count=Count('employee')).order_by('id')
        return render(request, "position.html", {
            "position_list" : position_list,
        })


class ProjectView(View):
    def get(self, request):
        project_list = Project.objects.all()
        return render(request, "project.html", {
            "project_list" : project_list
        })
    
    def delete(self, request, project_id):
        projecto = Project.objects.get(pk=project_id)
        projecto.delete()
        return JsonResponse({'message': 'already delete project'})

class ProjectDetailView(View):
    def get(self, request, project_id):
        get_project = Project.objects.annotate(manager_fullname=Concat('manager__first_name', Value(" "), 'manager__last_name')).get(pk=project_id)

        get_start_date = get_project.start_date.strftime("%Y-%m-%d")
        get_due_date = get_project.due_date.strftime("%Y-%m-%d")

        get_staff = get_project.staff.all()


        return render(request, "project_detail.html", {
            "project" : get_project,
            "start_date" : get_start_date,
            "due_date" : get_due_date,
            "staffs" : get_staff
        })
    
    def put(self, request, project_id):
        project = Project.objects.get(pk=project_id)
        data = json.loads(request.body)
        staff_id = data.get("emp_id")

        staff = Employee.objects.get(pk=staff_id)
        project.staff.add(staff)
        return JsonResponse({'message': 'already add staff'})  

    def delete(self, request, project_id, employee_id):
        project = Project.objects.get(pk=project_id)
        staff = Employee.objects.get(pk=employee_id)
        project.staff.remove(staff)
        return JsonResponse({'message': 'already kick staff'})
    
class LayoutView(View):
    def get(self, request):
        return render(request, 'layout.html')







class IndexView2(View):
    def get(self, request):
        # employee_list = Employee.objects.annotate(fullname=Concat('first_name', Value(" "), 'last_name'))

        employee_list = Employee.objects.all()
        # print(Employee.get_full_name)
        

        return render(request, "2employee.html", {
            "employee_list" : employee_list,
            "total" : Employee.objects.all().count(),
            # "fullname" : Employee.objects.annotate(fullname=Concat('first_name', Value(" "), 'last_name'))
        })
    
class PositionView2(View):
    def get(self, request):
        position_list = Position.objects.annotate(employee_count=Count('employee')).order_by('id')
        return render(request, "2position.html", {
            "position_list" : position_list,
        })


class ProjectView2(View):
    def get(self, request):
        project_list = Project.objects.all()
        return render(request, "2project.html", {
            "project_list" : project_list
        })
    
    def delete(self, request, project_id):
        projecto = Project.objects.get(pk=project_id)
        projecto.delete()
        return JsonResponse({'message': 'already delete project'})

class ProjectDetailView2(View):
    def get(self, request, project_id):
        get_project = Project.objects.annotate(manager_fullname=Concat('manager__first_name', Value(" "), 'manager__last_name')).get(pk=project_id)

        get_start_date = get_project.start_date.strftime("%Y-%m-%d")
        get_due_date = get_project.due_date.strftime("%Y-%m-%d")

        get_staff = get_project.staff.all()


        return render(request, "2project_detail.html", {
            "project" : get_project,
            "start_date" : get_start_date,
            "due_date" : get_due_date,
            "staffs" : get_staff
        })
    
    def put(self, request, project_id):
        project = Project.objects.get(pk=project_id)
        data = json.loads(request.body)
        staff_id = data.get("emp_id")

        staff = Employee.objects.get(pk=staff_id)
        project.staff.add(staff)
        return JsonResponse({'message': 'already add staff'})  

    def delete(self, request, project_id, employee_id):
        project = Project.objects.get(pk=project_id)
        staff = Employee.objects.get(pk=employee_id)
        project.staff.remove(staff)
        return JsonResponse({'message': 'already kick staff'})
