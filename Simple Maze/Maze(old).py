#Program Title:     Simple Maze w/Agent
#Programmer:        Isaac Khan
#Course:            CSC 412 - Aritifical Intelligence
#Description:       Create a program with an Agent that will traverse a 10 by 10 maze
#                   The maze will be read in from a file, and the Agent will follow
#                   the BFS and DFS Algorithms when solving this Simple Maze Program.



#This allows me to use a List as a queue; adds the .popleft() function to lists
from collections import deque



#---------------------------------------------------------#
#                        Classes                          #
#---------------------------------------------------------#



class Node:
    def __init__(self, location = 0, value = ""):
        self.location = location
        self.value = value
        self.pathTraveled = []
        self.visited = False
        self.nextNode = None
    
class SomeThing:
    def __init__(self, root = None, size = 0):
        self.root = root
        self.size = 0
    
    def addNode(self, Location, Value, pT = None):
        if self.root == None:
            newNode = Node(Location, Value)
            newNode.pathTraveled.append(Location)

            self.root = newNode
            self.size += 1
        else:
            currentNode = self.root
            temp = []

            while currentNode.nextNode is not None:
                if self.check(Location) is not True:
                    temp.append(currentNode.location)
                    currentNode = currentNode.nextNode
                else:
                    currentNode = currentNode.nextNode

            temp.append(currentNode.location)

            newNode = Node(Location, Value)
            newNode.pathTraveled = temp
            newNode.pathTraveled.append(Location)

            currentNode.nextNode = newNode
            self.size += 1

    def find(self, CL):
        currentNode = self.root
        while currentNode.nextNode is not None:
            if currentNode.location is CL:
                currentNode.visited = True
                break
            else:
                currentNode = currentNode.nextNode

    def check(self, CL):
        currentNode = self.root
        i = 0
        if currentNode.location is CL and currentNode.visited is True:
            return True

        while currentNode.nextNode is not None:
            if currentNode.location is CL and currentNode.visited is True:
                return True
            else:
                i += 1
                currentNode = currentNode.nextNode

        return False

    def printThing(self):
        currentNode = self.root
        i = 0

        while currentNode is not None:
            currentNode = currentNode.nextNode
            i +=1
            if i == self.size - 2:
                print("Step ", self.size)
                print("-------------------------------------")
                print("Location:", currentNode.location)
                print("Value:", currentNode.value)
                print("Path Traveled:", currentNode.pathTraveled)
                print("-------------------------------------")




#---------------------------------------------------------#
#                       Functions                         #
#---------------------------------------------------------#



def printMaze(iMaze):
    #i is the counter for how many columns are in the maze
    i = 0
    #for-loop based on the size of the maze length
    for i in range(len(maze)):
        #Since this is a 10x10 maze, we want to start a new line on the 10th read
        if i % 10 == 0:
            print("")
            print(maze[i], end = "  ")
        #Otherwise we would print normally, making sure we give some elbow room
        else:
            print(maze[i], end = "  ")
        #and of course, don't forget to increment the counter
        i += 1
    print("")

def findEnterance(iMaze):
    print("\nLet's look for that entrance...")
    i = 0
    while i < 10:
        if iMaze[i*10] == "E":
            print("Found it!")
            return i*10
        i += 1
    print("I must be blind, because I can't find one!")
    return 0

def checkUp(iMaze, Location):
    if Location - 10 in range(0, len(iMaze)):
        return iMaze[Location - 10]

def checkDown(iMaze, Location):
    if Location + 10 in range(0, len(iMaze)):
        return iMaze[Location + 10]

def checkLeft(iMaze, Location):
    if Location - 1 in range(0, len(iMaze)):
        return iMaze[Location - 1] 

def checkRight(iMaze, Location):
    if Location + 1 in range(0, len(iMaze)):
        return iMaze[Location + 1]

def BFS(something, iMaze, start):
    queue = deque([])
    currentLocation = start
    nextLocation = None
    beenThere = None
    exitFound = False
    up = ""
    down = ""
    left = ""
    right = ""

    something.addNode(currentLocation, iMaze[currentLocation])
    queue.append(currentLocation)

    while queue:
        up = checkUp(iMaze, currentLocation)
        down = checkDown(iMaze, currentLocation)
        left = checkLeft(iMaze, currentLocation)
        right = checkRight(iMaze, currentLocation)

        beenThere = False

        if iMaze[currentLocation] == "X":
            exitFound = True
        if exitFound is not True:   
            if up is "P" or up is "X":
                nextLocation = currentLocation - 10
                beenThere = something.check(nextLocation)


                if beenThere is False and iMaze[nextLocation] is not "W":
                    something.addNode(nextLocation, iMaze[nextLocation])
                    queue.append(nextLocation)
        
            if right is "P" or right is "X":
                nextLocation = currentLocation + 1
                beenThere = something.check(nextLocation)

                if beenThere is False and iMaze[nextLocation] is not "W":
                    something.addNode(nextLocation, iMaze[nextLocation])
                    queue.append(nextLocation)
                
            if down is "P" or down is "X":
                nextLocation = currentLocation + 10
                beenThere = something.check(nextLocation)

                if beenThere is False and iMaze[nextLocation] is not "W":
                    something.addNode(nextLocation, iMaze[nextLocation])
                    queue.append(nextLocation)
                
            if left is "P" or left is "X":
                nextLocation = currentLocation - 1
                beenThere = something.check(nextLocation)

                if beenThere is False and iMaze[nextLocation] is not "W":
                    something.addNode(nextLocation, iMaze[nextLocation])
                    queue.append(nextLocation)
        else:
            break
        
        something.find(currentLocation)
        print("********************")
        print(queue)
        print("********************")
        queue.popleft()
        currentLocation = queue[0]
    
def DFS(something, iMaze, start):
    stack = []
    currentLocation = start
    nextLocation = None
    beenThere = None
    exitFound = False
    up = ""
    down = ""
    left = ""
    right = ""

    something.addNode(currentLocation, iMaze[currentLocation])
    stack.append(currentLocation)

    while stack:
        up = checkUp(iMaze, currentLocation)
        down = checkDown(iMaze, currentLocation)
        left = checkLeft(iMaze, currentLocation)
        right = checkRight(iMaze, currentLocation)

        beenThere = False

        if iMaze[currentLocation] == "X":
            exitFound = True
        if exitFound is not True:   
            if up is "P" or up is "X":
                nextLocation = currentLocation - 10
                beenThere = something.check(nextLocation)

                if beenThere is False and iMaze[nextLocation] is not "W":
                    something.addNode(nextLocation, iMaze[nextLocation])
                    stack.append(nextLocation)
        
            if right is "P" or right is "X":
                nextLocation = currentLocation + 1
                beenThere = something.check(nextLocation)

                if beenThere is False and iMaze[nextLocation] is not "W":
                    something.addNode(nextLocation, iMaze[nextLocation])
                    stack.append(nextLocation)
                
            if down is "P" or down is "X":
                nextLocation = currentLocation + 10
                beenThere = something.check(nextLocation)

                if beenThere is False and iMaze[nextLocation] is not "W":
                    something.addNode(nextLocation, iMaze[nextLocation])
                    stack.append(nextLocation)
                
            if left is "P" or left is "X":
                nextLocation = currentLocation - 1
                beenThere = something.check(nextLocation)

                if beenThere is False and iMaze[nextLocation] is not "W":
                    something.addNode(nextLocation, iMaze[nextLocation])
                    stack.append(nextLocation)
        else:
            break
        
        something.find(currentLocation)

        #stack.pop()
        currentLocation = stack.pop()

        

#---------------------------------------------------------#
#                     Driver Code                         #
#---------------------------------------------------------#



maze = []
start = None
thing = SomeThing()
anotherThing = SomeThing()

with open("maze.txt") as mazefile:
    #Opens a file and removes the whitespace or \n's from what is read in
    #Then stores it in our empty list
    maze = [x.strip() for x in mazefile.readlines()]
    printMaze(maze)

start = findEnterance(maze)
print("")
print("")
print("BFS")
BFS(thing, maze, start)
thing.printThing()

#anotherThing.addNode(start, maze[start])
#anotherThing.addNode(start + 1, maze[start + 1])
#anotherThing.addNode(start + 2, maze[start + 2])
#anotherThing.addNode(start + 3, maze[start + 3])
#anotherThing.addNode(start + 4, maze[start + 4])

print("")
print("")
print("DFS")
DFS(anotherThing, maze, start)
anotherThing.printThing()
