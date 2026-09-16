from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("employees/", views.employee_list, name="employee_list"),
    path("create/", views.employee_create, name="employee_create"),
    path("delete/<int:id>/", views.employee_delete, name="employee_delete"),
    path("update/<int:id>/", views.employee_update, name="employee_update"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),

    # path("employees/", views.EmployeeListView.as_view(), name="employee_list"),
    path("departments/", views.DepartmentListView.as_view(), name="department_list"),
    path("departments/<int:pk>/", views.DepartmentDetailView.as_view(), name="department_detail"),
    path("departments/create/", views.DepartmentCreateView.as_view(), name="department_create"),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
