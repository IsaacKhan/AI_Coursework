#This allows me to use a List as a queue; adds the .popleft() function to lists
from collections import deque

class Node:
    #this is the constructor for the class Node
    #as you can see, it has default values if none are provided
    def __init__(self, location = 0, value = ""):
        self.location = location
        self.value = value
        self.pathTraveled = []
        self.visited = False
        self.nextNode = None
    
class SomeThing:
    #This class is basically a linked list, but at the time of creation
    #I wasn't sure if this was what I needed for the project
    
    #This is the constructor for the class SomeThing
    def __init__(self, root = None, size = 0):
        self.root = root
        self.size = 0
    
    #This member function will add nodes to our list
    def addNode(self, Location, Value, pT = None):

        #check if there is a root node
        if self.root == None:

            #If there is, we create a new node with the given data
            newNode = Node(Location, Value)

            #Add to the nodes path traveled
            newNode.pathTraveled.append(Location)

            #set the Root to be this new node and increase the size 
            self.root = newNode
            self.size += 1

        #In this case, there are one or more nodes in our list
        else:

            #So we create a traversal node, and set it to the root
            currentNode = self.root

            #This temp variable is a list and is used for storing
            #every nodes path traveled. This is done so that the last node
            #has the same data as each previous node.
            temp = []
            
            #before we start to traverse this list, we check if the given location
            #has already been visited. This keeps repeats in our path traveled.
            if self.findAndCheck(Location) is not True:

                #Loop through the list until we get to the last node
                while currentNode.nextNode is not None:

                    #At each iteration, we add the location value of that node to our temp variable
                    temp.append(currentNode.location)

                    #move our traversal node to the next node
                    currentNode = currentNode.nextNode
            if Location == 4:
                print()
                
            #This makes sure we capture the last node's location value in our temp variable
            temp.append(currentNode.location)

            #Here we create our node with the provided data
            newNode = Node(Location, Value)

            #copy our temp variable into the newNode's pathTraveled
            newNode.pathTraveled = temp

            #and add the new, provided data to the pathTraveled
            newNode.pathTraveled.append(Location)

            #Since our traversal node is set to the last node we can use it to put our newNode at the end
            currentNode.nextNode = newNode

            #and increase the size of our list
            self.size += 1

    #This member function checks if a certain node already exists
    def doesNodeExist(self, CL):
        #Traversal node set to root/starting point
        currentNode = self.root

        #iterating through the list until we reach the end
        while currentNode.nextNode is not None:
            
            #at each iteration, we checks if the node we are at is the node we are looking for
            if currentNode.location is CL:
                return True
            #if it is not, keep moving
            else:
                currentNode = currentNode.nextNode

        #This if-else makes sure the last node is checks
        if currentNode.location is CL:
            return True
        else:
            return False

    #This memeber function will find the given node and set it to visited
    def findAndSet(self, CL):
        #traversal node
        currentNode = self.root

        #loop through list
        while currentNode.nextNode is not None:

            #at each iteration, see if matched provided data
            if currentNode.location is CL:
                #set vistied to true and break out
                currentNode.visited = True
                break
            else:
                #otherwise keep moving
                currentNode = currentNode.nextNode
    
    #This member fucntion will find the given node and see if it has been visited
    def findAndCheck(self, CL):
        #traversal node
        currentNode = self.root

        #iterate till end
        while currentNode.nextNode is not None:

            #returns true if locaion matches and it has been visited
            if currentNode.location is CL and currentNode.visited is True:
                return True
            #returns false if location matches and it hasn't been visited
            elif currentNode.location is CL and currentNode.visited is False:
                return False
            else:
                #otherwise, keep truckin'
                currentNode = currentNode.nextNode

        #at this point we know the node hasn't been visited AND doesn't exist
        return False

    #Print function for my thing(s)
    #Instead of printing the whole list, i'm just printing the last node
    #Since it will have the pathTraveled data of all previous nodes
    def printThing(self):
        #start at the root
        currentNode = self.root

        #go all the way to the end
        while currentNode.nextNode is not None:
            currentNode = currentNode.nextNode

        #and then print that node's data
        print("Step ", self.size)
        print("-------------------------------------")
        print("Location:", currentNode.location)
        print("Value:", currentNode.value)
        print("Path Traveled:", currentNode.pathTraveled)
        print("-------------------------------------")