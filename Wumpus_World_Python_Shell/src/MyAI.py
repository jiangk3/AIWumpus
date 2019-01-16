# ======================================================================
# FILE:        MyAI.py
#
# AUTHOR:      Abdullah Younis
#
# DESCRIPTION: This file contains your agent class, which you will
#              implement. You are responsible for implementing the
#              'getAction' function and any helper methods you feel you
#              need.
#
# NOTES:       - If you are having trouble understanding how the shell
#                works, look at the other parts of the code, as well as
#                the documentation.
#
#              - You are only allowed to make changes to this portion of
#                the code. Any changes to other portions of the code will
#                be lost when the tournament runs your code.
# ======================================================================

from Agent import Agent
#import queue 
import random
 

class MyAI ( Agent ):

    def __init__ ( self):
        # ======================================================================
        # YOUR CODE BEGINS
        # ======================================================================
        self.map = [[[] for i in range(8)]for j in range(8)]
        self.goHome = False
        self.c = 0
        self.r = 6
        self.position = [self.r, self.c]
        self.direction = 1 #right
        self.rWall = 6
        self.uWall = 0
        self.start = [6,0]
        self.moves = [0,3,2,1]
        self.action = []
        self.count = 1
        self.go = True
        # ======================================================================
        # YOUR CODE ENDS
        # ======================================================================

#up = 0
#right = 1
#down = 2
#left = 3

    def getAction( self, stench, breeze, glitter, bump, scream ):
        # ======================================================================
        # YOUR CODE BEGINS
        # ======================================================================
        if ((breeze or stench) and self.position == self.start):
            return Agent.Action.CLIMB

        #while(self.goHome == False):
        while(self.go == True):
            #for i in self.map:
            #    print(i)
            #print('count:', self.count)
            #print('count:', self.count)
            self.position = [self.r, self.c]
#====================GLITTER===================================
            if (glitter):
                self.action.append('l')
                self.action.append('l')
                self.action.append('f')
                self.goHome = True #def goHome
                return Agent.Action.GRAB
#=====================ACTION====================================
            elif(self.action != []):
                #do those moves
                if(self.action[0] == 'l'):
                    self.action.pop(0)
                    #turn left
                    if(self.direction == 0):
                        self.direction = 3
                    else:
                        self.direction = self.direction - 1
                    return Agent.Action.TURN_LEFT
                elif(self.action[0] == 'r'):
                    self.action.pop(0)
                    #turn right
                    if(self.direction == 3):
                        self.direction = 0
                    else:
                        self.direction = self.direction + 1
                    return Agent.Action.TURN_RIGHT
                elif(self.action[0] == 'f'):
                    self.action.pop(0)
                    #update position on map
                    self.updatePosition() 
                    self.count += 1
                    return Agent.Action.FORWARD
#=====================GO HOME============================================
            elif(self.goHome == True):
                return self.takeMove(self.map[self.r][self.c].pop(-2),1)
#=======================BREEZE OR STENCH==================================
            elif (breeze or stench):
                #GO BACK, by turnning left
                if(self.direction == 0):
                    self.direction = 3
                else:
                    self.direction -= 1
                self.action.append('l')
                self.action.append('f')
                #update map
                self.map[self.r][self.c] = 'X'
                return Agent.Action.TURN_LEFT
#========================BUMP=================================
            elif(bump):
                if (self.direction == 1): #right
                    self.map[self.r][self.c] = 'X'
                    self.c -= 1
                    self.rWall = self.c
                    return self.takeMove(self.map[self.r][self.c].pop(0), len(self.map[self.r][self.c]))
                    #get next move
                    #update position
                    #update direction
                elif(self.direction == 0): #up
                    self.r += 1
                    self.uWall = self.r
                    return self.takeMove(self.map[self.r][self.c].pop(0), len(self.map[self.r][self.c]))
                    #get next move
                    #update position
                    #update direction
#==========================INSERT MOVES=============================================================
            elif(self.map[self.r][self.c] == []):# moves have not been assigned to that square
                if(self.position == self.start):#left bottom corner
                    self.map[self.r][self.c] = [1,0,'c', 'E'] #right, up, climb
                    #take move
                    #print(self.map[self.r][self.c])
                    return self.takeMove(self.map[self.r][self.c].pop(0), len(self.map[self.r][self.c]))
                elif (self.r == 6):# last row, cannot go down(2)
                    moves = []
                    moves.append(self.direction)
                    if(self.direction >= 2):
                        moves.append(self.direction - 2)
                    else:
                        moves.append(self.direction + 2)
                    for i in self.moves:
                        if (i not in moves):
                            moves.insert(1,i)
                    moves.remove(2)
                    moves.append('E')
                    self.map[self.r][self.c] = moves
                    #take move
                    #print(self.map[self.r][self.c])
                    return self.takeMove(self.map[self.r][self.c].pop(0), len(self.map[self.r][self.c]))
                elif (self.c == self.rWall):# right wall, cannot go right(1)
                    moves = []
                    moves.append(self.direction)
                    if(self.direction >= 2):
                        moves.append(self.direction - 2)
                    else:
                        moves.append(self.direction + 2)
                    for i in self.moves:
                        if (i not in moves):
                            moves.insert(1,i)
                    moves.remove(1)
                    moves.append('E')
                    self.map[self.r][self.c] = moves
                    #take move
                    #print(self.map[self.r][self.c])
                    return self.takeMove(self.map[self.r][self.c].pop(0), len(self.map[self.r][self.c]))
                elif (self.c == 0):# left wall, cannot go left(3)
                    moves = []
                    moves.append(self.direction)
                    if(self.direction >= 2):
                        moves.append(self.direction - 2)
                    else:
                        moves.append(self.direction + 2)
                    for i in self.moves:
                        if (i not in moves):
                            moves.insert(1,i)
                    moves.remove(3)
                    moves.append('E')               
                    self.map[self.r][self.c] = moves
                    #take move
                    #print(self.map[self.r][self.c])
                    return self.takeMove(self.map[self.r][self.c].pop(0), len(self.map[self.r][self.c]))
                elif (self.r == self.uWall):# upper wall, cannot go up(0)
                    moves = []
                    moves.append(self.direction)
                    if(self.direction >= 2):
                        moves.append(self.direction - 2)
                    else:
                        moves.append(self.direction + 2)
                    for i in self.moves:
                        if (i not in moves):
                            moves.insert(1,i)
                    moves.remove(0)
                    moves.append('E')
                    self.map[self.r][self.c] = moves
                    #take move
                   # print(self.map[self.r][self.c])
                    return self.takeMove(self.map[self.r][self.c].pop(0), len(self.map[self.r][self.c]))
                else:
                    moves = []
                    moves.append(self.direction)
                    if(self.direction >= 2):
                        moves.append(self.direction - 2)
                    else:
                        moves.append(self.direction + 2)
                    for i in self.moves:
                        if (i not in moves):
                            moves.insert(1,i)
                    moves.append('E')
                    
                    self.map[self.r][self.c] = moves
                    #take move
                    #print(self.map[self.r][self.c])
                    return self.takeMove(self.map[self.r][self.c].pop(0), len(self.map[self.r][self.c]))
#=====================================TAKE MOVE==============================================
            else:#take next move from current position
                #print(self.map[self.r][self.c])
                return self.takeMove(self.map[self.r][self.c].pop(0), len(self.map[self.r][self.c]))
        # ======================================================================
        # YOUR CODE ENDS
        # ======================================================================
    
    # ======================================================================
    # YOUR CODE BEGINS
    # ======================================================================
    def updatePosition(self):
        if(self.direction == 0):
            self.r -= 1
            self.position = [self.r, self.c]
        elif(self.direction == 1):
            self.c += 1
            self.position = [self.r, self.c]
        elif(self.direction == 2):
            self.r += 1
            self.position = [self.r, self.c]
        elif(self.direction == 3):
            self.c -= 1
            self.position = [self.r, self.c]
    
    def takeMove(self,move,length):
        if(move == 'c'):
            return Agent.Action.CLIMB
        else:
            while(self.check(move) == 0 and length > 1):
                move = self.map[self.r][self.c].pop(0)
                length -= 1
            #print('move:', move)
            if(move == 'c'):
                return Agent.Action.CLIMB
#------------------------up------------------------------------------
            elif(move == 0):
                if(move == self.direction):
                    self.r -= 1
                    self.position = [self.r, self.c]
                    self.count += 1
                    return Agent.Action.FORWARD
                elif(self.direction == 1):
                    self.action.append('f')
                    #update direction
                    self.direction -= 1
                    return Agent.Action.TURN_LEFT
                elif(self.direction == 2):
                    self.action.append('l')
                    self.action.append('f')
                     #update direction
                    self.direction -= 1
                    return Agent.Action.TURN_LEFT
                elif(self.direction == 3):
                    self.action.append('f')
                     #update direction
                    self.direction = 0
                    return Agent.Action.TURN_RIGHT
#------------------------right------------------------------------------
            elif(move == 1):
                if(move == self.direction):
                    self.c += 1
                    self.position = [self.r, self.c]
                    self.count += 1
                    return Agent.Action.FORWARD
                elif(self.direction == 0):
                    self.action.append('f')
                    #update direction
                    self.direction += 1
                    return Agent.Action.TURN_RIGHT
                elif(self.direction == 2):
                    self.action.append('f')
                    #update direction
                    self.direction -= 1
                    return Agent.Action.TURN_LEFT
                elif(self.direction == 3):
                    self.action.append('r')
                    self.action.append('f')
                    #update direction
                    self.direction = 0
                    return Agent.Action.TURN_RIGHT
#------------------------down------------------------------------------
            elif(move == 2):
                if(move == self.direction):
                    self.r += 1
                    self.position = [self.r, self.c]
                    self.count += 1
                    return Agent.Action.FORWARD
                elif(self.direction == 0):
                    self.action.append('r')
                    self.action.append('f')
                    #update direction
                    self.direction += 1
                    return Agent.Action.TURN_RIGHT
                elif(self.direction == 1):
                    self.action.append('f')
                    #update direction
                    self.direction += 1
                    return Agent.Action.TURN_RIGHT
                elif(self.direction == 3):
                    self.action.append('f')
                    #update direction
                    self.direction -= 1
                    return Agent.Action.TURN_LEFT
#------------------------Left-----------------------------------------------
            elif(move == 3):
                if(move == self.direction):
                    self.c -= 1
                    self.position = [self.r, self.c]
                    self.count += 1
                    return Agent.Action.FORWARD
                elif(self.direction == 0):
                    self.action.append('f')
                    #update direction
                    self.direction = 3
                    return Agent.Action.TURN_LEFT
                elif(self.direction == 1):
                    self.action.append('r')
                    self.action.append('f')
                    #update direction
                    self.direction += 1
                    return Agent.Action.TURN_RIGHT
                elif(self.direction == 2):
                    self.action.append('f')
                    #update direction
                    self.direction += 1
                    return Agent.Action.TURN_RIGHT
                

    def check(self,move):
        if(move == 0):
            if(self.map[self.r - 1][self.c] == 'X' or 'E' in self.map[self.r - 1][self.c]):
                return 0
            else:
                return 1
        elif(move == 1):
            if(self.map[self.r][self.c + 1] == 'X' or 'E' in self.map[self.r][self.c + 1]):
                return 0
            else:
                return 1
        elif(move == 2):
            if(self.map[self.r + 1][self.c] == 'X'or 'E' in self.map[self.r + 1][self.c]):
                return 0
            else:
                return 1
        elif(move == 3):
            if(self.map[self.r][self.c - 1] == 'X' or 'E' in self.map[self.r][self.c - 1]):
                return 0
            else:
                return 1
    # ======================================================================
    # YOUR CODE ENDS
    # ======================================================================