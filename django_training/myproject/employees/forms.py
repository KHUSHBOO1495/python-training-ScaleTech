from django import forms
from .models import Employee, Department

class EmployeeForm(forms.ModelForm):
    def clean_age(self):
        age = self.cleaned_data["age"]

        if age < 18 or age > 60:
            raise forms.ValidationError(
                "Employee age must be between 18 and 60."
            )

        return age
    
    def clean(self):
        cleaned_data = super().clean()

        age = cleaned_data.get("age")
        designation = cleaned_data.get("designation")

        if age is not None and designation:
            if designation.lower() == "manager" and age < 25:
                raise forms.ValidationError(
                    "A Manager must be at least 25 years old."
                )

        return cleaned_data

    class Meta:
        model = Employee
        fields = ['name', 'age', 'designation', 'department', 'projects', 'profile_image']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ["name"]