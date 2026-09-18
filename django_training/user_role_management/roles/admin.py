from django.contrib import admin
from .models import Role

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'roleName', 'createdAt', 'active')
    search_fields = ('roleName',)
    list_filter = ('active',)