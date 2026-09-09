from django.shortcuts import render
from .models import Employee
from django.views import View
from django.views.generic import ListView
from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to the Employee Management System")


# def employee_list(request):
#     employees = Employee.objects.all()
#     if request.method == 'GET':
#         return render(
#             request,
#             "employees/employee_list.html",
#             {"employees": employees}
#         )
#     return HttpResponse("Unsupported request method")

# class EmployeeListView(View):

#     def get(self, request):
#         employees = Employee.objects.all()

#         return render(
#             request,
#             "employees/employee_list.html",
#             {"employees": employees}
#         )

class EmployeeListView(ListView):
    model = Employee
    template_name = "employees/employee_list.html"
    context_object_name = "employees"