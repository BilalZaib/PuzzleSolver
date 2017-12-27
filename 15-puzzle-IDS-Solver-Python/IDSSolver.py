from StringState import StringState
from Tile import Tile
from State import State

class IDSSolver:
    stateToSolve = 0
    goal = "0123456789ABCDEF"
    goal2 = "123456789ABCDEF0"
    previous = {} #Dictionary to avoid duplicates
    solution = ""
    solveState = 0
    solved = False
    maxDepth = 9999999

    #-1,-1 for decrement of coordinates
    up = -4
    down = 4
    left = -1
    right = 1

    #constructor
    def __init__(self,s):
        self.solveState = self.duplicateState(s)
        self.stateToSolve = self.duplicateState(s)
        self.IDDFS(s)

    def IDDFS(self,s):
        temp = self.duplicateState(s)
        for i in range(0,self.maxDepth+1):
            IDSSolver.previous[StringState(s).getStringState()] = None
            self.DLS(temp,i)
            if(self.solved == True):
                self.solution = self.solveState.getSolution()
                print("#########\n# Solved #\n#########")
                print(self.solution)
                return
            print("\nIteration : ", i, " Complete and Map is Cleared\n")
            self.previous.clear()

        if (self.solution == "" or self.solution == (None)):
            print("no solution")
    def DLS(self,s,limit):
        if (self.goalReached(s)):
            self.solveState = s
            self.solved = True
            print("Solution found")
            return
        if(limit<=0):
             return
        self.explore(s,limit-1)

    def duplicateState(self,s):
        l = s.getLength()
        w = s.getWidth()
        tempTs = []
        p = s.getTiles()
        for i in range(0,s.getTotalTiles()):
            name = p[i].getName()
            ind = p[i].getIndex()
            t = Tile(name, ind)
            tempTs.append(t)
        state = State(l,w,tempTs)
        state.setNumMoves(s.getNumMoves())
        state.setSolution(s.getSolution())
        return state

    def goalReached(self,s):
        ss = StringState(s).getStringState()
        if (ss == (self.goal) or ss == (self.goal2)):
            return True;
        return False;
    def movable(self,s):
        p = s.getTiles()
        for i in range(0,s.getTotalTiles()):
            if(p[i].getName() == "0"):
                return i
        return -1 #Error
    def makeStack(self,nextt,pre,s,limit):
        if(nextt not in self.previous):
            self.previous[nextt] = pre
            # print("MakeStack: " , nextt)
            self.DLS(s, limit)
        #else:
            #print("Already Visited")


   # helps explore moves

    def explore(self,s,limit):
        if (self.solved != True):
            self.moveLeft(s, limit)
        if (self.solved != True):
            self.moveRight(s, limit)
        if (self.solved != True):
            self.moveUp(s, limit)
        if (self.solved != True):
            self.moveDown(s, limit)

    def moveLeft(self,s,limit):
        p = s.getTiles()
        if(p[self.movable(s)].couldMoveLeft() == True):
            ss = StringState(s)
            #print("LEFT: " , ss.getStringState() , limit)
            copyS = self.duplicateState(s)
            moveI = self.movable(s)
            copyS.getTiles()[moveI].setName(copyS.getTiles()[moveI+self.left].getName())
            copyS.getTiles()[moveI+self.left].setName("0")
            copyS.addSteps("left\n")
            tempSS = StringState(copyS)
            self.makeStack(tempSS.getStringState(), ss.getStringState(), copyS, limit)

    def moveRight(self, s, limit):
        p = s.getTiles()
        if (p[self.movable(s)].couldMoveRight() == True):
            ss = StringState(s)
            #print("Right: ", ss.getStringState(), limit)
            copyS = self.duplicateState(s)
            moveI = self.movable(s)
            copyS.getTiles()[moveI].setName(copyS.getTiles()[moveI + self.right].getName())
            copyS.getTiles()[moveI + self.right].setName("0")
            copyS.addSteps("right\n")
            tempSS = StringState(copyS)
            self.makeStack(tempSS.getStringState(), ss.getStringState(), copyS, limit)

    def moveUp(self, s, limit):
        p = s.getTiles()
        if (p[self.movable(s)].couldMoveUp() == True):
            ss = StringState(s)
            #print("UP : ", ss.getStringState(), limit)
            copyS = self.duplicateState(s)
            moveI = self.movable(s)
            copyS.getTiles()[moveI].setName(copyS.getTiles()[moveI + self.up].getName())
            copyS.getTiles()[moveI + self.up].setName("0")
            copyS.addSteps("up\n")
            tempSS = StringState(copyS)
            self.makeStack(tempSS.getStringState(), ss.getStringState(), copyS, limit)

    def moveDown(self, s, limit):
        p = s.getTiles()
        if (p[self.movable(s)].couldMoveDown() == True):
            ss = StringState(s)
            #print("DOWN: ", ss.getStringState(), limit)
            copyS = self.duplicateState(s)
            moveI = self.movable(s)
            copyS.getTiles()[moveI].setName(copyS.getTiles()[moveI + self.down].getName())
            copyS.getTiles()[moveI + self.down].setName("0")
            copyS.addSteps("down\n")
            tempSS = StringState(copyS)
            self.makeStack(tempSS.getStringState(), ss.getStringState(), copyS, limit)