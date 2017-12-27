class Tile:
    numberName = ""
    index = 0

   #Constructor for class Tile
    def __init__(self, name,ind):
        self.numberName = name
        self.index = ind


    #Setters
    def setName(self,s):
        self.numberName = s

    def setIndex(self,ind):
        self.index = ind

    #Getters
    def getName(self):
        return self.numberName

    def getIndex(self):
        return self.index

    def couldMoveRight(self):
        if ((self.index - 3) % 4 != 0):
            return True
        return False
    def couldMoveLeft(self):
        if ((self.index % 4 != 0)):
            return True
        return False
    def couldMoveUp(self):
        if ((self.index-3 > 0)):
            return True
        return False
    def couldMoveDown(self):
        if ((self.index -12 < 0)):
            return True
        return False