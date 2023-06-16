from random import random
from random import choice
from math import ceil

def travel(load):
    
    eventCheck = 1.0
    distanceTraveled = 0
    
    
    ''' this while will stop at 3 events
     when the distance to the next node is 0
     when the play has run out off basic resuese
     and when RNG saiese the player run into something'''
    while load.currentNode.distance > 0 and load.basic > 0 and eventCheck > load.risk:
        for x in load.vessels:
            used = x.useage
            distanceTraveled += used
            load.basic -= used
        load.currentNode.distance -= 1
        eventCheck = random()
    
    print("used up ", distanceTraveled, " basic resouse before...")
    
    if load.currentNode.distance <= 0:
        print("you araived at your destination \n")
    elif eventCheck < load.risk:
        #print("you would have ran into someting if I had finished the event system")
        load = event(load)
        eventCheck = 1.0
    
    return load 
    
def event(load): # not finished yet, chouse to hold off so I can wor kon the other systems, will need to go back to the flowchart for this
    chance = random()
    
    events = getEvents()
    
    event = choice(events)
    print("\n",event["text"])
    
    load = action(load, event)
    
    return load

def action(load, event):# part of event
    
    temp = ""
    """
    this is ment to read a set of commands from a event in a code I will design
    but for now it will just give to player a set amout of resources
    """
    for x in event["actions"]:
        for xx in x:
            if xx.isdigit(): 
                temp = temp + xx
    
    load.basic += eval(temp)
    
    print("\n","you gain",  temp, "basic resource")
    print("something else would have happoned if I had finished the event system")
    return load
    

def getEvents(): # get a list of events from a file
    file = open("data/events.txt")
    
    rawText = file.read()
    
    file.close()
    
    rawEvents = []
    for x in range(len(rawText)):
        if rawText[x] == '{':
            rawEvents.append(rawText[x+1:x+rawText[x:].index('}')])
    
    events = []
    
    for x in rawEvents:
        event = {}
        
        parts = x.split(";")
        
        event["name"] = parts[0]
        event["text"] = parts[1]
        
        event["actions"] = parts[2:]
        
        events.append(event)
        '''
        if "text:" in x:
            whereTextIs = x.index("text:")
            event["text"] = x[whereTextIs:x[whereTextIs:].index(';') + whereTextIs]
        else:
            event["text"] = x[:x.index(';')]
        
        if "basic:" in x:
            whereTextIs = x.index("basic:")
            event["text"] = x[whereTextIs:x[whereTextIs:].index(';') + whereTextIs]
        '''
    return events
    
    