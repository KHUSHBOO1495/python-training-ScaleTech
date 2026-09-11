from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    # path("employees/", views.employee_list),
    path("employees/", views.EmployeeListView.as_view(), name="employee_list"),
    path("create/", views.employee_create, name="employee_create"),
    path("delete/<int:id>/", views.employee_delete, name="employee_delete"),
    path("update/<int:id>/", views.employee_update, name="employee_update"),
]
