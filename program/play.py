
from classes import gameData
from classes import node
from classes import vessel
from random import random
from rest import rest
from travel import travel

        

def play(load):
    
   if load.endingGame == True:
       return None
    
   if load.currentNode.distance > 0:
       load = travel(load)
   else:
       load = rest(load)
   
   if load.basic == 0:
        print(load) 
        load.endingGame = True
        load = None
   input("\nhit enter to continue...")
   print("\n"*5)
   return load 