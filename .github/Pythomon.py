import math
import time
import random
print("Welcome to Pythomon!")
time.sleep(0.5)
print("Choose your Pythomon!")
time.sleep(0.25)
print("1. Chonkers, 2. Ballerson, 3. Sausage")
print()
time.sleep(0.25)
Choice = input("Type here ")
if Choice.lower() == "chonkers":
  HP = 150
if Choice.lower() == "ballerson":
  HP = 115
if Choice.lower() == "sausage":
  HP = 100
if Choice.lower() != "chonkers" and Choice.lower() != "ballerson" and Choice.lower() != "sausage":
  print("Invalid Choice!")
  quit()
print("Go,", Choice,"!")
time.sleep(0.25)
P2 = random.randint(1,3)
if P2 == 1:
  Choice3 = "Willow"
  HP2 = 100
if P2 == 2:
  Choice3 = "Tohru"
  HP2 = 125
if P2 == 3:
  Choice3 = "Taco"
  HP2 = 115
print("Opponent sent out", Choice3,"!")
time.sleep(0.25)


#all of while loop indented one space
#Chonkers selected
if Choice.lower() == "chonkers":
  while HP > 0 and HP2 > 0:
  #day 6 code, attacking moves and changed willow to choice3
    print("Select a move!", "Attack or Defend!")
    Choice2 = input()
    time.sleep(0.25)
    print(Choice, "used", Choice2)
    if Choice2.lower() == "attack":
      DMG = random.randint(15,30)
      HP2 = HP2 - DMG
      print(Choice3,"'s HP is now", HP2)
    elif Choice2.lower() == "defend":
      DEF = random.randint(10,20)
      HP = HP + DEF
      print(Choice,"'s HP is now", HP)
    time.sleep(0.25)
    P1 = random.randint(1,3)
    DMG2 = random.randint(15,30)
  #trying to make invalid moves not work
    if P1 > 1:
      time.sleep(0.25)
      print(Choice3, "used Attack")
      HP = HP - DMG2
      time.sleep(0.25)
      print(Choice,"'s HP is now", HP)
    elif P1 < 2:
      DEF2 = random.randint(10,20)
      time.sleep(0.25)
      print(Choice3, "used Defend")
      time.sleep(0.25)
      HP2 = HP2 + DEF2
      print(Choice3,"'s HP is now", HP2)

#^^^ Character 1 ^^^
#VVV Character 2 VVV

#Ballerson selected
if Choice.lower() == "ballerson":
  while HP > 0 and HP2 > 0:
      print("Select a move!")
      print("Hurricane or ")
      Choice2 = input()
      time.sleep(0.25)
      print(Choice, "used", Choice2)
      if Choice2.lower() == "attack":
        DMG = random.randint(15,30)
        HP2 = HP2 - DMG
        print(Choice3,"'s HP is now", HP2)
      elif Choice2.lower() == "defend":
        DEF = random.randint(10,20)
        HP = HP + DEF
        print(Choice,"'s HP is now", HP)
      time.sleep(0.25)
      P1 = random.randint(1,3)
      DMG2 = random.randint(15,30)
      if P1 > 1:
        time.sleep(0.25)
        print(Choice3, "used Attack")
        HP = HP - DMG2
        time.sleep(0.25)
        print(Choice,"'s HP is now", HP)
      elif P1 < 2:
        DEF2 = random.randint(10,20)
        time.sleep(0.25)
        print(Choice3, "used Defend")
        time.sleep(0.25)
        HP2 = HP2 + DEF2
        print(Choice3,"'s HP is now", HP2)

#^^^ Character 2 ^^^
#VVV Character 3 VVV

#Sausage selected
if Choice.lower() == "sausage":
  while HP > 0 and HP2 > 0:
    print("Select a move!", "Attack or Defend!")
    Choice2 = input()
    time.sleep(0.25)
    print(Choice, "used", Choice2)
    if Choice2.lower() == "attack":
      DMG = random.randint(15,30)
      HP2 = HP2 - DMG
      print(Choice3,"'s HP is now", HP2)
    elif Choice2.lower() == "defend":
      DEF = random.randint(10,20)
      HP = HP + DEF
      print(Choice,"'s HP is now", HP)
    time.sleep(0.25)
    P1 = random.randint(1,3)
    DMG2 = random.randint(15,30)
    if P1 > 1:
      time.sleep(0.25)
      print(Choice3, "used Attack")
      HP = HP - DMG2
      time.sleep(0.25)
      print(Choice,"'s HP is now", HP)
    elif P1 < 2:
      DEF2 = random.randint(10,20)
      time.sleep(0.25)
      print(Choice3, "used Defend")
      time.sleep(0.25)
      HP2 = HP2 + DEF2
      print(Choice3,"'s HP is now", HP2)
if HP <= 0:
  print(Choice, "was defeated!")
  time.sleep(0.25)
  print("Defeat!")
if HP2 <= 0:
  print("Willow was defeated!")
  time.sleep(0.25)
  print("Victory!")