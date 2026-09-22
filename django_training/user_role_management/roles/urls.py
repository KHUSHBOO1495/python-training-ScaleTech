from django.urls import path
from . import views

urlpatterns = [
    path("", views.role_list, name="role_list"),
    path("roles/<int:role_id>/", views.role_detail, name="role_detail"),
    path("csrf-token/", views.csrf_token_view, name="csrf_token"),
]