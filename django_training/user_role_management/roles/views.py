from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import json

from .models import Role

@ensure_csrf_cookie
def csrf_token_view(request):
    """
    Set a CSRF cookie for the client.
    """
    return JsonResponse({"message": "CSRF cookie set"})


def role_list(request):
    
    if request.method == "GET":
        roles = Role.objects.all()

        role_data = list(
            roles.values(
                "id",
                "roleName",
                "accessModules",
                "createdAt",
                "active",
            )
        )

        return JsonResponse(role_data, safe=False)
    
    elif request.method == "POST":
        data = json.loads(request.body)
        if "roleName" not in data:
            return JsonResponse(
                {"error": "roleName is required"},
                status=400
            )
        if not data["roleName"].strip():
            return JsonResponse(
                {"error": "roleName cannot be empty"},
                status=400
            )
        if not isinstance(data["accessModules"], list):
            return JsonResponse(
                {"error": "accessModules must be a list"},
                status=400
            )
        
        role = Role.objects.create(
            roleName=data["roleName"],
            accessModules=data["accessModules"],
            active=data.get("active", True),
        )
        return JsonResponse(
            {
                "id": role.id,
                "roleName": role.roleName,
                "accessModules": role.accessModules,
                "createdAt": role.createdAt,
                "active": role.active,
            },
            status=201
        )
    

def role_detail(request, role_id):

    if request.method == "GET":
        try:
            role = Role.objects.get(id=role_id)
        except Role.DoesNotExist:
            return JsonResponse(
                {"error": "Role not found"},
                status=404
            )

        return JsonResponse(
            {
                "id": role.id,
                "roleName": role.roleName,
                "accessModules": role.accessModules,
                "createdAt": role.createdAt,
                "active": role.active,
            }
        )

    elif request.method == "PUT":
        try:
            role = Role.objects.get(id=role_id)
            print(role)
        except Role.DoesNotExist:
            return JsonResponse(
                {"error": "Role not found"},
                status=404
            )

        data = json.loads(request.body)

        if "roleName" not in data:
            return JsonResponse(
                {"error": "roleName is required"},
                status=400
            )

        if not data["roleName"].strip():
            return JsonResponse(
                {"error": "roleName cannot be empty"},
                status=400
            )

        if "accessModules" not in data:
            return JsonResponse(
                {"error": "accessModules is required"},
                status=400
            )

        if not isinstance(data["accessModules"], list):
            return JsonResponse(
                {"error": "accessModules must be a list"},
                status=400
            )

        role.roleName = data["roleName"]
        role.accessModules = data["accessModules"]
        role.active = data.get("active", role.active)

        role.save()

        return JsonResponse(
            {
                "id": role.id,
                "roleName": role.roleName,
                "accessModules": role.accessModules,
                "createdAt": role.createdAt,
                "active": role.active,
            }
        )

    elif request.method == "DELETE":
        try:
            role = Role.objects.get(id=role_id)
        except Role.DoesNotExist:
            return JsonResponse(
                {"error": "Role not found"},
                status=404
            )

        role.delete()

        return JsonResponse(
            {"message": "Role deleted successfully"}
        )
    

def update_access_modules(request, role_id):
    if request.method == "PUT":
        try:
            role = Role.objects.get(id=role_id)
        except Role.DoesNotExist:
            return JsonResponse(
                {"error": "Role not found"},
                status=404
            )

        data = json.loads(request.body)

        if "accessModules" not in data:
            return JsonResponse(
                {"error": "accessModules is required"},
                status=400
            )

        if not isinstance(data["accessModules"], list):
            return JsonResponse(
                {"error": "accessModules must be a list"},
                status=400
            )
        
        unique_modules = list(dict.fromkeys(data["accessModules"]))
        role.accessModules = unique_modules
        role.save()

        return JsonResponse(
            {
                "id": role.id,
                "roleName": role.roleName,
                "accessModules": role.accessModules,
            }
        )
    

def remove_access_module(request, role_id):
    if request.method == "DELETE":
        try:
            role = Role.objects.get(id=role_id)
        except Role.DoesNotExist:
            return JsonResponse(
                {"error": "Role not found"},
                status=404
            )

        data = json.loads(request.body)

        if "module" not in data:
            return JsonResponse(
                {"error": "module is required"},
                status=400
            )
        
        module = data["module"]

        if module not in role.accessModules:
            return JsonResponse(
                {"error": "Module not found in accessModules"},
                status=404
            )
        
        role.accessModules.remove(module)
        role.save()

        return JsonResponse(
            {
                "id": role.id,
                "roleName": role.roleName,
                "accessModules": role.accessModules,
            }
        )