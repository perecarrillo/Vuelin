import socket as sc

client = sc.socket(sc.AF_BLUETOOTH, sc.SOCK_STREAM, sc.BTPROTO_RFCOMM)
client.connect(("c8:b2:9b:1a:74:b1", 4))

message = input("input game name:")
message = client.send(message.encode("utf-8"))

playerNames = client.recv(4096).decode("utf-8").split(";")

print(playerNames)

class Client:
    def __init__(self):
        self.host = str()
        self.nom = str()
        self.adr = str()
        self.gameCode = str()

    def getHost(self):
        return self.host
    
    def setHost(self, h):
        self.host = h
    
    def setNom(self, name):
        self.nom = name

    def getNom(self):
        return self.nom
    
    def setAdr(self, a):
        self.adr = a

    def getAdr(self):
        return self.adr

    def getGameCode(self):
        return self.gameCode
    
    def getPlayers(self):
        return host.getPlayers()


client.close()

# try:
#     while True:
#         message = input("Enter message: ")
#         client.send(message.encode("utf-8"))
#         data = client.recv(1024)
#         if not data:
#             break
#         print(f"Message: {data.decode('utf-8')}")
# except OSError as e:
#     pass

# client.close()