import playerController as pl
import time

pc = pl.PlayerController()

name = input("Input your name: ")
pc.registerPlayer(name)

pc.connectToHost()

pc.enterGame("abc")


rounds = 0
while not pc.hasGameStarted():
    pn = pc.getPlayerNames()
    rounds = len(pc.getPlayerNames())-1
    print(pn)
    time.sleep(2)


# Game Starts

initialQuote = input("Input your initial sentence, it must contain the word " + pc.getMyWord() + ": ")
# Comprovar prompt
pc.setInitialQuote(initialQuote)

quoteRound = False # cert si et toca escriure
print("entro", rounds)
for i in range(rounds):
    if quoteRound:
        print("EscriureFrase")
        photo = pc.receivePhoto()
        showPhoto(photo)
        sentence = input("Write a sentence that describes this photo: ")
        pc.sendSentence(sentence)
        
    else: 
        print("Dibuixar")
        sentence = pc.receiveSentence()
        print("Draw this: " + sentence)

        photo = readPhoto()
        pc.sendPhoto(photo)

print("surto")
# Game has finished

hist = pc.getHistory()
print("History: ")
print(hist)

pc.finish()