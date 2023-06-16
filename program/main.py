
from classes import gameData

import play as game
'''
 I might have been too ambitious with this. 
 I could have made sometihng smaller like that tic-tac-tow thing that one person made or blackjack
'''
load = None

titleFile = open("data/title.txt")
title = titleFile.read();
titleFile.close()

startgame = ""

while startgame != "end":
    
    print(title)
    
    print("enter 'start' to play")
    print("you can't load or save games becasue I haven't finished that yet\n")
    
    if startgame == "start":
        load = gameData("test")
    elif startgame == "load":
        print("I haven't finished that yet")
    while load != None:
        load = game.play(load)
        if load == None: print ("End game")
    
    startgame = input("> ").lower()


print("end")