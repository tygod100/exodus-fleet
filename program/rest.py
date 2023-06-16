from classes import node
from classes import gameData
from classes import vessel
from random import randint
from math import ceil
from math import floor

def rest(load):
    
    
    display = ["Actions you can do:"]
    
    # print paly resources
    print("you have\n", load.basic, "Basic and\n", load.luxury, "Luxury resources\n")
    
    # is the current node hads a Civilisation, add trade to list of thign you can do.
    if load.currentNode.hasCivilisation: display.append("trade")
    
    display.append("manage vessels", )
    display.append("embark")
    display.append("")
    
    for x in display:
        print(x)
    
    action = input("Play: ")
    
    if action == "embark":
        load = embark(load)
    elif action == "manage" or action == "manage vessels":
        load = vesselManagement(load)
    elif action == "trade": 
        if load.currentNode.hasCivilisation:
           load = trade(load)
        else:
            print("There's no one the trade with")
    if action == "end":
        load.endingGame = True
        
    return load


def trade(load):
    rate = 5 + ceil(10 * load.currentNode.wealth) #conversion rate for number of Basic per Luxury
    
    print("you have\n", load.basic, "Basic and\n", load.luxury, "Luxury resources")
    
    print("\nThe current conversion rate is ")
    print(rate, "Basic per 1 Luxury resource\n")
    
    #after printing conversion rate, ask player to chouse what they want to get
    choice = input("Which resource were you looking for? Basic(1) or Luxury(2)\n").lower()
    
    # trade for basic
    if choice == "basic" or choice == '1': 
        print("you can buy up to", rate*load.luxury, "basic resources. How much do you want?")
        choice = input()
        if choice.isdigit() and not choice == "0":
            #calculate the cost of wha the player is asking for
            cost = ceil(float(choice)/rate)
            
            print("you are trading", cost, "luxury resources for", cost*rate, "basic resources.")
            
            if cost > load.luxury: #if the amount of luxury it would take for to get what the palyer wants, end
                print("you can't afford this")
            else:
                choice = input("Do you want this? yes(Y)/no(N)").lower()
                if choice == "yes" or choice == 'y':
                    load.basic += cost*rate
                    load.luxury -= cost
                    print("You now have", load.basic, "basic and", load.luxury, "luxury resources")
                else:
                    print("Ok then")
        else: print("Ok then")
    # trade for luxury
    elif choice == "luxury" or choice == '2':
        maxBuy = floor(float(load.basic)/rate) # the max number of you can buy with out going below 0
        
        if float(load.basic)%rate == 0: maxBuy -= 1 #if buying the max numver of , then lower maxBuy my one so the player don't accdenly start them selfs
        
        print("you can buy up to", maxBuy, "luxury resources. How much do you want?")
        choice = input()
        if choice.isdigit() and not choice == "0":
            #calculate the cost of wha the player is asking for
            cost = int(choice)*rate
            print("you are trading", cost, "basic resources for", choice, "luxury resources.")
            
            if cost >= load.basic:#if the amount of luxury it would take for to get what the palyer wants, end
                print("you can't afford this")
            else:
                choice = input("Do you want this? yes(Y)/no(N)").lower()
                if choice == "yes" or choice == 'y':
                    load.basic -= cost
                    load.luxury += int(cost/rate)
                    print("You now have", load.basic, "basic and", load.luxury, "luxury resources")
                else:
                    print("Ok then")
    else:
        print("Ok then")
    
    return load

def embark(load):
    
    # list all futureNodes and assign them a number, also here is a nested loop
    for x in load.futureNodes:
        print("\nNumber:", load.futureNodes.index(x) + 1)
        for xx in x.getInfo():
            print(xx)
            
    
    choice = input("\nEnter the number of the node you want to go to, enter anyting else to cancel: \n")
    
    #When the player picks a note, set that node to the current node and clear then fill futureNodes with new randomized nodes
    if choice.isdigit() and int(choice) <= len(load.futureNodes):
        load.currentNode = load.futureNodes[int(choice)-1]
        load.futureNodes.clear()
        for x in range(randint(1,3)):
            load.futureNodes.append(node())
            load.futureNodes[x].randomize()
    else: # canssles if player netered something outside the given list or that isn't a number
        print("never mind then")
    return load

def vesselManagement(load):#holding off on working on this to wfinish the rest of the project, might need to edit flowchart
    
    
    # parallel array listing the Vessels anf there values for both the player's and the node
    playerVessels = []
    playerVesselsValues = []
    nodeVessels = []
    nodeVesselsValues = []
    
    #filling the arrays
    for x in load.vessels:
        playerVessels.append(x.name)
        playerVesselsValues.append(x.value)
    
    for x in load.currentNode.vessels:
        nodeVessels.append(x.name)
        nodeVesselsValues.append(x.value)
    
    listLenght = len(playerVessels)
    if listLenght < len(nodeVessels): listLenght = len(nodeVessels)
    
    rowSize = 20
    
    print ("   Own vessels" + (" " * (rowSize - len(" Own vessels"))) + "   " + " available vessels" + (" " * (rowSize - len(" available vessels"))) + "   ")
    
    for x in range(listLenght):
       #print(playerVessels[x] + (" " * ( rowSize - (len(playerVessels[x]) + len(str(playerVesselsValues[x]) ) ) ) + str(playerVesselsValues[x]) +  + nodeVessels[x] + (" " * ( rowSize - (len(nodeVessels[x]) + len(str(nodeVesselsValues[x]) ) ) ) + str(nodeVesselsValues[x]) )
       print("|" , end = " ")
       print(playerVessels[x] , end = "")
       print( " " * ( rowSize - (len(playerVessels[x]) + len(str(playerVesselsValues[x]) ) ) ) ,end = "")
       print( str(playerVesselsValues[x]) ,end = " | ")
       
       print(nodeVessels[x] , end = "")
       print( " " * ( rowSize - (len(nodeVessels[x]) + len(str(nodeVesselsValues[x]) ) ) ) ,end = "")
       print( str(nodeVesselsValues[x]) ,end = " | ")
       
       #print("")
       
    print("this system is not finished yet")
    return load