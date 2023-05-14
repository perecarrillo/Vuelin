import socket as sc
import encoder as e

class PlayerController:
    name : str
    host : sc.socket

    def __init__(self):
        pass

    def registerPlayer(self, name):
        self.name = name
        
    def connectToHost(self):
        #print("ConnectToHost")
        self.host = sc.socket(sc.AF_BLUETOOTH, sc.SOCK_STREAM, sc.BTPROTO_RFCOMM)
        self.host.connect(("c8:b2:9b:1a:74:b1", 4))


    def enterGame(self, name):
        #print("EnterGame " + str(name))
        #msg = "#Enter#" + name
        self.host.send(name.encode("utf-8"))


    def getPlayerNames(self):
        msg = "#GetPlayerNames#"
        self.host.send(msg.encode("utf-8"))
        return self.receiveFrom(self.host).split(";")
        

    def finish(self):
        self.host.close()

    def receiveFrom(self, h):
        msg = None
        while not msg:
            msg = h.recv(4096).decode("utf-8")
        return msg

    def hasGameStarted(self):
        msg = "#gameStarted?#"
        self.host.send(msg.encode("utf-8"))
        return e.stringToBool(self.receiveFrom(self.host))
    
    def getMyWord(self):
        return self.receiveFrom(self.host)
    
    def setInitialQuote(self, string):
        #msg = "#Quote#" + string
        self.host.send(string.encode("utf-8"))

    def getRounds(self):
        #msg = "#NRounds?#"
        #self.host.send(msg.encode("utf-8"))
        return e.stringToInt(self.receiveFrom(self.host))
    
    def receiveSentence(self):
        return self.receiveFrom(self.host)
    
    def sendPhoto(self, photo):
        self.host.send(e.jpgToByteArray(photo))

    def receiveFromRaw(h):
        msg = None
        while not msg:
            msg = h.recv(4096)
        return msg

    def receivePhoto(self):
        return e.ByteArrayToJpg(self.receiveFromRaw(self.host))
    
    def sendSentence(self, string):
        self.host.send(string.encode("utf-8"))

    def getHistory(self):
        return e.stringToArray(self.receiveFrom(self.host))