from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("employees/", views.employee_list, name="employee_list"),
    # path("employees/", views.EmployeeListView.as_view(), name="employee_list"),
    path("create/", views.employee_create, name="employee_create"),
    path("delete/<int:id>/", views.employee_delete, name="employee_delete"),
    path("update/<int:id>/", views.employee_update, name="employee_update"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
]
