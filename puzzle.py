from copy import deepcopy                                                   #imported from https://docs.python.org/3/library/copy.html for copying puzzle board states
import time                                                                 #imported from https://docs.python.org/3/library/time.html to keep track of CPU time

#puzzle node object
class puzzleNode:                                                           
    def __init__(self, puzzleState,depth,cost,heuristic, visitedStates):    #puzzle node object with necessary values
        self.puzzleState = puzzleState                                          
        self.depth = depth                                                      
        self.cost = cost
        self.heuristic = heuristic
        self.visitedStates = visitedStates

    #check if goal state is reached
    def goalTest(self):                                                     
        goalState = [[1,2,3],[4,5,6],[7,8,0]]
        if self.puzzleState == goalState:
            return True
        else:
            return False

    #print puzzle board
    def printPuzzle(self):
        for row in self.puzzleState:                
            for element in row:
                print(element, end=" ")                                    #print each element with a space between
            print("")                                                      #newline

    #Find indices for blank space
    def findBlank(self):
        for i in range(len(self.puzzleState)):                             #i represents row index
            for j in range(len(self.puzzleState[i])):                      #j represents column index
                if self.puzzleState[i][j] == 0:
                    return i,j                                             #return pair of indices


    #Check if left is possible
    def leftMoveAvailable(self):
        row, column = self.findBlank()
        #boolean for checking up
        left = False
        #check for left
        if column == 0:                                                    #first column
            left = False
        elif column == 1:                                                  #middle column
            left = True
        elif column == 2:                                                  #last column
            left = True
        
        if left:
            leftCopy = deepcopy(self.puzzleState)                          #make copy of original puzzle board using deepcopy, referred to https://docs.python.org/3/library/copy.html
            hold = leftCopy[row][column]                                   #store original value
            leftCopy[row][column] = leftCopy[row][column-1]                #swap
            leftCopy[row][column-1] = hold

            #check for duplicates
            for state in self.visitedStates:
                if state == leftCopy:
                    return False                                           #repeated state
            return True                                                    #can move left
        else:
            return False                                                   #illegal move

    #Check if right is possible
    def rightMoveAvailable(self):
        row, column = self.findBlank()
        #boolean for checking up
        right = False

        #check for left
        if column == 0:                                                    #first column
            right = True
        elif column == 1:                                                  #middle column
            right = True
        elif column == 2:                                                  #last column
            right = False
        
        if right:
            rightCopy = deepcopy(self.puzzleState)                         #make copy of original puzzle board using deepcopy, referred to https://docs.python.org/3/library/copy.html
            hold = rightCopy[row][column]                                  #store original value
            rightCopy[row][column] = rightCopy[row][column+1]              #swap
            rightCopy[row][column+1] = hold

            #check for duplicates
            for state in self.visitedStates:
                if state == rightCopy:
                    return False                                           #repeated state
            return True                                                    #can move right
        else:
            return False                                                   #illegal move

#Check if up is possible
    def upMoveAvailable(self):
        row, column = self.findBlank()
        #boolean for checking up
        up = False

        #check for up
        if row == 0:                                                       #top row
            up = False
        elif row == 1:                                                     #middle row
            up = True
        elif row == 2:                                                     #bottom row
            up = True
        
        if up:
            upCopy = deepcopy(self.puzzleState)                            #make copy of original puzzle board using deepcopy, referred to https://docs.python.org/3/library/copy.html
            hold = upCopy[row][column]                                     #store original value
            upCopy[row][column] = upCopy[row-1][column]                    #swap
            upCopy[row-1][column] = hold

            #check for duplicates
            for state in self.visitedStates:
                if state == upCopy:
                    return False                                           #repeated state
            return True                                                    #can move up
        else:
            return False                                                   #illegal move

    #Check if down is possible
    def downMoveAvailable(self):
        row, column = self.findBlank()
        #boolean for checking up
        down = False

        #check for down
        if row == 0:                                                       #top row
            down = True
        elif row == 1:                                                     #middle row
            down = True
        elif row == 2:                                                     #bottom row
            down = False

        if down:
            downCopy = deepcopy(self.puzzleState)                          #make copy of original puzzle board using deepcopy, referred to https://docs.python.org/3/library/copy.html
            hold = downCopy[row][column]                                   #store original value
            downCopy[row][column] = downCopy[row+1][column]                #swap
            downCopy[row+1][column] = hold

            #check for duplicates
            for state in self.visitedStates:
                if state == downCopy:
                    return False                                           #repeated state
            return True                                                    #can move down
        else:
            return False                                                   #illegal move

#move left
def getLeft(currNode):
    row, column = currNode.findBlank()
    leftCopy = deepcopy(currNode.puzzleState)                              #make copy of original puzzle board, documentation under https://docs.python.org/3/library/copy.html
    hold = leftCopy[row][column]                                           #store original value
    leftCopy[row][column] = leftCopy[row][column-1]                        #swap
    leftCopy[row][column-1] = hold
    return leftCopy

#move right
def getRight(currNode):
    row, column = currNode.findBlank()
    rightCopy = deepcopy(currNode.puzzleState)                             #make copy of original puzzle board, documentation under https://docs.python.org/3/library/copy.html
    hold = rightCopy[row][column]                                          #store original value
    rightCopy[row][column] = rightCopy[row][column+1]                      #swap
    rightCopy[row][column+1] = hold
    return rightCopy

#move up
def getUp(currNode):
    row, column = currNode.findBlank()
    upCopy = deepcopy(currNode.puzzleState)                                #make copy of original puzzle board, documentation under https://docs.python.org/3/library/copy.html
    hold = upCopy[row][column]                                             #store original value
    upCopy[row][column] = upCopy[row-1][column]                            #swap
    upCopy[row-1][column] = hold
    return upCopy

#move down
def getDown(currNode):
    row, column = currNode.findBlank()
    downCopy = deepcopy(currNode.puzzleState)                              #make copy of original puzzle board, documentation under https://docs.python.org/3/library/copy.html
    hold = downCopy[row][column]                                           #store original value
    downCopy[row][column] = downCopy[row+1][column]                        #swap
    downCopy[row+1][column] = hold
    return downCopy

#expand node
def expand(currNode,qf):                                                   #expand the current node for different moves
    if qf == 1:                                                            #uniform cost search
        currNode.heuristic = 0                                              
    elif qf == 2:                                                          #misplaced tile A*
        currNode.heuristic = misplacedHeuristic(currNode)
    elif qf == 3:                                                          #manhattan distance A*
        currNode.heuristic = 0
    expandedNodes = []  
    if currNode.leftMoveAvailable():                                       #check for left
        leftNode = puzzleNode(getLeft(currNode), currNode.depth+1, 1, currNode.heuristic, currNode.visitedStates)
        if qf == 1:                                                        #uniform cost search
            leftNode.heuristic = 0                                         
        elif qf == 2:                                                      #misplaced tile A*
            leftNode.heuristic = misplacedHeuristic(leftNode)
        elif qf == 3:                                                      #manhattan distance A*
            leftNode.heuristic = manhattanHeuristic(leftNode)
        leftNode.visitedStates.append(leftNode.puzzleState)
        expandedNodes.append(leftNode)                                     #add node to list
        
    if currNode.rightMoveAvailable():                                      #check for right
        rightNode = puzzleNode(getRight(currNode), currNode.depth+1, 1, currNode.heuristic, currNode.visitedStates)
        if qf == 1:                                                        #uniform cost search
            rightNode.heuristic = 0
        elif qf == 2:                                                      #misplaced tile A*
            rightNode.heuristic = misplacedHeuristic(rightNode)
        elif qf == 3:                                                      #manhattan distance A*
            rightNode.heuristic = manhattanHeuristic(rightNode)
        rightNode.visitedStates.append(rightNode.puzzleState)
        expandedNodes.append(rightNode)                                    #add node to list 

    if currNode.upMoveAvailable():                                  #check for up
        upNode = puzzleNode(getUp(currNode), currNode.depth+1, 1, currNode.heuristic, currNode.visitedStates)
        if qf == 1:                                                        #uniform cost search
            upNode.heuristic = 0    
        elif qf == 2:                                                      #misplaced tile A*
            upNode.heuristic = misplacedHeuristic(upNode)
        elif qf == 3:                                                      #manhattan distance A*
            upNode.heuristic = manhattanHeuristic(upNode)
        upNode.visitedStates.append(upNode.puzzleState)
        expandedNodes.append(upNode)                                       #add node to list
        
    if currNode.downMoveAvailable():                                       #check for down
        downNode = puzzleNode(getDown(currNode), currNode.depth+1, 1, currNode.heuristic, currNode.visitedStates)
        if qf == 1:                                                        #uniform cost search
            downNode.heuristic = 0
        elif qf == 2:                                                      #misplaced tile A*
            downNode.heuristic = misplacedHeuristic(downNode)
        elif qf == 3:                                                      #manhattan distance A*
            downNode.heuristic = manhattanHeuristic(downNode)
        downNode.visitedStates.append(downNode.puzzleState)
        expandedNodes.append(downNode)                                     #add node to list  
    
    return expandedNodes                                                   #return list of expanded nodes

#get misplaced tile heuristic           
def misplacedHeuristic(puzzleNode):
    goalState = [[1,2,3],[4,5,6],[7,8,0]]                           
    misplacedVal = 0                                

    for i in range(len(puzzleNode.puzzleState)):                           #iterate index of row
        for j in range(len(puzzleNode.puzzleState)):                       #iterate index of column
            if puzzleNode.puzzleState[i][j] != 0 and puzzleNode.puzzleState[i][j] != goalState[i][j]:     #if a tile is misplaced
                misplacedVal += 1                                          #increment heuristic value
    return misplacedVal           

#get manhattan distance heuristic
def manhattanHeuristic(puzzleNode):
    goalState = [[1,2,3],[4,5,6],[7,8,0]]
    check = [1,2,3,4,5,6,7,0]                                              #list to compare value
    manhattanVal = 0
    problemI = 0                                                           #index i of the problem node
    problemJ = 0                                                           #index j of the problem node
    goalI = 0                                                              #index i of the goal node
    goalJ = 0                                                              #index j of the goal node
    for value in check:                                                    #iterate through the check list
        for i in range(len(puzzleNode.puzzleState)):
            for j in range(len(puzzleNode.puzzleState)):
                if goalState[i][j] == value:                               #store indices of the problem node puzzle
                    goalI = i
                    goalJ = j
                if puzzleNode.puzzleState[i][j] == value:                  #store indices of the goal state
                    problemI = i
                    problemJ = j
        manhattanVal += abs(problemI - goalI) + abs(problemJ - goalJ)      #calculate manhattan distance using summation of the shift values of the indices
    return manhattanVal

#general search algorithm
def generalSearch(problem,qf):                                             #general search algorithm using different heuristics and queueing techniques for different algorithms
    algType = qf   
    timeStart = time.time()                                                #time before algorithm starts, documentation under https://docs.python.org/3/library/time.html
    expandedNodesVal = 0
    maxQueueSize = 0
    puzzleQueue = []                                                       #use a list implemented as a FIFO queue, documentation under https://docs.python.org/3/tutorial/datastructures.html     
    firstNode = puzzleNode(problem,0,0,0,[])                                
    if qf == 1:                                                            #uniform cost search heuristic, AKA 0
        firstNode.heuristic = 0
    elif qf == 2:                                                          #misplaced tile heuristic
        firstNode.heuristic = misplacedHeuristic(firstNode)
    elif qf == 3:                                                          #manhattan distance heuristic
        firstNode.heuristic = manhattanHeuristic(firstNode)
    puzzleQueue.append(firstNode)                                          #insert first node to the "queue" list, documentation under https://docs.python.org/3/tutorial/datastructures.html
    while puzzleQueue:  
        if algType != 1:                                                   #sort the queue by heuristic for A* algorithm
            puzzleQueue = sorted(puzzleQueue, key=lambda puzzle: (puzzle.depth +  (puzzle.cost + puzzle.heuristic), puzzle.depth)) # sorted function implementation, referred to https://docs.python.org/3/howto/sorting.html                                     
        if not puzzleQueue:                                                #if no nodes, faill
            return "failure"        
        currNode = puzzleQueue.pop(0)                                      #pop value, documentation under https://docs.python.org/3/tutorial/datastructures.html
        if currNode.cost == 0:                                             #print initial problem state
            print("The initial problem state is: ")
            currNode.printPuzzle()
        if currNode.goalTest():                                            #solution
            timeComplete = time.time()                                     #time at completetion, documentation under https://docs.python.org/3/library/time.html
            cpuTime = timeComplete - timeStart                             #calculated total seconds, documentation under https://docs.python.org/3/library/time.html
            print("")
            print("Goal State!")
            currNode.printPuzzle()
            print("")
            print("Solution depth: " + str(currNode.depth))         
            print("Number of nodes expanded: " + str(expandedNodesVal))
            print("Max queue size: " + str(maxQueueSize))
            print("")
            #TEST
            print("CPU Time: " + str(cpuTime) + " seconds")         
            return currNode                                                #goal state reached 
        else:                                                              #print the expansion of the puzzle
            if algType == 1:
                print("The best state to expand with a g(n) = " + str(currNode.cost) + " and h(n) = 0 is...")
            elif algType == 2:
                print("The best state to expand with a g(n) = " + str(currNode.cost) + " and h(n) = " + str(misplacedHeuristic(currNode)) + " is...")
            elif algType == 3:
                print("The best state to expand with a g(n) = " + str(currNode.cost) + " and h(n) = " + str(manhattanHeuristic(currNode)) + " is...")
            currNode.printPuzzle()
            print("Expanding this node...")
        expandedNodes = expand(currNode,algType)                           #store possible move operators
        if expandedNodes:
            if algType == 1:                                               #append all the possible moves for uniform cost search
                for node in expandedNodes:                          
                    puzzleQueue.append(node)                               
            else:                                                          #for A* algorithm, only append the best heuristic cost
                expandedNodes = sorted(expandedNodes, key=lambda puzzle: (puzzle.depth +  (puzzle.cost + puzzle.heuristic), puzzle.depth)) #sored again, https://docs.python.org/3/howto/sorting.html 
                for node in expandedNodes:                          
                    puzzleQueue.append(node) 
            expandedNodesVal += 1                                          #increment expanded number of nodes
        if len(puzzleQueue) > maxQueueSize:                                #update max queue size
            maxQueueSize = len(puzzleQueue)                     
        

#TEST STATES
depth0 = [[1,2,3],[4,5,6],[7,8,0]] 
depth2 = [[1,2,3],[4,5,6],[0,7,8]] 
depth4 = [[1,2,3],[5,0,6],[4,7,8]] 
depth8 = [[1,3,6],[5,0,2],[4,7,8]] 
depth12 = [[1,3,6],[5,0,7],[4,8,2]] 
depth16 = [[1,6,7],[5,0,3],[4,8,2]] 
depth20 = [[7,1,2],[4,8,5],[6,3,0]] 
depth24 = [[0,7,2],[4,6,1],[3,5,8]] 
slidesExample = [[1,2,0],[4,5,3],[7,8,6]]

def main():
    userInput = input("Welcome to Terry's 8 puzzle Solver. Type '1' to use a default puzzle, or '2' to create your own: ")
    puzzle = []
    alg = 0
    if userInput == "1":                                                 #call a default puzzle
        puzzle = depth20
    if userInput == "2":                                                 #user manually inputs 
        print("Enter your puzzle, using '0' to represent the blank. Be sure to space out each value and enter a new line when done with each row.")
        row1Input = input("Enter Row 1: ")                               #take each row as a string
        row2Input = input("Enter Row 2: ")
        row3Input = input("Enter Row 3: ")

        row1 = row1Input.split(" ")                                      #split each string into a list of strings, referred to https://www.w3schools.com/python/ref_string_split.asp
        row2 = row2Input.split(" ")
        row3 = row3Input.split(" ")

        puzzle = [row1,row2,row3]                                        #store as 2d list of strings

        for i in range(len(puzzle)):
            for j in range(len(puzzle[i])):
                puzzle[i][j] = int(puzzle[i][j])                         #convert string 2d list into int
    chooseAlg = input("Select an Algorithm.\n(1) for Uniform Cost Search\n(2) for the Misplaced Tile Heuristic\n(3) for the Manhattan Distance Heuristic\n")#determine queueing func
    if chooseAlg == "1":                                                 #uniform cost search
        alg = 1                                                          
    if chooseAlg == "2":                                                 #misplaced tile                    
        alg = 2
    if chooseAlg == "3":                                                 #manhattan distance
        alg = 3
    generalSearch(puzzle,alg)
main()
