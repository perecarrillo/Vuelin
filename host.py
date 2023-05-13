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
        self.players = []
        self.name = str()
        self.destination = str()
        self.gameCode = "abc"
        self.resultat = dict()
        self.round = int()
        self.paraulesPais = {
            "France" : ["Torre Eiffel", "París", "ciudad del amor"],
            "Spain" : ["Sevilla", "paella", "Barcelona", "Sagrada Família"]
        }
        self.frasesInicials = []
        self.historial = []
    
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
    
class Player:
    def __init__(self, id, addr):
        self.id = id
        self.addr = addr
    
    def getName(self):
        return "Hey "

host = Host()
th.start_new_thread(host.listenForPlayers, ())

while not start:
    host.sendPlayerNamesToEveryone()
    time.sleep(2)

#codi pagines 5-final
numPlayers = len(host.players)
# un cop es dona play
# escull una paraula random del pais
for p in host.players:
    p.setParaula(random.choice(host.paraulesPais[host.getDestination]))

contador = 0
while contador < numPlayers:
    fr = esperar_frase_inicial()
    host.frasesInicials.append(fr)
    contador = contador + 1

llb = [1] * numPlayers
for f in host.frasesInicials:
    num = random.randint(0, numPlayers-1)
    while not llb[num]:
        num = random.randint(0, numPlayers-1)
    llb[num] = 0
    host.players[num].enviar_frase(f)

it_frase = False
frasesAnt = host.frasesInicials
imatgesAnt = []
for i in (0, numPlayers-1):
    if it_frase:
        contador = 0
        frases = []
        while contador < numPlayers:
            fr, p = esperar_frase()
            frases.append(fr)
            contador = contador + 1
        llb = [1] * numPlayers
        for f in frases:
            num = random.randint(0, numPlayers-1)
            while not llb[num]:
                num = random.randint(0, numPlayers-1)
            llb[num] = 0
            host.players[num] = enviar_frase(f)
        host.historial.append()
    else:
        contador = 0
        imatges = []
        while contador < numPlayers:
            im, p = esperar_imatge()
            imatges.append(im)
            contador = contador + 1
        llb = [1] * numPlayers
        for j in imatges:
            num = random.randint(0, numPlayers-1)
            while not llb[num]:
                num = random.randint(0, numPlayers-1)
            llb[num] = 0
            host.players[num] = enviar_imatge(j)
            imatgesAnt[num] = 
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