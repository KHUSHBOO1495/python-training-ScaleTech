from django.test import TestCase
from .models import Employee
from .forms import EmployeeForm
from django.urls import reverse
from django.contrib.auth.models import User, Permission

class EmployeeTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )

        permission = Permission.objects.get(
            codename="view_employee"
        )

        self.user.user_permissions.add(permission)

        self.client.login(
            username="testuser",
            password="testpassword"
        )

    def test_employee_creation(self):
        employee = Employee.objects.create(
            name="Test Employee",
            age=25,
            designation="Developer"
        )

        self.assertEqual(employee.name, "Test Employee")
        self.assertEqual(employee.age, 25)
        self.assertEqual(employee.designation, "Developer")

    def test_employee_list_view(self):
        # response = self.client.get("/employees/")
        response = self.client.get(
            reverse("employee_list")
        )
        self.assertEqual(response.status_code, 200)

    def test_invalid_employee_age(self):
        form = EmployeeForm(data={
            "name": "Young Employee",
            "age": 15,
            "designation": "Developer",
        })

        self.assertFalse(form.is_valid())
        self.assertIn("age", form.errors)