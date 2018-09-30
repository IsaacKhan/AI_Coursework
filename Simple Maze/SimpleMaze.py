#Program Title:     Simple Maze w/Agent
#Programmer:        Isaac Khan
#Course:            CSC 412 - Aritifical Intelligence
#Description:       Create a program with an Agent that will traverse a 10 by 10 maze
#                   The maze will be read in from a file, and the Agent will follow
#                   the BFS and DFS Algorithms when solving this Simple Maze Program.



#---------------------------------------------------------#
#                        Classes                          #
#---------------------------------------------------------#



#Creating a class for our nodes, and since i'm not being boring i will call them 'Pages'
#This is because they will be stored in a linked-list style DS called 'Notebook'
class Page:
    def __init__(self, currentLocation = 0, locationValue = None, pathTraveled = None):
        self.currentLocation = currentLocation
        self.locationValue = locationValue
        self.pathTraveled = pathTraveled
        self.visited = False
        self.nextPage = None

    #Get and Set for Next node
    def getNextPage(self):
        return self.nextPage
    def setNextPage(self, NP):
        self.nextPage = NP

    #Get and Set for remaining data in node/pages
    def getCurrentLocation(self):
        return self.currentLocation
    def setCurrentLocation(self, CL):
        self.currentLocation = CL
    def getLocationValue(self):
        return self.locationValue
    def setLocationValue(self, LV):
        self.locationValue = LV
    def getPathTraveled(self):
        return self.pathTraveled
    def setPathTraveled(self, PT):
        self.pathTraveled = PT

#Creating a 'Notebook' for our agent, this will be where the nodes or 'Pages' will be stored
#Currently thinking this class as a linked list style DS
class Notebook():
    def __init__(self, firstPage = None):
        self.firstPage = firstPage
        self.size = 0
        
    def getSize(self):
        return self.size

    def addPage(self, CL, LV):
        if self.firstPage == None:
            newPage = Page(CL, LV)
            newPage.setPathTraveled(CL)
            self.firstPage = newPage
            self.size += 1
        else:
            #Like a traversal pointer
            thisPage = self.firstPage
            newPage = Page(CL, LV)

            #temp variable for PT shorterm storage
            temp = ""

            if thisPage.nextPage == None:
                temp = str(thisPage.getPathTraveled()) + ", "
            else:
                #This should iterate through the pages/nodes until the last one
                while thisPage.getNextPage() != None:
                    temp = str(thisPage.getPathTraveled()) + ", "
                    thisPage = thisPage.getNextPage()
                temp = str(thisPage.getPathTraveled()) + ", "

            #add the current CL to our PT so it will show in the last page
            temp += str(CL) + ", "

            #Once at the last page, we create the new page and set the last
            #page to point to the new page
            newPage.setPathTraveled(temp)
            thisPage.nextPage = newPage
            self.size +=1

    def removePage(self, data):
        thisPage = self.firstPage
        lastPage = None

        while thisPage:
            if thisPage.getCurrentLocation == data:
                if lastPage:
                    lastPage.setNextPage(thisPage.getNextPage())
                else:
                    self.firstPage = thisPage
                self.size -= 1
                return True
            else:
                lastPage = thisPage
                thisPage = thisPage.getNextPage()
        return False

    def readNotebook(self):
        thisPage = self.firstPage
        i = 0
        while thisPage and i < self.size:
            print("Page ", i + 1)
            print("------------------------------")
            print("Current Location: ", thisPage.getCurrentLocation())
            print("Location Value: ", thisPage.getLocationValue())
            print("Path Traveled: ", thisPage.getPathTraveled())
            print("------------------------------")
            i += 1
            thisPage = thisPage.getNextPage()

    def readLastPage(self):
        thisPage = self.firstPage

        while thisPage.getNextPage() != None:
            thisPage = thisPage.getNextPage()
        
        print("This is the last Page: Page ", self.getSize())
        print("------------------------------")
        print("Current Location: ", thisPage.getCurrentLocation())
        print("Location Value: ", thisPage.getLocationValue())
        print("Path Traveled: ", thisPage.getPathTraveled())
        print("------------------------------")

    def find(self, data):
        thisPage = self.firstPage

        while thisPage:
            if thisPage.getCurrentLocation() == data:
                return data
            else:
                thisPage = thisPage.getNextPage()
            return None

#Creating a class for our agent. I think we need to do this? Not Sure.
class MyAgent:
    myNotebook = Notebook()

    def __init__(self, name = "No Name", position = 0, positionValue = "", 
                 pathTraveled = "No Path", up = "", down = "", left = "", right = "",
                 enteranceFound = False, exitFound = False):
        self.name = name
        self.position = position
        self.positionValue = positionValue
        self.up = up
        self.down = down
        self.left = left
        self.right = right

    #Movement Functions
    def moveUp(self, currentPosition):
        #To move up, subtract 10
        self.position -= 10
    def moveDown(self, currentPosition):
        #To move down, add 10
        self.position += 10
    def moveLeft(self, currentPosition):
        #To move left, subtract 1
        self.position -= 1
    def moveRight(self, currentPosition):
        #To move right, add 1
        self.position += 1

    #Functionality functions
    def findEnterance(self, iMaze):
        print("\nLet's look for that entrance...")
        i = 0
        while i < 10:
            if iMaze[i*10] == "E":
                self.position = i * 10
                self.positionValue = iMaze[self.position]
                self.enteranceFound = True
            i += 1
        if self.enteranceFound == True:
            print("Found it!")
        else:
            print("I must be blind, because I can't find one!")

    def checkSurroundings(self, iMaze):
        #Need to make sure what we check is within the range of our input Maze
        if self.position - 10 in range(0, len(iMaze)):
            self.up = iMaze[self.position - 10]
        if self.position + 10 in range(0, len(iMaze)):
            self.down = iMaze[self.position + 10]
        if self.position - 1 in range(0, len(iMaze)):
            self.left = iMaze[self.position - 1] 
        if self.position + 1 in range(0, len(iMaze)):
            self.right = iMaze[self.position + 1]
        
        #Set the Agents position value
        self.positionValue = iMaze[self.position]

    def BFS(self, iMaze):
        queue = []
        currentPage = myNotebook.firstPage

        myNotebook.addPage(self.position, self.positionValue)


        pass

    def DFS(self, iMaze):
        pass



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



#---------------------------------------------------------#
#                     Driver Code                         #
#---------------------------------------------------------#



# Variables&Objects #

maze = []
AgentNiko = MyAgent("Niko", 0)

# Code #

with open("maze.txt") as mazefile:
    #Opens a file and removes the whitespace or \n's from what is read in
    #Then stores it in our empty list
    maze = [x.strip() for x in mazefile.readlines()]
    printMaze(maze)

#Get our Agent to find the enterance to the maze
AgentNiko.findEnterance(maze)

#Now we check our surrondings so the agent can see it's options
AgentNiko.checkSurroundings(maze)

AgentNiko.BFS(maze)

#readNotebook is kind of a debugging function, but also adds a bit of personality to our Agent
#AgentNiko.readNotebook()

#print("")
#print("")
#print("")

#AgentNiko.myNotebook.addPage(AgentNiko.position, AgentNiko.positionValue)
#AgentNiko.myNotebook.readNotebook()

#print("")
#print("")
#print("")

#AgentNiko.moveRight(AgentNiko.position)
#AgentNiko.checkSurroundings(maze)
#AgentNiko.myNotebook.addPage(AgentNiko.position, AgentNiko.positionValue)
#AgentNiko.myNotebook.readNotebook()

#print("")
#print("")
#print("")

#AgentNiko.myNotebook.readLastPage()

#print("")
#print("")
#print("")

#AgentNiko.moveRight(AgentNiko.position)
#AgentNiko.checkSurroundings(maze)
#AgentNiko.myNotebook.addPage(AgentNiko.position, AgentNiko.positionValue)
#AgentNiko.myNotebook.readNotebook()