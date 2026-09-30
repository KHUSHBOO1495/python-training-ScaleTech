from django.urls import path
from . import views

urlpatterns = [
    path("", views.role_list, name="role_list"),
    path("roles/<int:role_id>/", views.role_detail, name="role_detail"),
    path("roles/<int:role_id>/access-modules/", views.update_access_modules, name="update_access_modules",),
    path("roles/<int:role_id>/access-modules/remove/", views.remove_access_module, name="remove_access_module",),    
    path("csrf-token/", views.csrf_token_view, name="csrf_token"),
]