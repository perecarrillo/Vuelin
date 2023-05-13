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
        return self.host.recv(4096).decode("utf-8").split(";")
        

    def finish(self):
        self.host.close()

    def hasGameStarted(self):
        #msg = "#gameStarted?#"
        #self.host.send(msg.encode("utf-8"))
        return e.stringToBool(self.host.recv(1024).decode("utf-8"))
    
    def getMyWord(self):
        return self.host.recv(1024).decode("utf-8")
    
    def setInitialQuote(self, string):
        #msg = "#Quote#" + string
        self.host.send(string.encode("utf-8"))

    def getRounds(self):
        #msg = "#NRounds?#"
        #self.host.send(msg.encode("utf-8"))
        return e.stringToInt(self.host.recv(1024).decode("utf-8"))
    
    def receiveSentence(self):
        return self.host.recv(4096).decode("utf-8")
    
    def sendPhoto(self, photo):
        self.host.send(e.jpgToByteArray(photo))

    def receivePhoto(self):
        return e.ByteArrayToJpg(self.host.recv(4096))
    
    def sendSentence(self, string):
        self.host.send(string.encode("utf-8"))

    def getHistory(self):
        return e.stringToArray(self.host.recv(4096).decode("utf-8"))