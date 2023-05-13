import socket as sc
import _thread as th
import time

start = False



class Host:
    def __init__(self):
        self.mac = self.getMacAddress()
        self.server = sc.socket(sc.AF_BLUETOOTH, sc.SOCK_STREAM, sc.BTPROTO_RFCOMM)
        server.bind((self.mac, 4))
        self.players = []
    
    def getMacAddress(self):
        pass

    def setGameName(self, num):
        self.gameName = num

    def listenForPlayers(self):
        pass

    def sendPlayerNamesToEveryone(self):
        for p in self.players:
            p.send(",".join(x.getName() for x in self.players))
    
class Player:
    def __init__(self, id, addr):
        self.id = id
        self.addr = addr

    def send(self, message):
        self.id.send(message.encode("utf-8"))

host = Host()
th.start_new_thread(host.listenForPlayers, ("PlayerListener"))

while not start:
    host.sendPlayerNamesToEveryone()
    time.sleep(2)


server = sc.socket(sc.AF_BLUETOOTH, sc.SOCK_STREAM, sc.BTPROTO_RFCOMM)
server.bind(("c8:b2:9b:1a:74:b1", 4))
server.listen(1)

client, addr = server.accept()

try:
    while True:
        data = client.recv(1024)
        if not data:
            break
        print(f"Message: {data.decode('utf-8')}")
        message = input("Enter message:")
        client.send(message.encode("utf-8"))
except OSError as e:
    pass

client.close()
server.close()