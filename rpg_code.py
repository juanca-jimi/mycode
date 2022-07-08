#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live



""" Used in the GoRandom() function """
import random

def showInstructions():
    #print a main menu and the commands
    print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
  ''')

def showStatus():
      #print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
  #print the current inventory
    print('Inventory : ' + str(inventory))
  #print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")

"""
This code will execute if you enter the garden and pick up the paper

if you get this riddle right, you acquire an escape potion!
The escape potion is meant to allow you to escape the monster ONE time
"""
def riddle():
    #checks the input of the user with correct answer
    if input('what word is spelled incorrectly in the dictionary?') == 'incorrectly':
        print('You have gained the ability to escape the monster 1 time')
        inventory.append("escape")
    else:
        print('the correct answer is \'incorrectly\', better luck next time!')


#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

        'Hall' : {
            'south' : 'Kitchen',
            'east'  : 'Dining Room',
            'item'  : 'key'
            },

        'Kitchen' : {
            'north' : 'Hall',
            'item'  : 'monster',
            },
        'Dining Room' : {
            'west' : 'Hall',
            'south': 'Garden',
            'item' : 'potion',
            'north' : 'Pantry',
            },
        'Garden' : {
            'north' : 'Dining Room',
            'item' : 'paper'
            },
        'Pantry' : {
            'south' : 'Dining Room',
            'item' : 'cookie',
            }
        }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()



"""
The purpose of this function is to take you to another room, it may be the exact same one that you're in now 
or any other key in the rooms dictionary

-JC
"""
def goRandom():
    print('You\'re teleporting to a random room')

    #this takes you to any key in the dictionary
    #that key will be a room we go to
    
    room_list  = list(rooms)
    print(room_list)
    randomRoom = random.choice(room_list)
    print(randomRoom)
    currentRoom = randomRoom


#loop forever
while True:

    showStatus()

    #get the player's next 'move'
    #.split() breaks it up into an list array
    #eg typing 'go east' would give the list:
    #['go','east']
    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        
       
    # This else if statement allows the user to go to any room dependent on the random function 
        
        elif move[1] == 'random':
            goRandom()
    #there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        #if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item from the room
            del rooms[currentRoom]['item']
            #if the got the riddle 
            if move[1] == 'paper': 
                riddle()
        #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    ## Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break

    ## If a player enters a room with a monster
    #if player has an escape, it will be saved from the monster
    elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] and 'escape' in inventory:
        #removes the escape from the inventory so that next time the player encounters the 
        #monster, it may be game over
        inventory.remove('escape')
        print(f'you have used to \'escape\' to hide from the monster. Next time you may not be so lucky!') 
    elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break
