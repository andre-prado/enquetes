from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# def caminho_teste(request):
#     return HttpResponse("Olá, você está na página de teste.")
