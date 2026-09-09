from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    # path("employees/", views.employee_list),
    path("employees/", views.EmployeeListView.as_view()),
]
