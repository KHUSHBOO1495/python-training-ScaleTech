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