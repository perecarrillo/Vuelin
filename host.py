import socket as sc
import _thread as th
import time

start = False

class Host:
    def __init__(self):
        self.mac = self.getMacAddress()
        self.server = sc.socket(sc.AF_BLUETOOTH, sc.SOCK_STREAM, sc.BTPROTO_RFCOMM)
        self.server.bind((self.mac, 4))
        self.players = []
        self.name = str()
        self.destination = str()
        self.gameCode = str()
        self.resultat = dict()
        self.round = int()
        self.paraulesPais = {
            "France" : ["Torre Eiffel", "París", "ciudad del amor"],
            "Spain" : ["Sevilla", "paella", "Barcelona", "Sagrada Família"]
        }
        self.paraula = str()
    
    def getMacAddress(self):
        return "c8:b2:9b:1a:74:b1"

    def listenForPlayers(self):
        while True:
            self.server.listen(10)
            player, addr = self.server.accept()
            roomNumber = player.recv(4096)
            if (roomNumber == self.gameCode): 
                self.players.append(Player(player, addr))
                print(str(addr) + "accepted!")
            else:
                print(str(addr) + "rejected!")
                player.close()

    def sendPlayerNamesToEveryone(self):
        for p in self.players:
            self.sendToPlayer(p, ",".join(x.getName() for x in self.players))

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
    
class Player:
    def __init__(self, id, addr):
        self.id = id
        self.addr = addr

host = Host()
th.start_new_thread(host.listenForPlayers, ())

while not start:
    host.sendPlayerNamesToEveryone()
    time.sleep(2)

#codi pagines 5-final
# un cop es dona play
# escull una paraula random del pais
host.paraula = choice(host.paraulesPais[host.getDestination])
for p in host.players:
    p.setParaula(choice(host.paraulesPais[host.getDestination]))

while not 



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