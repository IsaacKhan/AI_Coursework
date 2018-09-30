#Function to print the maze nicely (10x10)
def printMaze(iMaze):
    #i is the counter for how many columns are in the maze
    i = 0
    #for-loop based on the size of the maze length
    for i in range(len(iMaze)):
        #Since this is a 10x10 maze, we want to start a new line on the 10th read
        if i % 10 == 0:
            print("")
            print(iMaze[i], end = "  ")
        #Otherwise we would print normally, making sure we give some elbow room
        else:
            print(iMaze[i], end = "  ")
        #and of course, don't forget to increment the counter
        i += 1
    print("")

#function to find the enterance, assuming it will always be on the left side of the maze
def findAndSetEnterance(iMaze):
    #including some print()'s for fun
    print("\nLet's look for that entrance...")

    #the counter is for formatting the maze ina 10x10 layout
    i = 0

    #we follow this loop logic because for a 10x10 maze storing in a list (like i'm doing)
    #the left side is values 00 - 90, so we can just multiply each iteration of i by 10
    #Again, this is under the assumption that the enterance will always be on the left side
    #This assumption is made because of the wording in our handout(s) for this project
    while i < 10:

        #check if the location value is E
        if iMaze[i*10] == "E":

            #another print for fun
            print("Found it!")

            #and return that value to be stored as the starting point
            return i*10

        #if it isn't the right value, we keep looking
        i += 1

    #and if the value E isn't found, then there is no enterance on the left side of the maze
    print("I must be blind, because I can't findAndSet one!")
    #so we return 0
    return 0

#function that checks the value of the location up one space from our current location
def checkUp(iMaze, Location):
    if Location - 10 in range(0, len(iMaze)):
        return iMaze[Location - 10]

#function that checks the value of the location down one space from our current location
def checkDown(iMaze, Location):
    if Location + 10 in range(0, len(iMaze)):
        return iMaze[Location + 10]

#function that checks the value of the location left one space from our current location
def checkLeft(iMaze, Location):
    if Location - 1 in range(0, len(iMaze)):
        return iMaze[Location - 1] 

#function that checks the value of the location right one space from our current location
def checkRight(iMaze, Location):
    if Location + 1 in range(0, len(iMaze)):
        return iMaze[Location + 1]