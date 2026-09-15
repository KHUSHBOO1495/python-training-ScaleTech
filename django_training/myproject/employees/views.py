from django.shortcuts import render, redirect
from .models import Employee
from django.views import View
from django.views.generic import ListView
from django.http import HttpResponse
from .forms import EmployeeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required

def home(request):
    return render(
        request,
        "employees/home.html"
    )

@login_required
@permission_required(
    "employees.view_employee",
    raise_exception=True
)
def employee_list(request):
    employees = Employee.objects.all()
    if request.method == 'GET':
        return render(
            request,
            "employees/employee_list.html",
            {"employees": employees}
        )
    return HttpResponse("Unsupported request method")

# class EmployeeListView(View):

#     def get(self, request):
#         employees = Employee.objects.all()

#         return render(
#             request,
#             "employees/employee_list.html",
#             {"employees": employees}
#         )

# class EmployeeListView(ListView):
#     model = Employee
#     template_name = "employees/employee_list.html"
#     context_object_name = "employees"

@login_required
@permission_required(
    "employees.add_employee",
    raise_exception=True
)
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

@login_required
@permission_required(
    "employees.delete_employee",
    raise_exception=True
)
def employee_delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()

    return redirect("employee_list")

@login_required
@permission_required(
    "employees.change_employee",
    raise_exception=True
)
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

def user_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("employee_list")

        else:
            return render(
                request,
                "employees/login.html",
                {"error": "Invalid username or password."}
            )

    return render(request, "employees/login.html")

def user_logout(request):
    logout(request)
    return redirect("login")