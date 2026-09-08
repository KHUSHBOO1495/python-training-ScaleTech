from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello from Django!")

def about(request):
    return HttpResponse("This is the about page.")