from django.shortcuts import render
from fqs.models import PreguntasFrecuentes

def inicio(request):
    fqs = PreguntasFrecuentes.objects.all()
    return render(request, 'fqs.html', {'fqs': fqs})
