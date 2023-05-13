import socket as sc
import _thread as th
import time
import random

start = False

class Host:
    def __init__(self):
        self.mac = self.getMacAddress()
        self.server = sc.socket(sc.AF_BLUETOOTH, sc.SOCK_STREAM, sc.BTPROTO_RFCOMM)
        self.server.bind((self.mac, 4))
        self.players = [] #array de players
        self.name = str()
        self.destination = str()
        self.gameCode = "abc"
        self.round = int()
        self.paraulesPais = {
            "France" : ["Torre Eiffel", "París", "ciudad del amor"],
            "Spain" : ["Sevilla", "paella", "Barcelona", "Sagrada Família"]
        }
        self.frasesInicials = []
        self.historial = []
        self.assignacions = {}
    
    def getMacAddress(self):
        return "c8:b2:9b:1a:74:b1"

    def listenForPlayers(self):
        while True:
            self.server.listen(10)
            player, addr = self.server.accept()
            print("accepted, waiting for recv")
            roomNumber = None
            while not roomNumber:
                roomNumber = (player.recv(4096)).decode("utf-8")
                print(roomNumber)
            print("recieved")
            if (roomNumber == self.gameCode): 
                self.players.append(Player(player, addr))
                print(str(addr) + " accepted!")
            else:
                print(str(addr) + " rejecteed! " + roomNumber)
                player.close()

    def sendPlayerNamesToEveryone(self):
        for p in self.players:
            self.sendToPlayer(p, ";".join(x.getName() for x in self.players))

    def sendToPlayer(self, player, message):
        player.id.send(message.encode("utf-8"))

    def setDestination(self, name):
        self.destination = name

    def getDestination(self):
        return self.destination
    
    def setGameCode(self, string):
        self.gameCode = string

    def getGameCode(self):
        return self.gameCode
    
    def getNumPlayers(self):
        return len(self.players)
    
    def setRound(self, num):
        self.round = num
    
    def getRound(self):
        return self.round
    
    def getPlayers(self):
        result = []
        for p in self.players:
            result.append(p.id)
        return result
    
    def filterFrases(self, visited, available):
        filtered = [1] * list(range(len(self.players)))
        filtered2 = [0] * list(range(len(self.players)))
        for i in visited:
            filtered[i] = 0
        for i in available:
            filtered2[i] = 1
        resultat = []
        for i in range(len(self.players)):
            if filtered[i] and filtered2[i]:
                resultat.append(i)
        return resultat
    
    def getLastAssignacio(self, name):
        return self.assignacions[name][-1]

    
class Player:
    def __init__(self, id, addr):
        self.id = id
        self.addr = addr
    
    def getName(self):
        self.id = "Hey"
        return self.id

host = Host()
th.start_new_thread(host.listenForPlayers, ())

for p in host.players:
    host.assignacions[p.getNom()] = []

while not start:
    host.sendPlayerNamesToEveryone()
    time.sleep(2)

#codi pagines 5-final
numPlayers = len(host.players)
# un cop es dona play
# escull una paraula random del pais
for p in host.players:
    p.setParaula(random.choice(host.paraulesPais[host.getDestination]))


# Crear frases inicials
contador = 0
while contador < numPlayers:
    fr, p = esperar_frase()
    host.frasesInicials.append([fr, p])
    contador += 1

# frasesDisponibles = list(range(numPlayers))
# for p in host.players:
#     frases = host.filterFrases([], frasesDisponibles) # conjunt de frases que encara no s'han assignat a aquesta ronda
#     num = (random.randint(len(frases)))
#     frasesDisponibles.remove(num)
#     p.enviar_frase(host.frasesInicials[num][0])


it_frase = False
cont = 0
for i in range (1, numPlayers): #numero de rondes
    # if it_frase:
    frasesDisponibles = list(range(numPlayers))
    for p in host.players:
        visited = host.assignacions[p.getName()]
        frases = host.filterFrases(visited, frasesDisponibles) # conjunt de frases que encara no s'han assignat a aquesta ronda
        num = (random.randint(len(frases)))
        frasesDisponibles.remove(num)
        if it_frase:
            p.enviar_frase(host.frasesInicials[num][0])
        else:
            p.enviar_draw(host.frasesInicials[num][0])
        visited.append(num)
        host.assignacions[p.getName()] = visited

    contador = 0
    draws = [0] * numPlayers
    while contador < numPlayers:
        dr, p = esperar_draw()
        idxFrase = host.getLastAssignacio(p.getName())
        draws[idxFrase] = dr
        contador += 1
    host.historial.append(draws)

            
















it_frase = False
frasesAnt = host.frasesInicials
imatgesAnt = []

for i in range(numPlayers):
    if it_frase:
        contador = 0
        frases = []
        while contador < numPlayers:
            fr, p = esperar_frase()
            frases.append(fr)
            contador += 1
        llb = [1] * numPlayers
        for f in frases:
            num = (random.randint(0, numPlayers-1)) % numPlayers
            while not llb[num]:
                num = (random.randint(0, numPlayers-1)) % numPlayers
            llb[num] = 0
            host.players[num] = enviar_frase(f)
        host.historial.append()
    else:
        pass
        
    it_frase = not it_frase



# server = sc.socket(sc.AF_BLUETOOTH, sc.SOCK_STREAM, sc.BTPROTO_RFCOMM)
# server.bind(("c8:b2:9b:1a:74:b1", 4))
# server.listen(1)

# client, addr = server.accept()

# try:
#     while True:
#         data = client.recv(1024)
#         if not data:
#             break
#         print(f"Message: {data.decode('utf-8')}")
#         message = input("Enter message:")
#         client.send(message.encode("utf-8"))
# except OSError as e:
#     pass

# client.close()
# server.close()