from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Project(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    designation = models.CharField(max_length=100)

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="employees",
        null=True
    )

    projects = models.ManyToManyField(
        Project,
        related_name="employees"
    )

    def __str__(self):
        return self.name

    def get_info(self):
        return f"{self.name} - {self.designation}"

    def get_project_count(self):
        return self.projects.count()
    
class EmployeeProfile(models.Model):
    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.employee.name}'s Profile"