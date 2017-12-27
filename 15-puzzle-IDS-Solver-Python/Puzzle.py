from Tile import Tile
from State import State
from StringState import StringState
from IsSolveable import Issolveable
from IDSSolver import IDSSolver


def readInTile( str, tiles):
    sstr = str.split()
    for i in range(0,len(sstr)):
        t = Tile(sstr[i], i)
        tiles.append(t)

#print a State
def printState(s):
    t = s.getTiles()
    for i in range(0,16):
        print(t[i].getName())


str = "1 7 2 4 5 6 3 8 9 0 A C D E B F"#Solveable
str1 = "1 2 3 4 5 6 7 8 9 0 B C D A E F"#Solveable
str2 = "1 2 3 4 5 6 7 8 9 A B C D F E 0"#Not Solveable
str3 = "D 2 A 3 1 C 8 4 5 0 9 6 F E B 7"#Solveable
str4 = "6 D 7 A 8 9 B 0 F 2 C 5 E 3 1 4"#Solveable
str5 = "3 9 1 F E B 4 6 D 0 A C 2 7 8 5"#Not Solveable

tiles = []
readInTile(str1, tiles)
s = State(4,4,tiles)
if(Issolveable(StringState(s).getStringState()).isSolveable() == True):
    print("State is Solveable")
else:
    print("State is not Solveable")
    import sys
    sys.exit()
solve = IDSSolver(s)
import sys
sys.exit()


