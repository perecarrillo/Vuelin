import vuelin.playerController as pl
import time

pc = pl.PlayerController()

name = input("Input your name: ")
pc.registerPlayer(name)

pc.connectToHost()

pc.enterGame("abc")

while not pc.hasGameStarted():
    print(pc.getPlayerNames())
    time.sleep(2)

# Game Starts

initialQuote = input("Input your initial sentence, it must contain the word " + pc.getMyWord() + ": ")
# Comprovar prompt
pc.setInitialQuote(initialQuote)

rounds = pc.getRounds()
quoteRound = True
for i in range(rounds):
    if quoteRound:
        sentence = pc.receiveSentence()
        print("Draw this: " + sentence)

        photo = readPhoto()
        pc.sendPhoto(photo)

    else: 
        photo = pc.receivePhoto()
        showPhoto(photo)
        sentence = input("Write a sentence that describes this photo: ")
        pc.sendSentence(sentence)

# Game has finished

hist = pc.getHistory()
print("History: ")
print(hist)

pc.finish()