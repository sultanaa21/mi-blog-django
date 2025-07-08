from django.http import HttpResponse

def inicio(request):
    return HttpResponse("<h1>¡Hola! Esta es mi primera página con Django</h1>")