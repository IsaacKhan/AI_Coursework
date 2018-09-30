#Program Title:     Simple Maze w/Agent
#Programmer:        Isaac Khan
#Course:            CSC 412 - Aritifical Intelligence
#Description:       Create a program with an Agent that will traverse a 10 by 10 maze
#                   The maze will be read in from a file, and the Agent will follow
#                   the BFS and DFS Algorithms when solving this Simple Maze Program.
#                   Also, I went back and added comments for you.



#This allows me to use a List as a queue; adds the .popleft() function to lists
from collections import deque
from myMazeLib import Classes, BFS, DFS, MiscFuncs

#creating a list to hold our maze
maze = []

#start is the location (number) of value E
start = None

#two objects for our BFS and DFS
thing = Classes.SomeThing()
anotherThing = Classes.SomeThing()

#open the text file and store data in our maze list
with open("maze.txt") as mazefile:
    #Opens a file and removes the whitespace or \n's from what is read in
    #Then stores it in our empty list
    maze = [x.strip() for x in mazefile.readlines()]
    MiscFuncs.printMaze(maze)

#find out start location
start = MiscFuncs.findAndSetEnterance(maze)

#start the BFS and print results
print("\n\nBFS")
BFS.BFS(thing, maze, start)
thing.printThing()

#start the DFS and print results
print("\n\nDFS")
DFS.DFS(anotherThing, maze, start)
anotherThing.printThing()