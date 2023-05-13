import socket as sc

class PlayerController:
    def __init__(self):
        pass
        
    def connectToHost(self):
        print("ConnectToHost")
        self.client = sc.socket(sc.AF_BLUETOOTH, sc.SOCK_STREAM, sc.BTPROTO_RFCOMM)
        self.client.connect(("c8:b2:9b:1a:74:b1", 4))


    def enterGame(self, name):
        print("EnterGame " + str(name))
        self.client.send(name.encode("utf-8"))


    def getPlayerNames(self):
        return self.client.recv(4096).decode("utf-8").split(";")
        

    def finish(self):
        self.client.close()

