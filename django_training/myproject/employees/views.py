from django.shortcuts import render

from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to the Employee Management System")


def employee_list(request):
    if request.method == 'GET':
        return HttpResponse("Here are our employees")
    return HttpResponse("Unsupported request method")
