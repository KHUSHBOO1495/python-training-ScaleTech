from django.urls import path
from . import views

urlpatterns = [
    path("", views.user_list, name="user_list"),
    path("bulk-update/", views.bulk_update_users, name="bulk_update_users"),
    path("bulk-update-different/", views.bulk_update_users_different, name="bulk_update_users_different"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login_user, name="login_user"),
    path("<int:user_id>/", views.user_detail, name="user_detail"),
    path("<int:user_id>/access/<str:module>/", views.check_module_access, name="check_module_access",),
]