# room1.py
# The function draws and activates a room1
import sys
sys.path.append("..")
from graphics import *
from button import Button
from widgets import storytell
import time

def room1(win, inventory):

# setting base variables
  continueGame = True
  lost = False

# drawing room
  img1 = Image(Point(20, 10), "rooms/room1.gif")
  img1.draw(win)

# drawing user
  user = Image(Point(20,1), "rooms/thief.gif")
  user.draw(win)

# drawing inventory label
  inventLabel = Text(Point(5, 19), "Inventory")
  inventLabel.setStyle("bold")
  inventLabel.draw(win)

# drawing a button that says that a person can put an item into inventory by pressing g
  get_item = Button(win, Point(5,2), 8, 2, "Get Item by Pressing <g>")

# drawing inventory items
  inventoryTexts = []
  last = 17
  for x in inventory:
      inventoryTexts.append(Text(Point(5,last), x))
      last = last - 1
  for x in inventoryTexts:
      x.draw(win)

  # setting up the key items for the room and what can be collected
  main_item = 'candle'
  things_in_room = {"Point(21.0,11.0)": "candle", "Point(28.0,3.0)": "candle", "Point(12.0,2.0)": "plant"}

  # storytell


  # Storytell The beginning
  storytell(win,
        "Hey player! Welcome to Escape Room, a game where you will need to complete tasks in each of the rooms to unlock the next one. You are a thief, located in an extremely safe house looking for the jackpot, but how will you get to it? All of the doors are locked, and you can’t go back to a room once you get to the next one. There is a certain amount of items in each room that you will need along the way, so pay close attention or you will lose! Good luck!")
  storytell(win, "You can move around by pressing arrow buttons")
  storytell(win,
        "Hmm… this house is so big! The people that live here must have so much money! Oh wait, there is a letter in the table. The letter reads: “Dear Mom, I have left 3 bars of gold in the safe located in our room. I gave you the code to open it last week, but just in case you forgot, each room of the house has a clue to figure it out! Hope you do’t have any trouble. Love, your daughter and John.” ")
  storytell(win, "Nice! I’ll get those bars pretty easily. Now, I see some stairs that lead somewhere, but it’s so dark… what should I do?")


  while continueGame is True and lost is False:

      # ask for key input (arrows)
      k = win.getKey()
      # check which arrow was pressed and move the user accordingly 
      # while also checking that the user doesn't go outside the room's
      # borders
      if k == "Right" and user.getAnchor().getX() != 30:
          user.move(1, 0)
      if k == "Left" and user.getAnchor().getX() != 10:
          user.move(-1, 0)
      if k == "Up" and user.getAnchor().getY() != 20:
          user.move(0, 1)
      if k == "Down" and user.getAnchor().getY() != 0:
          user.move(0, -1)

      if k == 'G' or k == 'g':
        if get_item.active:
            inventory.append(item)
            inventoryTexts.append(Text(Point(5, last), item))
            last = last - 1
            inventoryTexts[-1].draw(win)

      # Getting user location
      usx = user.getAnchor().getX()
      usy = user.getAnchor().getY()

      user_pos = "Point({0},{1})".format(usx, usy)
      # Activating a pickup button if the user is standing on a candle
      if user_pos in things_in_room.keys() and things_in_room[user_pos] not in inventory:
          item = things_in_room[user_pos]
          get_item.activate()
      else:
          get_item.deactivate()
        
      # checks that if user tries to go through the 
      # left door, he/she dies
      if usx == Point(10.0, 7.0).getX() and usy == Point(10.0, 7.0).getY():
        storytell(win,"The thief went into the living room and the dog got woken up and barked till the neighbours came. You loose! The thief got arrested.")
        continueGame = False
        lost = True

      # checking the ladder
      if usx >= Point(10.0, 17.0).getX() and usx<= Point(16.0, 17.0).getX() and usy >= Point(10.0, 17.0).getY() and usy <= Point(10.0, 20.0).getY():
          # checking if a user has essential item
          if main_item in inventory:
              # delete the room picture on the screen
              storytell(win,"Good job! You passed the first room with the help of the candle in your inventory! Now it’s time for the next room. ")
              user.undraw()
              img1.undraw()
              for i in inventoryTexts:
                  i.undraw()
              get_item.undrawButton(win)
              # and return the state
              return True, False, inventory
          else:
              storytell(win,"The stairs were too dark and the thief fell down, opened his head and layed unconscious until the owners came back. Next, he was arrested.")
              return False, True, inventory





  return continueGame, lost, inventory