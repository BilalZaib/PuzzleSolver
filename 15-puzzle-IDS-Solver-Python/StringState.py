class StringState:
    Stringst = ""

    def __init__(self, s):
        self.Stringst = self.convertToString(s)

    def convertToString(self, s):
        stile = s.getTiles()
        finalString = stile[0].getName()
        for i in range(1,s.getTotalTiles()):
            finalString += stile[i].getName()
        return finalString

    def getStringState(self):
        return self.Stringst
    def setStringState(self, s):
        self.Stringst = s