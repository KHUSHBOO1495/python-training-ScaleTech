import json

from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth import authenticate, login

from .models import User
from roles.models import Role


def user_list(request):

    if request.method == "GET":
        users = User.objects.all()
        search = request.GET.get("search")

        if search:
            users = users.filter(
                Q(first_name__icontains=search)
                | Q(last_name__icontains=search)
                | Q(email__icontains=search)
            )

        user_data = []

        for user in users:
            user_data.append(
                {
                    "id": user.id,
                    "firstName": user.first_name,
                    "lastName": user.last_name,
                    "email": user.email,
                    "role": {
                        "roleName": user.role.roleName,
                        "accessModules": user.role.accessModules,
                    },
                    "is_active": user.is_active,
                }
            )

        return JsonResponse(user_data, safe=False)

    elif request.method == "POST":
        data = json.loads(request.body)

        required_fields = ["firstName", "lastName", "email", "password", "role"]

        for field in required_fields:
            if field not in data:
                return JsonResponse(
                    {"error": f"{field} is required"},
                    status=400
                )

        try:
            role = Role.objects.get(id=data["role"])
        except Role.DoesNotExist:
            return JsonResponse(
                {"error": "Role not found"},
                status=404
            )

        user = User(
            username=data["email"],
            first_name=data["firstName"],
            last_name=data["lastName"],
            email=data["email"],
            role=role,
        )

        user.set_password(data["password"])
        user.save()

        return JsonResponse(
            {
                "id": user.id,
                "firstName": user.first_name,
                "lastName": user.last_name,
                "email": user.email,
                "role": user.role_id,
                "is_active": user.is_active,
            },
            status=201
        )
    
def user_detail(request, user_id):

    if request.method == "GET":
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return JsonResponse(
                {"error": "User not found"},
                status=404
            )

        return JsonResponse(
            {
                "id": user.id,
                "firstName": user.first_name,
                "lastName": user.last_name,
                "email": user.email,
                "role": user.role_id,
                "is_active": user.is_active,
            }
        )
    
    elif request.method == "PUT":
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return JsonResponse(
                {"error": "User not found"},
                status=404
            )

        data = json.loads(request.body)

        required_fields = [
            "firstName",
            "lastName",
            "email",
            "role",
        ]

        for field in required_fields:
            if field not in data:
                return JsonResponse(
                    {"error": f"{field} is required"},
                    status=400
                )

        try:
            role = Role.objects.get(id=data["role"])
        except Role.DoesNotExist:
            return JsonResponse(
                {"error": "Role not found"},
                status=404
            )

        user.username = data["email"]
        user.first_name = data["firstName"]
        user.last_name = data["lastName"]
        user.email = data["email"]
        user.role = role

        user.save()

        return JsonResponse(
            {
                "id": user.id,
                "firstName": user.first_name,
                "lastName": user.last_name,
                "email": user.email,
                "role": user.role_id,
                "is_active": user.is_active,
            }
        )
    
    elif request.method == "DELETE":
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return JsonResponse(
                {"error": "User not found"},
                status=404
            )

        user.delete()

        return JsonResponse(
            {"message": "User deleted successfully"}
        )
    

def check_module_access(request, user_id, module):
    if request.method == "GET":
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return JsonResponse(
                {"error": "User not found"},
                status=404
            )

        has_access = module in user.role.accessModules

        return JsonResponse(
            {
                "userId": user.id,
                "module": module,
                "hasAccess": has_access,
            }
        )
    

def bulk_update_users(request):
    if request.method == "PUT":
        data = json.loads(request.body)

        if "userIds" not in data:
            return JsonResponse(
                {"error": "userIds is required"},
                status=400
            )

        if "data" not in data:
            return JsonResponse(
                {"error": "data is required"},
                status=400
            )
        
        if not isinstance(data["userIds"], list):
            return JsonResponse(
                {"error": "userIds must be a list"},
                status=400
            )
        
        if not isinstance(data["data"], dict):
            return JsonResponse(
                {"error": "data must be an object"},
                status=400
            )

        allowed_fields = {
            "firstName": "first_name",
            "lastName": "last_name",
            "email": "email",
            "role": "role", 
            "is_active": "is_active",
        }

        update_data = {}

        for field, value in data["data"].items():
            if field not in allowed_fields:
                return JsonResponse(
                    {"error": f"Field '{field}' cannot be updated"},
                    status=400
                )

            update_data[allowed_fields[field]] = value

        user_ids = data["userIds"]

        updated_count = User.objects.filter(
            id__in=user_ids
        ).update(**update_data)

        return JsonResponse(
            {
                "message": "Users updated successfully",
                "updatedCount": updated_count,
            },
            status=200
        )
    
def bulk_update_users_different(request):
    if request.method == "PUT":
        data = json.loads(request.body)

        if "users" not in data:
            return JsonResponse(
                {"error": "users is required"},
                status=400
            )

        if not isinstance(data["users"], list):
            return JsonResponse(
                {"error": "users must be a list"},
                status=400
            )
            
        allowed_fields = {
            "firstName": "first_name",
            "lastName": "last_name",
            "email": "email",
            "role": "role",
            "is_active": "is_active",
        }
        users_to_update = []
        fields_to_update = set()
        for user_data in data["users"]:
            if "id" not in user_data or "data" not in user_data:
                return JsonResponse(
                    {"error": "Each user must contain id and data"},
                    status=400
                )
            
            if not isinstance(user_data["data"], dict):
                return JsonResponse(
                    {"error": "data must be an object"},
                    status=400
                )

            update_data = {}

            for field, value in user_data["data"].items():
                if field not in allowed_fields:
                    return JsonResponse(
                        {"error": f"Field '{field}' cannot be updated"},
                        status=400
                    )

                update_data[allowed_fields[field]] = value

            try:
                user = User.objects.get(id=user_data["id"])
            except User.DoesNotExist:
                return JsonResponse(
                    {"error": f"User with id {user_data['id']} not found"},
                    status=404
                )
            
            for field, value in update_data.items():
                setattr(user, field, value)
                fields_to_update.add(field)

            users_to_update.append(user)

        User.objects.bulk_update(
            users_to_update,
            list(fields_to_update)
        )

        return JsonResponse(
            {
                "message": "Users updated successfully",
                "updatedCount": len(users_to_update),
            },
            status=200
        )


def signup(request):
    """
    Register a new user account.
    """

    if request.method == "POST":
        data = json.loads(request.body)

        required_fields = [
            "firstName",
            "lastName",
            "email",
            "password",
            "role",
        ]

        for field in required_fields:
            if field not in data:
                return JsonResponse(
                    {"error": f"{field} is required"},
                    status=400
                )

        try:
            role = Role.objects.get(id=data["role"])
        except Role.DoesNotExist:
            return JsonResponse(
                {"error": "Role not found"},
                status=404
            )

        if User.objects.filter(email=data["email"]).exists():
            return JsonResponse(
                {"error": "A user with this email already exists"},
                status=400
            )

        user = User(
            username=data["email"],
            first_name=data["firstName"],
            last_name=data["lastName"],
            email=data["email"],
            role=role,
        )

        user.set_password(data["password"])
        user.save()

        return JsonResponse(
            {
                "message": "User registered successfully",
                "id": user.id,
                "firstName": user.first_name,
                "lastName": user.last_name,
                "email": user.email,
                "role": user.role_id,
            },
            status=201
        )
    
def login_user(request):
    """
    Authenticate a user using email and password.
    """

    if request.method == "POST":
        data = json.loads(request.body)

        required_fields = [
            "email",
            "password",
        ]

        for field in required_fields:
            if field not in data:
                return JsonResponse(
                    {"error": f"{field} is required"},
                    status=400
                )
            
        user = authenticate(
            username=data["email"],
            password=data["password"],
        )

        if user is None:
            return JsonResponse(
                {"error": "Invalid email or password"},
                status=401
            )
        
        login(request, user)
        
        return JsonResponse(
            {
                "message": "Login successful",
                "id": user.id,
                "firstName": user.first_name,
                "lastName": user.last_name,
                "email": user.email,
                "role": user.role_id,
            },
            status=200
        )