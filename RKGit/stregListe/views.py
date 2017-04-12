from django.shortcuts import render
from stregListe.models import Vejleder, Indkoeb

# Create your views here.
def alleVejledere(request):
    alle = Vejleder.objects.all().order_by('-nrBeers')
    data = []
    for person in alle:
        data.append(person.toDict())
    return render(request, "stregListe/index.html", {'data': data})


def eventOversigt(request):
    print("HERE")
    alle = Indkoeb.objects.all().order_by('-date')
    data = []
    for event in alle:
        data.append(event.toDict())
    return render(request, 'stregListe/oversigt.html', {'data': data})
