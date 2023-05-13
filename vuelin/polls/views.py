from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def getCountries():
    return ['Barcelona','Paris','London']

def getPlayerNames():
    return ['Laura', 'Marc', 'Paula','Pere', '...', '...','...','...','...','...']

def index(request):
    return render(request,"index.html")

def gameCreator(request):
    countries = getCountries()
    context = {"countries": countries}
    return render(request,'gameCreator.html',context)

def waitingRoomHost(request):
    players = getPlayerNames()
    context = {"players": players}
    return render(request,'waitingRoomHost.html',context)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)