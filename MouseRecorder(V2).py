# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 15:46:21 2022

@author: Dewald
"""

import mouse
import keyboard
import time
import os
import tkinter as tk

events = []                 #This is the list where all the events will be stored

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

def recorder1():
  #Totals.delete(0,15)
  print("1")
  Totals.insert(1,"press a to start recording")
  print("2")
  #keyboard.wait("a")
  print("3")
  recordmouse()

def playevent():
  playmouse()

window = tk.Tk()

Totals = tk.Entry()
Totals.insert(0,"Countdown Timer")
Totals.pack()

PlayScript = tk.Button(
    text="Play Script",
    width=25,
    height=5,
    bg="Green",
    command = playevent)
PlayScript.pack()

RecordScript = tk.Button(
    text="Record Script",
    width=25,
    height=5,
    bg="Red",
    command = recorder1)
RecordScript.pack()

window.mainloop()