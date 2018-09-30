from collections import deque
from myMazeLib import Classes, MiscFuncs

#Our BFS Function
def BFS(something, iMaze, start):
    #need our queue for this to work properly
    queue = deque([])

    #Got to start from the beginning
    currentLocation = start

    #These variables are used later in the code and is good to have them be filled with something
    #to help identify what they are
    nextLocation = None
    beenThere = None
    up = ""
    down = ""
    left = ""
    right = ""

    #sicne we already have the starting point, we add it to the list
    something.addNode(currentLocation, iMaze[currentLocation])
    #and then add to the queue
    queue.append(currentLocation)

    #We are going to loop until the queue is empty or we find the exit
    while queue:

        #Start off by finding out what our surrondings are
        up = MiscFuncs.checkUp(iMaze, currentLocation)
        down = MiscFuncs.checkDown(iMaze, currentLocation)
        left = MiscFuncs.checkLeft(iMaze, currentLocation)
        right = MiscFuncs.checkRight(iMaze, currentLocation)

        #this resets the variables for each iteration
        beenThere = False
        nodeExist = False

        #the following 4 if statements check each possible direction we can go
        #at each if, we check if the value is a P or X, since those are the only valid locations to move to

        #check up
        if up is "P" or up is "X":
            #We use the nextLocation variable to evalute postion up from out current location
            nextLocation = currentLocation - 10

            #we store the result from the findAndCheck function for a check we do later
            beenThere = something.findAndCheck(nextLocation)

            #same thing as the above line of code, but we are checking a node itself, rather than
            #a value within the node
            nodeExist = something.doesNodeExist(nextLocation)

            #check if we have already been to that location and that the next location is not a wall
            if beenThere is False and iMaze[nextLocation] is not "W":
                # also check that the node doesn't already exist
                if nodeExist is not True:
                    #when the node does not exist, we add it to the list
                    something.addNode(nextLocation, iMaze[nextLocation])
                #since we haven't been to the next spot and it isn't a wall, we queue the next location
                queue.append(nextLocation)

            #we check in between directions if the currentlocation is X, meaning we found the exit
            if iMaze[nextLocation] == "X":
                #so we break out the loop
                break


        #The remaining direction checks follow the same logic and code, so i won't be putting comments on those
        #The only real differences is how we get to each location. ie, to go up we subtract 10 from the current location
        #and to go down we add 10 to the current location. for left and right it is either -1 or +1, respectively 
        

        #check right
        if right is "P" or right is "X":
            nextLocation = currentLocation + 1
            beenThere = something.findAndCheck(nextLocation)
            nodeExist = something.doesNodeExist(nextLocation)

            if beenThere is False and iMaze[nextLocation] is not "W":
                if nodeExist is not True:
                    something.addNode(nextLocation, iMaze[nextLocation])
                queue.append(nextLocation)
                    
            #we check in between directions if the currentlocation is X, meaning we found the exit
            if iMaze[nextLocation] == "X":
                #so we break out the loop
                break

        #check down
        if down is "P" or down is "X":
            nextLocation = currentLocation + 10
            beenThere = something.findAndCheck(nextLocation)
            nodeExist = something.doesNodeExist(nextLocation)


            if beenThere is False and iMaze[nextLocation] is not "W":
                if nodeExist is not True:
                    something.addNode(nextLocation, iMaze[nextLocation])
                queue.append(nextLocation)
        
            #we check in between directions if the currentlocation is X, meaning we found the exit
            if iMaze[nextLocation] == "X":
                #so we break out the loop
                break

        #check left    
        if left is "P" or left is "X":
            nextLocation = currentLocation - 1
            beenThere = something.findAndCheck(nextLocation)
            nodeExist = something.doesNodeExist(nextLocation)

            if beenThere is False and iMaze[nextLocation] is not "W":
                if nodeExist is not True:
                    something.addNode(nextLocation, iMaze[nextLocation])
                queue.append(nextLocation)
        
            #and we check again at the end of the iteration if the currentlocation is X, meaning we found the exit
            if iMaze[nextLocation] == "X":
                #so we break out the loop
                break

        #change the value of the current location's "visited" variable to true, so we don't repeat that step    
        something.findAndSet(currentLocation)
        
        #remove the left most item in our list, which is acting like a queue thanks to the import deque
        queue.popleft()

        #and set the new current location euqal the the new, left-most item in our queue
        currentLocation = queue[0]