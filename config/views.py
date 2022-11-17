from django.http import HttpResponse


def index(request):
    return HttpResponse('Привіт, це головна сторінка!')