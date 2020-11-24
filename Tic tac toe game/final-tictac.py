# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 17:21:16 2020

@author: kai

this code makes a functioning tic tac toe game against a computer!

note: Dr. Z said there was a problem with the checkWin file, so just make sure you use their correct version,
whoever is grading this
"""

import turtle, random, time, checkWin

turtle.tracer(0)
turtle.colormode(255)

#========== GAME MANAGER CLASS ==============================================================

class gameManager:
    def __init__(self):
        
        self.running = False #game by default is not running
        self.w=600
        self.h=600
        self.panel = turtle.Screen()
        
        self.Player = player() #player object
        self.BOARD = Board() #board object
        
        self.size = 3 #how many tiles across the board is
        
        self.numTurt = self.size*self.size #makes a board with size number of tiles across and size tiles down
        self.turtList = []
        
        for i in range(self.numTurt): #adds turtles to the list of turtles
           self.turtList.append(turtle.Turtle(shape="square")) #makes all the turtles square
           
        for i in range(len(self.turtList)): #hides all of the turtles in the list by default
            self.turtList[i].ht()

        self.playerType = True #by default sets the player's image to cherry
        
        self.turn = True #means that it is the player's turn by default

        turtle.setup(self.w,self.h) # start with calling setup to turn on listeners
        turtle.listen() # for keyboard listening
        
        self.boardW = self.w-self.w/(self.size+2) #makes the 3x3 board not take up the whole screen
        self.boardH = self.h-self.h/(self.size+2)
  
        self.splashPic = "splash.gif"  #splash screen
  
        self.position = [(-self.boardW/self.size,self.boardH/self.size),(0,self.boardH/self.size),(self.boardW/self.size,self.boardH/self.size),(-self.boardW/self.size,0),(0,0),(self.boardW/self.size,0),(-self.boardW/self.size,-self.boardH/self.size),(0,-self.boardH/self.size),(self.boardW/self.size,-self.boardH/self.size)]  
  
        self.panel.addshape(self.Player.orange) #adding shape code was learned about here: https://stackoverflow.com/questions/37106118/python-command-to-turn-turtle-into-image
        self.panel.addshape(self.Player.cherry) #means I can set the turtle's shape to the images  
        self.panel.addshape(self.splashPic)
        
        self.startSetup = 0 #when this is zero, it means the game has not been started yet / space key hasn't been pressed
        
        self.empty = " " #empty scoreboard list value
  
    def gameSetup(self):
        "sets up the game"
        self.running = True
        self.splashTurt.clearstamp(self.stampy)
        self.BOARD.drawBoard()
        self.Player.pSetup()
        self.turnTurtSetup()
        self.makeBoardList()
            
    def test(self):
        "makes it so that the key press is registered"
        self.startSetup = 1
        
    def splash(self):
        "splash screen setup"
        self.splashTurt = turtle.Turtle(shape=self.splashPic)
        self.splashTurt.goto(0,0)
        self.stampy = self.splashTurt.stamp()
        self.splashTurt.ht()
        
    def turnTurtSetup(self):
        "sets up the turn text turtle"
        self.turnTurtle = turtle.Turtle() #makes the turn turtle
        self.turnTurtle.ht()
        self.turnTurtle.up()
        self.turnTurtle.color(0,0,0)
        self.style = ("Courier", 20, "normal")
        self.turnTurtle.goto(0,260)
        self.turnTurtle.write("It is your turn", font = self.style, align = "center")
    
    def addPlay(self):
        "selects a location for the computer to play if it is the computer's turn"
        
        if self.running == True: #checks if there are still open tiles for the computer to play on
            
            if self.turn == False: #checks if it is the computer's turn

                self.listNum = (self.size*self.size) -1 
                self.Select = random.randint(0,self.listNum) #picks a random open location
                print(self.boardList[int(self.Select/self.size)][self.Select%self.size])
                
                if self.boardList[int(self.Select/self.size)][self.Select%self.size] == self.empty:
                    self.turtList[self.Select].shape(self.Player.compShape) #changes the turtle to the computer's image
                    self.boardList[int(self.Select/self.size)][self.Select%self.size]="O"
                    print(self.boardList)
                    time.sleep(.5) #waits before playing
                    self.turn = True #makes it the player's turn now
                    self.turnTurtle.clear()
                    self.turnTurtle.write("It is your turn", font = self.style, align = "center")
                    self.panel.update()
                    self.checkForWin()
                else: 
                    self.Select = random.randint(0,self.listNum)
                       
    def makeBoardList(self):
            '''Makes an empty scoreboard for tictactoe, based on the number of sides.
            The default 3x3 looks like this:
                [ [ [],[],[] ],
                  [ [],[],[] ],
                  [ [],[],[] ] ]
            Parameters-
            numside - (int) number of squares per side of the tic tac toe board
            empty - the indicator to use for an empty board. Try 0 or a string value.'''
            self.boardList = [] # empty list
            for i in range(self.size):
                #make rows
                self.boardRow=[]
                for k in range(self.size):
                    # make columns
                    self.boardRow.append(self.empty)
                self.boardList.append(self.boardRow)
            return self.boardList

    def checkForWin(self):
            WINNER = checkWin.checkWin(self.boardList)
            
            if type(WINNER) == str and WINNER != self.empty:
                gameOver = True
                game.running = False
           
            else:
                for row in self.boardList:
                    if self.empty in row:
                        gameOver = False
                        break
                    else:
                        gameOver = True
                        self.turnTurtle.clear()
                        self.turnTurtle.write("It's a tie!", font = self.style, align = "center")
                        print("it's a tie!")
                        break
            if gameOver:
                game.running = False
                print("game over!")
                if WINNER == "C":
                    self.turnTurtle.clear()
                    self.turnTurtle.write("You win :)", font = self.style, align = "center")
                elif WINNER == "O":
                    self.turnTurtle.clear()
                    self.turnTurtle.write("You lose :(", font = self.style, align = "center")

#========== PLAYER CLASS ==============================================================

class player:
    def __init__(self):
        
    # ========= PLAYER ATTRIBUTES =========
        
        self.orange = "orange.gif" #importing the two images that the player and computer use to play
        self.cherry = "cherry.gif" 

    # ========= PLAYER FUNCTIONS =========
    
    def whichClicked(self,x,y,buffer=70): #this code was edited from Dr. Z's Select Turtle code
        "function that returns which turtle is clicked"
        
        for i in range(len(game.turtList)): 
            tX = game.turtList[i].xcor() #gets the selected turtle's x coordinate
            tY = game.turtList[i].ycor() #gets the selected turtle's y coordinate
            if tX - buffer < x < tX + buffer and tY - buffer < y < tY + buffer:
                # see if click is within some range
                return i #when a click happens inside of a bubble area, return the index of the turtList
    
    def changeTurt(self,x,y):
        "Callback function for onclick to change the selected turtle to an x or o (cherry or orange)"

        self.selected = self.whichClicked(x,y) # use the output of the selected 
        self.whichType()
        
        if game.turn == True :
            game.turtList[self.selected].shape(self.Shape) #changes the turtle to the player's image
            game.panel.update()
            game.boardList[int(self.selected/game.size)][self.selected%game.size]="C"
            print(game.boardList)
            game.turn = False #makes it the computer's turn
            game.turnTurtle.clear()
            game.turnTurtle.write("It is the computer's turn", font = game.style, align = "center")
            game.panel.update()
            game.checkForWin()
        else :
            print("it's not your turn!")
        

    def whichType(self):
        "Function that sets the player and computer's images to either cherry or orange"
        if game.playerType == True:
            self.Shape = self.cherry #whatever you choose, the computer will be set to the other
            self.compShape = self.orange
        else:
            self.Shape = self.orange
            self.compShape = self.cherry         

    #========= TURTLE SETUP ==========

    def pSetup(self): 
        "sets up the list of turtles"
        for i in range(len(game.turtList)):
            game.turtList[i].st()
            game.turtList[i].shapesize(7)
            game.turtList[i].color("white") 
            game.turtList[i].up()
            game.turtList[i].goto(game.position[i]) #makes the turtles go to their set positions in the list
            game.turtList[i].onclick(self.changeTurt)

#========== BOARD CLASS ====================================================================

class Board:
    def __init__(self):
    # ========= PLAYER ATTRIBUTES =========
    
        self.boardTurt = turtle.Turtle()
        self.border = 50 #adds a nice border around the turtles
    
    # ========= BOARD FUNCTIONS =========
    
    def drawBoard(self):
        "draws the board"
        game.panel.bgcolor(217, 186, 145)
        self.bSetup()
        self.boardTurt.begin_fill()
        for k in range(4):
            self.boardTurt.fd(game.w-self.border*2)
            self.boardTurt.right(90)
        self.boardTurt.end_fill()
        self.boardTurt.ht()
 
    #========= TURTLE SETUP ==========
    
    def bSetup(self):
        "sets up the board turtle"
        self.boardTurt.color(179, 147, 107)
        self.boardTurt.up()
        self.boardTurt.goto(game.w/2-self.border,game.h/2-self.border)
        self.boardTurt.seth(270)


# =========ANIMATIONS BELOW==============================================================

game = gameManager() #creates the game manager
game.splash() #makes the splash screen

startup = True #I know in theory this whole chunk should be in the game manager class but for the life of me I couldn't get it to function without crashing

while startup:
    game.panel.onkey(game.test, "space") #this code is a workaround to get my splash screen to work. just calling the setup function inside the onkey() function would break it!! not fun!!
    game.panel.update()
    if game.startSetup == 1: #this means the space key has been pressed
        game.gameSetup()
        startup = False 

while game.running:
    
    game.addPlay() #decides the computer's play if it's the computer's turn
    game.panel.update()

# =========LISTENERS & CLEANUP =========
game.panel.mainloop() # keep listeners listening DO NOT DELETE
turtle.done() # cleanup whenever we exit the loop DO NOT DELETE.