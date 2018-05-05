#author: Musaed, Kristy, Rodvin
#team: 07Nim
#description: The strategy game known as Nim. Players can take stones 
#Uses the rule that the player to take the last stone loses.

import turtle
import random
import time

wn = turtle.Screen()
wn.bgcolor("burlywood")

#Initial game state.
turncount = 0
playerlist = ["Player","Computer"]
player1 = "none"
player2 = "none"
setup = [4,[4,4,4,4]]
recordData = []
gameState = []
maxstones = max(setup[1])
NumofPiles = setup[0]

#Constants for the dimensions of the game board.
TOP = 40 * maxstones
BOTTOM = -40 * maxstones
LEFT = -83*NumofPiles
RIGHT = 83*NumofPiles
WIDTH = 100
BASE = BOTTOM + 20
SPACE = 80
CIRCLE_EDGE = LEFT + (WIDTH//4)
CIRCLE_RADIUS = 20
HEIGHT = (TOP-BOTTOM)

#Settings for the buttons.
backButt = LEFT - 200
forwButt = RIGHT + 100
buttonWidth = 100
buttonHeight = 50
forwColor = "grey"
backColor = "grey"

#Turtles involved in making the game board and player messages.
nim = turtle.Turtle() 
draw = turtle.Turtle()
stdraw = turtle.Turtle()
remove = turtle.Turtle()
status = turtle.Turtle()
button = turtle.Turtle()


#Hides turtles for screen setup and prints the welcome message in the terminal.
def intro():
	nim.hideturtle()
	draw.hideturtle()
	stdraw.hideturtle()
	remove.hideturtle()
	status.hideturtle()
	button.hideturtle()
	
 	#Welcome!
	print('''
|\     /(  ____ ( \     (  ____ (  ___  |       |  ____ ( )
| )   ( | (    \/ (     | (    \/ (   ) | () () | (    \/
| | _ | | (__   | |     | |     | |   | | || || | (__   | |
| |( )| |  __)  | |     | |     | |   | | |(_)| |  __)  | |
| || || | (     | |     | |     | |   | | |   | | (     (_)
| () () | (____/\ (____/\ (____/\ (___) | )   ( | (____/\_ 
(_______|_______(_______(_______(_______)/     \(_______(_''')

	#Rules of the game
	print('''
Game of Nim is a strategy game that consists of piles with different
numbers of stones. Each turn a player must remove one or more stones 
from a single pile. The player who removes the last stone loses.

To make your move, click on a stone to remove it and all stones above it.

Press S to save the game and L to load your saved game.''')

			
#Writes a welcome message on the screen that disappears after a short time, then displays the game title.
def welcome():   
	bob = turtle.Turtle()
	bob.hideturtle()
	bob.pen(pencolor = "red", pensize = 7, speed = 1)
	bob.penup()
	bob.goto(0,200)
	bob.write ("Welcome!" , align = "center", font=("Arial", 100, "normal"))
	
	status.write('''
Game of Nim is a strategy game that consists of piles with different
numbers of stones. Each turn a player must remove one or more stones 
from a single pile. The player who removes the last stone loses.

To make your move, click on a stone to remove it and all stones above it.

Press S to save the game and L to load your saved game.''', align = "center", font = ("Arial", 16, "normal"))
	time.sleep(5)
	bob.clear()

	nim.pen(pencolor = "red", pensize = 7, speed = 5)
	nim.penup()
	nim.goto(-300,TOP + 50)
	nim.write("Game of Nim" , font=("Arial", 80, "normal"))

	status.clear()
	status.penup()
	status.goto(0, BOTTOM - SPACE)
	
	gameStat()
	forward()
	backward()
	
	
#Creates a list that contains smaller lists each representing a pile.
#The number of the smaller lists depends on the number of piles.
#Then the function fills them with zeros according
#to the maximum number of stones.
def gameStat():
	for pile in range(NumofPiles):
		pileList = []
		for stone in range(maxstones):
			pileList.append(0)
		gameState.append(pileList)
	applystones()

	
#Replaces zeros in the variable gameState with ones, which represent stones in a pile,
#according to the number of stones in each pile.
def applystones():
	for pile in range(NumofPiles):
		stone = setup[1][pile]
		setStone(pile, stone)	

		
#Draws the boundaries of the piles that will hold the stones.
def gameBoard():
	draw.pen(pencolor = "blue", pensize = 10, speed = 10)
	draw.penup()
	draw.goto(LEFT,TOP)
	for i in range(NumofPiles):
		draw.pendown()
		for half in range(2):	
			draw.forward(WIDTH)
			draw.right(90)
			draw.forward(HEIGHT)
			draw.right(90)
		draw.penup()		
		draw.forward(2*WIDTH)

		
#Draws stones in the initial configuration.
def gamePiece():
	stdraw.pen(pencolor = "red", speed = 0, pensize = 5)
	stdraw.penup()
	position = 0
	for i in range (LEFT + WIDTH//2, WIDTH*NumofPiles, WIDTH * 2):
		stdraw.goto(i,BASE)
		countstones = gameState[position].count(1) 
		position+=1
		if not countstones == 0:
			for sNumber in range(countstones+1):
				stdraw.pendown()
				stdraw.circle(CIRCLE_RADIUS)
				stdraw.penup()
				stdraw.goto(i,BASE+(SPACE*sNumber))

				
#Draws the forward button.
def forward():
	button.speed(0)
	button.penup()
	button.goto(forwButt, TOP)
	button.fillcolor(forwColor)
	button.begin_fill()
	for i in range(2):
		button.forward(buttonWidth)
		button.left(90)
		button.forward(buttonHeight)
		button.left(90)
	button.end_fill()
	button.goto(forwButt + buttonWidth/4, TOP + 10)
	button.write("redo" , font=("Arial", 17, "normal"))

	
#Draws the backward button.	
def backward():
	button.speed(0)
	button.penup()
	button.goto(backButt, TOP)
	button.fillcolor(backColor)
	button.begin_fill()
	for i in range(2):
		button.forward(buttonWidth)
		button.left(90)
		button.forward(buttonHeight)
		button.left(90)
	button.end_fill()
	button.goto(backButt+buttonWidth/4, TOP+10)
	button.write("undo" , font=("Arial", 17, "normal"))	
	

		
#Checks the game state for a stone in a specific position. 
#Parameters: pile and stone, used as indices in the game state list.
#Returns: True if there is a stone in the position.
def getStone(pile,stone):
	if gameState[pile][stone] == 1:
		return True
	
#Places a stone in the game state in the position given.
#Parameters: pile and stone, used as indices in the game state list.
def setStone(pile,stone):
	for stn in range(0, stone):
		if gameState[pile][stn] == 0:
			gameState[pile][stn] = 1
		
#Removes a stone from the game state at the position given.
#Parameters: pile and stone, used as indices in the game state list.
def removeStone(pile,stone):
	for stn in range(maxstones-1, stone-1 , -1):
		if gameState[pile][stn] == 1:
			gameState[pile][stn] = 0
			
			
			
#Used to write the status of the game on the turtle graphic screen.
#Parameters: message: takes the message that we want to write on the turtle graphic.
def write(message):
	status.write(message, align = "center", font = ("Arial", 12, "normal"))
	
	
#Removes a stone on the screen.
#Parameters: pile and stone, used as indices in the game state list.
def remover(pile, stone):
	countstones = gameState[pile].count(1)
	counter = countstones - stone
	FirstPile = LEFT + WIDTH//2
	stnPosi = BASE + ((countstones - 1)*SPACE)
	pilePosi = FirstPile + (WIDTH*2) * pile
	remove.pen(pensize = 5, pencolor = "burlywood")
	
	for i in range(counter):
		remove.penup()
		remove.goto(pilePosi, stnPosi)
		remove.pendown()
		remove.circle(CIRCLE_RADIUS)
		stnPosi -= SPACE


		
#Creates a list that contain the numbers of stones in each pile.
#Then it appends that list into the bigger list in the variable recordData.		
def recordgame():
	global recordData
	Data = gmData()
	if dataIsUniqe(Data):
		recordData.append(Data)

		
#Access the list of each pile in the variable gameState and then counts
#all ones and then appends these numbers to the list Data and returns that list.		
def gmData():
	Data = []
	for pile in gameState:
		countstone = pile.count(1)
		Data.append(countstone)
	return Data		

	
#Access the list Data and then checks if that list with the numbers inside it matches
#any other lists in recordData. If not, returns True.
#Parameter: Data: a list that contain the number of stones in each pile
def dataIsUniqe(Data):
	uniqe = True
	for savedData in recordData:
			if Data == savedData:
				uniqe = False
	if uniqe:
		return True

		
		
#Opens a file to write and then writes all the numbers in recordData.
#Then it goes to the next line and writes a number that represents the turncount.
#Then it goes the line after that and writes a number that represents the value of first.
#After that the file is closed.
def save():
	status.clear()
	write("Saving..." )
	time.sleep(1)
	status.clear()
	write("Game is saved.")
	time.sleep(1)
	status.clear()
	
	savefile = open("save.txt", "w")
	for list in recordData:
		for data in list:
			savefile.write(str(data))
			savefile.write(" ")
	savefile.write("\n")
	savefile.write(str(turncount))
	savefile.write("\n")
	savefile.write(str(first))
	savefile.close()

	
#Loads the game from the file save.txt if the file exists, otherwise prints an error message.
#After that it closes the file.
def load():
	global turncount
	global recordData
	global first
	try:		
		loadfile = open("save.txt", 'r')
		Data = processData(loadfile)
		recordData = Data[:len(Data)-1]
		turncount = Data[len(Data)-1][0]
		first = Data[len(Data)-1][1]
		gameData = recordData[turncount]
			
		stdraw.clear()
		status.clear()
		write("Loading saved game...")
		time.sleep(1)
		status.clear()
		
		eraseData()
		newState(gameData)
		gamePiece()
		buttoncolor()
		
		write("Game was loaded.")
		time.sleep(1)
		status.clear()
		loadfile.close()
		
	except IOError:
		print("\nThere is no saved game.")
		status.clear()
		write("There is no saved game.")
		
	except:
		print("\nError while loading saved game.")
		status.clear()
		write("Error while loading saved game.")

		
#Creates a list of the number of stones in each pile.
#The last two numbers represent the turncount and value of the variable first recpectiveley.
#Parameters: loadfile: Takes a file that is opened to read data from.
def processData(loadfile):
	content = loadfile.read()
	dataList = content.split()
	proccessedData = []
	for data in dataList:
		convertData = int(data)
		proccessedData.append(convertData)
	data = setupData(proccessedData)
	if len(data[-1]) != 2:
		return
	return data

	
#Puts all data in the list into smaller lists, which contain the number of stones in each pile.
#The length of the smaller lists is arranged according to the number of piles. Each smaller list
#represent a recorded game round. The last list contains two numbers representing the turncount 
#and the value of first respectiveley. 
#Parameters: data: a list that contains all data in it.
#Returns: dataList: A list that contains smaller lists, which inside them are numbers that 
#represent the number of stones in each pile.
def setupData(data):
	dataList = []
	for i in range(0, len(data), NumofPiles):
		pileData = data[i:i+NumofPiles]
		dataList.append(pileData)
	return dataList
			
			
#Clears the previous game state.
def eraseData():
	for pile in range(NumofPiles):
		removeStone(pile, 0)
		
		
#Uses the game data list to place the stones in the loaded state.
#Parameter: gameData: Takes the list of gameData which contain the number of stones in each pile.
def newState(gameData):
	for pile in range(NumofPiles):
		stone = gameData[pile]
		setStone(pile, stone)		


		
#Clears the drawings of the stones on the gameboard and erases the
#stones in the current gameState and  and then decreaces turncount by 2.
#Then it uses the turncount to access the list in recordData that represent two
#backward moves and uses that list to put the new number of stones 
#in each pile in the gameState.
def back():
	global turncount
	stdraw.clear()
	eraseData()
	turncount -= 2
	previousMove = recordData[turncount]
	newState(previousMove)
	gamePiece()
	buttoncolor()

	
#Clears the drawings of the stones on the gameboard and erases the
#stones in the current gameState and  and then increments turncount by 2.
#Then it uses the turncount to access the list in recordData that represent two
#forward moves and uses that list to put the new number of stones 
#in each pile in the gameState.
def forw():
	global turncount
	stdraw.clear()
	eraseData()
	turncount += 2
	nextMove = recordData[turncount]
	newState(nextMove)
	gamePiece()
	buttoncolor()
	
	
#Checks that clicking one of the buttons would result in a valid action and performs that action if so.	
def validbutton(button):
	if button == "forward":
		if turncount < len(recordData)-2:		
			forw()
	
	if button == "backward":
		if compFirst():
			back()
		elif playFirst():
			back()

			
#Changes the color of the buttons.			
def buttoncolor():
	if turncount < len(recordData)-2:
		forwa("grey", "orange")
	else:
		forwa("orange", "grey")
	
	if compFirst():
		backwa("grey", "orange")
	
	elif playFirst():
		backwa("grey", "orange")
	
	else:
		backwa("orange", "grey")

		
#Returns True if the computer went first and the player has made at least one move.
def compFirst():
	if first == 1:
		if turncount > 1:
			return True

			
#Returns True if the player's turn was first and the player has made at least one move.			
def playFirst():
	if first == 0:
		if turncount > 0:
			return True
	
	
#Changes the color of the button forward.
#global forwColor is the variable that saves the color of the button forward.
#Parameters: color: the current color of the buttons that needs to be changed.
#			target: the color that we want to change the current color to it.
def forwa(color, target):
	global forwColor
	if forwColor == color:
		forwColor = target
		forward()

		
#Changes the color of the button backward.
#global backColor is the variable that saves the color of the button backward.
#Parameters: color: the current color of the buttons that needs to be changed.
#			target: the color that we want to change the current color to it.
def backwa(color, target):
	global backColor
	if backColor == color:
		backColor = target
		backward()
		
		
#Checks if the user clicked backward atleast once.  Then if the user removes a stone
#after clicking backward it deletes all lists in recordData that represent a forward move.	
def clearforward():
	global recordData
	if turncount < len(recordData)-2:
		recordData = recordData[:turncount+1]


		
#Randomly determines who goes first.
def firstTurn():
	global player1
	global player2
	roll = random.randint(0,1)
	player1 = playerlist[roll]
	player2 = playerlist[(roll+1)%2]
	return roll

	
#The computer's turn.		
def compturn():
	global turncount
	turncount += 1
	recordgame()
	status.clear()
	write("The computer is making a move.")
	time.sleep(1)
	
	winning = nimsum()
	if winning == 0:
		pile, stone = validpick()
	else:
		pile, stone = smartmove(winning)
	
	print ("\nComputer removed" , gameState[pile].count(1)-stone , "stones.")
	remover(pile, stone)
	removeStone(pile, stone)
	buttoncolor()
	recordgame()
	status.clear()
	if isGameOver():
		endGame()
		return
	else:
		write("It's your move.")

		
#Calculates the nim sum for use in the computer's strategy.
def nimsum():
	global gameState
	sum = gameState[0].count(1)
	for i in range (1, NumofPiles):
		sum = sum ^ gameState[i].count(1)
	return sum
	
	
#Chooses a pile and the bottom stone that the computer will take to maintain a winning position.
#Parameter: The nim sum - will not be zero
def smartmove(nsum):
	sums = []
	highest = 0
	for p in range(NumofPiles):
		st = gameState[p].count(1)
		if st > gameState[highest].count(1):
			highest = p
		if st ^ nsum < st:
			sums.append(p)
	pile = sums[0]
	top = gameState[pile].count(1)
	removed = top - (top ^ nsum)
	stone = top - removed
	if moveResult(pile,removed) == 0:
		pile = highest
		if oddpiles():
			stone = 0
		else:
			stone = 1
	return (pile,stone)

	
#Based on the potential move determined by the computer, 
#counts the number of piles that will be left with more than one stone.
def moveResult(pile,removed):
	pilesover1 = 0
	for p in range(NumofPiles):
		numcurr = gameState[p].count(1)
		if p == pile:
			numleft = numcurr-removed
		else:
			numleft = numcurr
		if numleft > 1:
			pilesover1 += 1
	return pilesover1

	
#Counts the number of piles with one stone, returning True for an odd number and False for an even number.	
def oddpiles():
	counter = 0
	for p in gameState:
		if p.count(1) == 1:
			counter += 1
	if counter % 2 == 1:
		return True
	else:
		return False
		
		
#Chooses a single stone to remove.
def validpick():
	validpick = False
	while not validpick:
		pile = random.randint(0,NumofPiles-1)
		stone = gameState[pile].count(1)-1
		if getStone(pile, stone):
			validpick = True

	return (pile, stone)

	
	
#Checks if the coordinates that the user clicked on are on any of the buttons:
#Parameters: x: the x coordinate.
#			y: the y coordinate.
def whatButton(x, y):
	button = None
	if y > TOP and y < TOP + buttonHeight:
		
		if x > forwButt and x < forwButt + buttonWidth:
			button = "forward"
		
		elif x > backButt and x < backButt + buttonWidth:
			button = "backward"

	return button
	
	
#Matches the screen x position to a pile.		
def whatPile(x):
	count = 0
	pile = None
	for p in range(CIRCLE_EDGE, WIDTH*((2*NumofPiles)-1), WIDTH*2):
		if x > p and x < p + CIRCLE_RADIUS * 2:
			pile = count
		count += 1
	return pile
	
	
#Matches the screen y position to a stone.
def whatStone(y):
	counter = 0	
	stone = None
	for stn in range(BASE, TOP, SPACE):
		if y > stn and y < stn + CIRCLE_RADIUS*2:
			stone = counter
		counter += 1
	return stone	

	
	
#Checks if one Pile is left.
def Lastpile():
	zeroStonePile = 0
	for pile in range(NumofPiles):
		if gameState[pile].count(1) == 0:
			zeroStonePile += 1
	if zeroStonePile == NumofPiles-1:
		return True
	
	
#Returns True if a click on a stone would result in a valid move.
#Parameters: pile: Checks if the indicie of pile is valid.
#			stone: Checks if the indicie of stone is valid	
def validclick(pile, stone):
	if pile != None and stone != None:
		if getStone(pile,stone):
			if not Lastpile():
				return True
			elif stone == 0:
				print("\nYou don't want to remove the last object!")
				status.clear()
				write("You don't want to remove the last object!")
			else:
				return True

				
#Responds to a click on the window, recording the move and ending the player's turn if it is on an existing stone.	
def stoneclick(x,y):
	global turncount
	pile = whatPile(x)
	stone = whatStone(y)
	button = whatButton(x, y)
	validbutton(button)
	if validclick(pile, stone):
		clearforward()
		recordgame()
		turncount += 1
		turnEnd(pile, stone)
		
		
#Removes the chosen stones from the board and game state, and checks for a game over state before the computer's turn.
def turnEnd(pile, stone):
	global turncount
	countstone = gameState[pile].count(1)
	status.clear()
	write("Removing your stones." )
	print ("\nRemoved" , countstone - stone , "stones.")
	remover(pile, stone)
	removeStone(pile, stone)
	recordgame()
	buttoncolor()
	if isGameOver():
		endGame()
		return
	else:
		time.sleep(1)
		compturn()

		
	
#Checks for a game over state (total stones less than 2).
def isGameOver():
	if countStones() < 2:
		return True
	else: 
		return False
		
		
#Counts the number of stones remaining in the game.
def countStones():
	counter = 0
	for pile in gameState:
		for stone in pile:
			if stone == 1:
				counter += 1
	return counter
		
		
#Disables clicks and buttons and prints the winner.	
def endGame():
	wn.onkey(None, 's')
	wn.onkey(None, 'l')
	wn.onclick(None)
	if turncount % 2 == 0:
		if countStones() == 0:
			winner = player1
		else:		
			winner = player2
	else:
		if countStones() == 0:
			winner = player2
		else:
			winner = player1
	gmover(winner)
	print("\nGame over. The winner is:" , winner)

	
#Clears the board and writes the game over message on the screen.
#Parameter: winner as determined when in the endGame function.
def gmover(winner):
	time.sleep(1)
	nim.clear()
	draw.clear()
	stdraw.clear()
	status.clear()
	button.clear()
	
	over = turtle.Turtle()
	over.hideturtle()
	over.pen(pencolor = "red", pensize = 7, speed = 0)
	over.penup()
	over.goto(-270, 0)
	over.write("Game Over" , font=("Arial", 75, "normal"))
	over.goto(0, -100)
	over.write(winner + " wins!" , align = "center", font=("Arial", 50, "normal"))
	

	
#Initializes the game, then sets up the responses to clicks and the save and load keys.	
def main():
	global first
	intro()
	welcome()
	gameBoard()
	gamePiece()
	first = firstTurn()
	if first == 1:
		print("\nThe computer goes first.")
		write("The computer will move first.")
		time.sleep(1)
		compturn()
	if first == 0:
		print("\nYou get to go first!")
		write("You get to go first!")
	
	wn.onclick(stoneclick)
	
	wn.onkey(save, 's')
	wn.onkey(load, 'l')
	wn.listen()
	
	wn.mainloop()

if __name__ == "__main__":
	main()