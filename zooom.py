import os
import csv
import pyautogui
from time import sleep
from datetime import datetime


#https://zoom.us/j/(10 digit number)
def startzoom():  
  os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

  sleep(2)
  if "zoom" in meetingnumber:
    meetinglink = meetingnumber
  else:
    meetinglink = "https://zoom.us/j/" + meetingnumber

  pyautogui.write(meetinglink)

  pyautogui.press("enter")


def seperator():
  newList = []
  with open("codes.csv", newline = "") as csvfile:
    thing = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in thing:
      newList = newList + row
  return newList

listt = seperator()



while True:
  while True:
    sleep(20)
    now = datetime.now().strftime("%H:%M")
    print(now)
    if now in listt:
      stimeindex = listt.index(now)
      stime = now
      meetingnumber = listt[stimeindex+1]
      ltime = listt[stimeindex+2]
      print (stime, meetingnumber, ltime)
      listt.remove(stime)
      listt.remove(meetingnumber)
      listt.remove(ltime)

      startzoom()
      break
    

  while True:
    sleep(20)
    now = datetime.now().strftime("%H:%M")
    print(now)
    if now == ltime :
      os.system("TASKKILL /F /IM msedge.exe")
      os.system("TASKKILL /F /IM zoom.exe")
      break
