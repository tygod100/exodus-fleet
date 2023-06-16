from random import random
from random import randint
"""
class vessel:
    def __init__(self, name, fuelUseage, value):
        self.useage = fuelUseage
        self.name = name
        self.value = value
        self.special = ""
        
               ci
"""

class vessel:
    def __init__(self, name, fuelUseage, value, special = ""):
        self.useage = fuelUseage
        self.name = name
        self.value = value
        self.special = special

class node:
    def __init__(self, distance = 10, hasCivilisation = True , wealth = 0.5):
        self.distance = distance
        self.hasCivilisation = hasCivilisation
        self.wealth = wealth
        self.vessels = [vessel("Rowboat", 1, 100)]
        
        
    def randomize(self): #create a randomley genrated node
        self.wealth = random()
        if random() < 0.4: 
            self.hasCivilisation = True
        else:
            self.hasCivilisation = False
        self.distance = randint(9,25)
        
               
    def getInfo(self): #retruns a array containg info on the node
        civilisationInfo = "Decadent"
        if self.hasCivilisation:
            if self.wealth < 0.2: civilisationInfo = "Impoverished"
            elif self.wealth < 0.4: civilisationInfo = "Poor"
            elif self.wealth < 0.6: civilisationInfo = "Decent"
            elif self.wealth < 0.8: civilisationInfo = "Wealthy"
        else:
            civilisationInfo = "None"
        civilisationInfo = "Civilisation: " + civilisationInfo
        return ["Distance: " + str(self.distance), civilisationInfo]
        
    def __str__(self):
        return f"{self.distance}({self.wealth})"   
    
class gameData: 
    def __init__(self, filename):
        self.fileName = filename
        self.basic = 100
        self.luxury = 0
        self.currentNode = node(0, True, 0.5)
        self.futureNodes = [node(10, True, 0.5)]
        self.vessels = [vessel("Flagship", 1, 0, "PERM")]
        self.endingGame = False
        self.risk = 0.1
    def getScore(self): #score is based of how much resources player has and the sum of each vessel's value
        score = self.basic
        score += self.luxury * 5
        for x in self.vessels:
            score += x.value
        return score
    
    def __str__(self):
        return f"{self.fileName}({self.getScore()})"   