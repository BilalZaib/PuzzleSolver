class State:
    length = 0
    width = 0
    numMoves = 0
    infoTable = []
    totalTiles = 0
    solution = ""

    def __init__(self, l, w, p):
        self.length = l
        self.width = w
        self.infoTable = p
        self.numMoves = 0
        self.totalTiles = 16
        self.solution = ""

    #Setters
    def setLength(self,l):
        self.length = l
    def setWidth(self,w):
        self.width = w
    def setTiles(self,p):
        self.infoTable = p
    def setNumMoves(self,i):
        numMoves = i
    def addSteps(self,s):
        self.solution += s
    def setSolution(self,s):
        self.solution = s

    #Getters
    def getLength(self):
        return self.width
    def getWidth(self):
        return self.length
    def getTiles(self):
        return self.infoTable
    def getNumMoves(self):
        return self.numMoves
    def getTotalTiles(self):
        return self.totalTiles
    def getSolution(self):
        return self.solution