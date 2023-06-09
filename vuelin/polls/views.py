from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django import forms
import os

from time import sleep 
import playerController as pl


pc = pl.PlayerController()
rounds = 0
global myPrompt
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
    return pc.hasGameStarted()

def getPromptWord():
    return pc.getMyWord()

def getImage():
    return os.path.abspath(os.path.dirname("/home/laura/Downloads"))
    

def getOtherPrompt():
    return "Una frase d'algú random"

def getAuthor():
    return "Algú random"

def getImages():
    return 

def getGuesses():
    return ["Una frase semblant", "Una full random"]

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
      
    print("nova crida a waiting") 
    if gameIsReady():
        return redirect('writePrompt')
    else:
        pn = pc.getPlayerNames()
        rounds = len(pn)-1
        sleep(1) 
        return render(request,'waitingRoomPlayer.html',{'redirect_url': '/polls/waitingRoomPlayer'})
    
class PromptForm(forms.Form):
    prompt = forms.CharField(max_length=50,label='')

prompt = "not defined"
global word

def writePrompt(request):
    global word
    global myPrompt 
    print("write prompt")
    print(request.method)
    if request.method == 'POST':
        print("method")
        form = PromptForm(request.POST)
        if form.is_valid():
            prompt = form.cleaned_data['prompt']  
            myPrompt = prompt         
            print(prompt)
            if word in prompt.upper():
                print("valid")
                pc.setInitialQuote(prompt)
                print("kañkljd")
                return redirect('canvas')
            else:
                return render(request,'writePrompt.html',{"promptWord": word,'form': form})
    else:
        form = PromptForm()
        word = getPromptWord().upper()
    return render(request,'writePrompt.html',{"promptWord": word,'form': form})

class PlayerNameForm(forms.Form):
    name = forms.CharField(max_length=50,label='')

def playerNameInput(request):
      
    if request.method == 'POST':
        form = PlayerNameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            pc.registerPlayer(name)
            pc.connectToHost()
            pc.enterGame("abc")
            return redirect('waitingRoomPlayer')
    else:
        form = PlayerNameForm()
    return render(request,'playerNameInput.html',{'form': form})

def canvas(request):    
    sentence = pc.receiveSentence()   
    return render(request,"canvas.html",{'redirect_url': '/polls/guessDrawing', "sentence": sentence})

class GuessingForm(forms.Form):
    guess = forms.CharField(max_length=50,label='')

def guessDrawing(request):
    im = getImage()

    username = request.user
    print(username)

    if request.method == 'POST':
        form = GuessingForm(request.POST)
        if form.is_valid():
            guess = form.cleaned_data['guess']
            return redirect('results')
    else:
        form = GuessingForm()
    return render(request,'guessDrawing.html',{'form': form, "user":username, "image": im})

def results(request):
    global myPrompt 
    images = getImages()
    guesses = getGuesses()
    context = {
        "original_prompt": myPrompt,
        "images": images,
        "guesses":guesses 
    }
    return render(request, "results.html",context)