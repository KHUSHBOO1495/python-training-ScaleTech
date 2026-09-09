from django.test import TestCase
from .models import Employee

class EmployeeTestCase(TestCase):

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
        response = self.client.get("/employees/")

        self.assertEqual(response.status_code, 200)