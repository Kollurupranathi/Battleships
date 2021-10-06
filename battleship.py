"""
Battleship Project
Name:
Roll No:
"""

from typing import ValuesView
import battleship_tests as test

project = "Battleship" # don't edit this

### SIMULATION FUNCTIONS ###

from tkinter import *
import random

EMPTY_UNCLICKED = 1
SHIP_UNCLICKED = 2
EMPTY_CLICKED = 3
SHIP_CLICKED = 4


'''
makeModel(data)
Parameters: dict mapping strs to values
Returns: None
'''
def makeModel(data):
    data["boardsize"]= 500
    data["rows"]=10
    data["cols"]=10
    data["cellsize"]= data["boardsize"]/data["rows"]
    data["numships"]=5
    data["usergrid"]= emptyGrid(data["rows"],data["cols"])  #test.testGrid()
    data["computergrid"]= addShips(emptyGrid(data["rows"],data["cols"]),data["numships"])
    data["tempship"]= []
    data["userships"]=0 #test.testShip()#createShip()

'''
makeView(data, userCanvas, compCanvas)
Parameters: dict mapping strs to values ; Tkinter canvas ; Tkinter canvas
Returns: None
'''
def makeView(data, userCanvas, compCanvas):
    usercanvas = drawGrid(data, userCanvas, data["usergrid"], True)
    compcanvas = drawGrid(data, compCanvas, data["computergrid"], True)
    emptyboard = drawShip(data, userCanvas, data["tempship"]) 
    return 


'''
keyPressed(data, events)
Parameters: dict mapping strs to values ; key event object
Returns: None
'''
def keyPressed(data, event):
    pass


'''
mousePressed(data, event, board)
Parameters: dict mapping strs to values ; mouse event object ; 2D list of ints
Returns: None
'''
def mousePressed(data, event, board):
    click =getClickedCell(data,event)
    if board == "user" :
     clickUserBoard(data, click[0], click[1])
    
    pass

#### WEEK 1 ####

'''
emptyGrid(rows, cols)
Parameters: int ; int
Returns: 2D list of ints
'''
def emptyGrid(rows, cols):
    grid = []
    for i in range(rows):
        s= []
        for j in range(cols):
            s.append(EMPTY_UNCLICKED)
        grid.append(s)
    return grid



'''
createShip()
Parameters: no parameters
Returns: 2D list of ints
'''
def createShip():
    row = random.randint(1,8)
    col =random.randint(1,8)
    center =random.randint(0,1)
    if center==0:
        ship =([[row-1,col],[row,col],[row+1,col]])
    else:
        ship =([[row,col-1],[row,col],[row,col+1]])
    return ship


'''
checkShip(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def checkShip(grid, ship):
     for i in ship:
        if grid[i[0]][i[1]]!=EMPTY_UNCLICKED:
            return False
     return True

   


'''
addShips(grid, numShips)
Parameters: 2D list of ints ; int
Returns: 2D list of ints
'''
def addShips(grid, numShips):
    count=0
    while count<numShips:
        newship = createShip()
        if checkShip(grid,newship):
          for j in newship:
                  grid[j[0]][j[1]]=SHIP_UNCLICKED
          count+=1
    return grid

 
'''
drawGrid(data, canvas, grid, showShips)
Parameters: dict mapping strs to values ; Tkinter canvas ; 2D list of ints ; bool
Returns: None
'''
def drawGrid(data, canvas, grid, showShips):
    for row in range(data["rows"]):
     for col in range(data["cols"]): 
      if grid[row][col]== SHIP_UNCLICKED:
        canvas.create_rectangle(data["cellsize"]*col, data["cellsize"]*row, data["cellsize"]*(col+1), data["cellsize"]*(row+1), fill="yellow")
      else:
        canvas.create_rectangle(data["cellsize"]*col, data["cellsize"]*row, data["cellsize"]*(col+1), data["cellsize"]*(row+1), fill= "blue")


### WEEK 2 ###

'''
isVertical(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isVertical(ship):
    temp =[]
    for i in range(len(ship)):
        temp.append(ship[i][0])
    temp.sort()
    if ship[0][1]==ship[1][1]==ship[2][1] and temp[0]==temp[1]-1==temp[2]-2:
        return True
    return False

  
'''
isHorizontal(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isHorizontal(ship):
  temp =[]
  for i in range(len(ship)):
        temp.append(ship[i][1])
  temp.sort()
  if ship[0][0]==ship[1][0]==ship[2][0] and temp[0]==temp[1]-1==temp[2]-2:
     return True
  return False
    


'''
getClickedCell(data, event)
Parameters: dict mapping strs to values ; mouse event object
Returns: list of ints
'''
def getClickedCell(data, event):
     x= int((event.y)/data['cellsize'])
     y= int((event.x)/data['cellsize'])
     return [x, y]
    


'''
drawShip(data, canvas, ship)
Parameters: dict mapping strs to values ; Tkinter canvas; 2D list of ints
Returns: None
'''
def drawShip(data, canvas, ship):
    for i in range(len(ship)):
     canvas.create_rectangle(data["cellsize"]*ship[i][1], data["cellsize"]*ship[i][0], data["cellsize"]*(ship[i][1]+1), data["cellsize"]*(ship[i][0]+1), fill= "white")
    return


'''
shipIsValid(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def shipIsValid(grid, ship):
    if checkShip(grid,ship):
      if isHorizontal(ship) or isVertical(ship):
        return True
    return False


'''
placeShip(data)
Parameters: dict mapping strs to values
Returns: None
'''
def placeShip(data):
    user_board = data["usergrid"]
    if shipIsValid(user_board,data["tempship"]):
        for i in data["tempship"]:
           user_board[i[0]][i[1]]= SHIP_UNCLICKED
        data["userships"]+=1
    else:
      print("Ship is not valid") 
    data["tempship"]=[] 
    return


'''
clickUserBoard(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def clickUserBoard(data, row, col):
    if data["userships"]==5:
       print("You can start the game")
       return
    if [row,col] == data["tempship"]:
       return 
    if [row,col] not in data["tempship"]:
      data["tempship"].append([row,col])
    if len(data["tempship"])==3:
        placeShip(data)   
    return


### WEEK 3 ###

'''
updateBoard(data, board, row, col, player)
Parameters: dict mapping strs to values ; 2D list of ints ; int ; int ; str
Returns: None
'''
def updateBoard(data, board, row, col, player):
    return


'''
runGameTurn(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def runGameTurn(data, row, col):
    return


'''
getComputerGuess(board)
Parameters: 2D list of ints
Returns: list of ints
'''
def getComputerGuess(board):
    return


'''
isGameOver(board)
Parameters: 2D list of ints
Returns: bool
'''
def isGameOver(board):
    return


'''
drawGameOver(data, canvas)
Parameters: dict mapping strs to values ; Tkinter canvas
Returns: None
'''
def drawGameOver(data, canvas):
    return


### SIMULATION FRAMEWORK ###

from tkinter import *

def updateView(data, userCanvas, compCanvas):
    userCanvas.delete(ALL)
    compCanvas.delete(ALL)
    makeView(data, userCanvas, compCanvas)
    userCanvas.update()
    compCanvas.update()

def keyEventHandler(data, userCanvas, compCanvas, event):
    keyPressed(data, event)
    updateView(data, userCanvas, compCanvas)

def mouseEventHandler(data, userCanvas, compCanvas, event, board):
    mousePressed(data, event, board)
    updateView(data, userCanvas, compCanvas)

def runSimulation(w, h):
    data = { }
    makeModel(data)

    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window

    # We need two canvases - one for the user, one for the computer
    Label(root, text = "USER BOARD - click cells to place ships on your board.").pack()
    userCanvas = Canvas(root, width=w, height=h)
    userCanvas.configure(bd=0, highlightthickness=0)
    userCanvas.pack()

    compWindow = Toplevel(root)
    compWindow.resizable(width=False, height=False) # prevents resizing window
    Label(compWindow, text = "COMPUTER BOARD - click to make guesses. The computer will guess on your board.").pack()
    compCanvas = Canvas(compWindow, width=w, height=h)
    compCanvas.configure(bd=0, highlightthickness=0)
    compCanvas.pack()

    makeView(data, userCanvas, compCanvas)

    root.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    compWindow.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    userCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "user"))
    compCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "comp"))

    updateView(data, userCanvas, compCanvas)

    root.mainloop()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":

    ## Finally, run the simulation to test it manually ##
    runSimulation(500, 500)
