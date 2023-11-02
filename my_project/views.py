from django.http import HttpResponse


def main_page(request):
    return HttpResponse("Hello World")


def contact(request):
    return HttpResponse("This is contact page")


def about(request):
    return HttpResponse("About us page")