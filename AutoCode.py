# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       liza2                                                        #
# 	Created:      2/18/2024, 8:10:08 PM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()

brain.screen.print("Hello V5")

#Plan:
#1.Moves arm up to see fruit
#2. Detect fruit, get distance
#3 line follow to the fruit (with some distance between)
#4 bring arm down to height underneath fruit
#5 turn to pick fruit
#6 Adjust height of arm to pick fruit
#7 Pick fruit
#8 Back up
#9 Turn out to center line
#10 Deposit fruit into back basket
#11 Turn back to prev position
#12 Turn to see next fruit
#13 Repeat steps #6 throgh #12 until 6 fruits are picked (Or capacity is calculated to max)
#14 drive streight until line
#15 turn 90 degrees on to the line
#16 drive until wall is seen
#17 back up specifific distance
#18 turn to find basket, recored distance
#18 drive streight, then move sideways until it sees correct basket
#19 rotate 180 degrees
#20 back up to deposit fruit
#21 turn around and drive
#22 restart, ignore previous fruit color 

#SATES
IDLE = 0
ROWSEARCH = 1
SEARCHFRUIT = 2
PICKFRUIT = 3
RETURNING = 4
DEPOSIT = 5

global FruitCount
global currentState
global maxFruit
global currentColor
pastColors = []

#Finds distance from fruit and returns forward and sideways distance
#Note, find out how far from fruit to stop
def triangulate():
    #TODO
    return (forwardDist,leftDist)

#Driving up to bin, bakcing up and dumping
def goToBin():
    #TODO
    return
#Event to check if the robot just found line
def foundLine():
    return lineFound

#Aproach first fruit in row
def startRow():
    #TODO
    return
#Aproach rest of fruit in row
def aproachFruit():
    #TODO
    return
#Lift arm to fruit, pick it, baack up, deposit to bin
def pickFruit():
    #TODO
    return
#Follow line
def lineFollowing():
    #TODO
    return



        
