# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 15:46:21 2022

@author: Dewald
"""

import mouse
import keyboard
import time
import os

events = []                 #This is the list where all the events will be stored
Play = ""

def recordmouse():
   mouse.hook(events.append)   #starting the mouse recording
   keyboard.wait("a")          #Waiting for 'a' to be pressed
   mouse.unhook(events.append) #Stopping the mouse recording
   #print(events)
   f = open("Mouse.txt","w+")
   for x in events:  
    f.write(str(x) +"\n") 
   f.close()
   #print(str(events))
   #mouse.play(events)

def playmouse():
   f = open("Mouse.txt","r")
   with open("Mouse.txt") as f:
     z = str(f.read())
     y = z.replace("),", "), ")
     events.append(y)
   print("\n ------------------")
   #print(events) Displays contents of the folder
   try:
       mouse.play(events)
   except Exception as e:
       print("error")

Record = input("Do you want to record mouse movement? (Y/N)\n")
if Record.upper() == "Y":
 timer = 10
 while timer >= 1:
  time.sleep(1)
  timer -= 1 
  print("Recording Starting in: "+str(timer))
 print("Recording Starting")
 recordmouse()

def playevent():
 while Play.upper() != "N":
  Play = input("Do yo want to play the recording (Y/N)\n")
 if Play.upper() == "Y":
  playmouse()
 else:
  print("Shutting Down..........")
