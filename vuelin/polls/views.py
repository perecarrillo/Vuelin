from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django import forms

from time import sleep 
import playerController as pl


# playerloco = pl.Player()
# playerloco.connectToHost()
# playerloco.enterGame("abc")

def getCountries():
    return [('barcelona','Barcelona'),('paris','Paris'),('london','London')]

def getPlayerNames():
    return ['Laura', 'Marc', 'Paula','Pere', '...', '...','...','...','...','...']
    #return playerloco.getPlayerNames()

def getCodes():
    return ['a','b','c']

def index(request):
    return render(request,"index.html")

def gameIsReady():
    return True

def getPromptWord():
    return "holi"

class CountriesForm(forms.Form):
    destination = forms.ChoiceField(choices=getCountries())
    code = forms.CharField(max_length=50)

def gameCreator(request):
    if request.method == 'POST':
        form = CountriesForm(request.POST)
        if form.is_valid():
            destination = form.cleaned_data['destination']
            code = form.cleaned_data['code']
            print(destination + code)
            return redirect('waitingRoomHost')
    else:
        form = CountriesForm()
    return render(request, 'gameCreator.html', {'form': form})    

def waitingRoomHost(request):
    players = getPlayerNames()
    context = {"players": players}
    return render(request,'waitingRoomHost.html',context)

def waitingRoomPlayer(request):
    sleep(1)
    if gameIsReady():
        return redirect('writePrompt')
    else:
        return render(request,'waitingRoomPlayer.html')
    
class PromptForm(forms.Form):
    prompt = forms.CharField(max_length=50,label='')

prompt = "not defined"

def writePrompt(request):
    word = getPromptWord().upper()
    if request.method == 'POST':
        form = PromptForm(request.POST)
        if form.is_valid():
            prompt = form.cleaned_data['prompt']
            print(prompt)
            if word in prompt.upper():
                return redirect('canvas')
            else:
                return render(request,'writePrompt.html',{"promptWord": word,'form': form})
    else:
        form = PromptForm()
    return render(request,'writePrompt.html',{"promptWord": word,'form': form})

class PlayerNameForm(forms.Form):
    name = forms.CharField(max_length=50,label='')

def playerNameInput(request):
    if request.method == 'POST':
        form = PlayerNameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            print(name)
            return redirect('waitingRoomPlayer')
    else:
        form = PlayerNameForm()
    return render(request,'playerNameInput.html',{'form': form})

def canvas(request):    
    return render(request,"canvas.html",{'redirect_url': '/polls', "prompt": prompt})
