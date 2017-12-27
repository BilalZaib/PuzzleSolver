class Issolveable:
    arr = ""

    def __init__(self, s):
        self.arr = s

    def getintval(self, value):
        if value == 'A':
            return 10
        elif value == "B":
            return 11
        elif value == "C":
            return 12
        elif value == "D":
            return 13
        elif value == "E":
            return 14
        elif value == "F":
            return 15
        return int(value)

    def getinvcount(self):
        invcount = 0
        for i in range(0, 15):
            for j in range(i + 1, 16):
                if self.getintval(self.arr[i]) != 0 and self.getintval(self.arr[j]) != 0 and self.getintval(
                        self.arr[i]) > self.getintval(self.arr[j]):
                    invcount += 1
        return invcount

    def findXPosition(self):
        for i in range(0, 16):
            if self.arr[i] == '0':
                return 4 - int(i / 4)

    def isSolveable(self):
        invCount = self.getinvcount()
        pos = self.findXPosition()
        print("Iversion Count :",invCount)
        print("Position of X :", pos)

        if pos % 2 == 0:
            if invCount % 2 != 0:
                #print("Position is Even and Inversion is Odd")
                #print("State is Solveable")
                return True
        else:
            if invCount % 2 == 0:
                #print("State is Solveable")
                #print("Position is Odd and Inversion is Even")
                return True

        #print("State is not Solveable")
        return False
