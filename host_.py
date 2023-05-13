class host:

    def __init__(self):
        self.name = ""
        self.destination = ""
        self.gamecode = ""
        self.players = dict()
        self.resultat = dict() 
        # clau es un pair de la frase inicial i el jugador i el valor es la llista de cada imatge i frase creada per cada jugador
        self.round = int()

    def setDestination(self, name):
        self.destination = name

    def getDestination(self):
        return self.destination
    
    def setGameCode(self, string):
        self.gamecode = string

    def getGameCode(self):
        return self.gamecode
    
    def getPlayers(self):
        return self.players.len()
    
    def setRound(self, num):
        self.round = num
    
    def getRound(self):
        return self.round
    