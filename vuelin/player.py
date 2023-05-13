import socket as sc

client = None


def connectToHost():
    client = sc.socket(sc.AF_BLUETOOTH, sc.SOCK_STREAM, sc.BTPROTO_RFCOMM)
    client.connect(("c8:b2:9b:1a:74:b1", 4))


def enterGame(name):
    client.send(name.encode("utf-8"))


def getPlayerNames():
    return client.recv(4096).decode("utf-8").split(";")
    

def finish():
    client.close()

