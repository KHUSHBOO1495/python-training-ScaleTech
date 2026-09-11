from django.shortcuts import render, redirect
from .models import Employee
from django.views import View
from django.views.generic import ListView
from django.http import HttpResponse
from .forms import EmployeeForm

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

def employee_create(request):

    if request.method == "POST":
        form = EmployeeForm(request.POST) # bound form

        if form.is_valid():
            form.save()
            return redirect("employee_list")

    else:
        form = EmployeeForm() # unbound form

    return render(
        request,
        "employees/employee_form.html",
        {"form": form}
    )

def employee_delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()

    return redirect("employee_list")

def employee_update(request, id):
    employee = Employee.objects.get(id=id)

    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            form.save()
            return redirect("employee_list")

    else:
        form = EmployeeForm(instance=employee)

    return render(
        request,
        "employees/employee_form.html",
        {"form": form}
    )