import time
import random
print("Welcome to Pythomon!")
print()
time.sleep(0.5)
print("Choose your Pythomon!")
print()
time.sleep(0.25)
print("1. Chonkers, 2. Ballerson, 3. Sausage")
print()
time.sleep(0.25)
Choice = input("Type here ")
HP = 0 
HP2 = 0
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
  Choice4 = "Bite"
  C5 = "Darkcharm"
  HP2 = 100
if P2 == 2:
  Choice3 = "Tohru"
  Choice4 = "Earthquake"
  C5 = "Enrage"
  HP2 = 125
if P2 == 3:
  Choice3 = "Taco"
  Choice4 = "Uppercut"
  C5 = "Focus"
  HP2 = 115
print("Opponent sent out", Choice3,"!")
time.sleep(0.25)

#Chonkers selected
if Choice.lower() == "chonkers":
  while HP > 0 and HP2 > 0:
    print("Select a move!")
    print("Tumble or Eat")
    Choice2 = input()
    time.sleep(0.25)
    print(Choice, "used", Choice2)
    if Choice2.lower() == "tumble":
      DMG = random.randint(15,30)
      HP2 = HP2 - DMG
      print(Choice3,"'s HP is now", HP2)
    elif Choice2.lower() == "eat":
      DEF = random.randint(25,35)
      HP = HP + DEF
      print(Choice,"'s HP is now", HP)
    if Choice2.lower() != "tumble" and Choice2.lower() != "eat":
      print("It did nothing...")
    time.sleep(0.25)
    if HP2 <= 0:
      print(Choice3, "was defeated!")
      time.sleep(0.25)
      print("Victory!")
      quit()
    P1 = random.randint(1,3)
    if P2 == 1:
      DMG2 = random.randint(15,25)
    if P2 == 2:
      DMG2 = random.randint(25,32)
    if P2 == 3:
      DMG2 = random.randint(20,28)
    if P1 > 1:
      time.sleep(0.25)
      print(Choice3, "used", Choice4)
      HP = HP - DMG2
      time.sleep(0.25)
      print(Choice,"'s HP is now", HP)
    if HP <= 0:
      print(Choice, "was defeated!")
      time.sleep(0.25)
      print("Defeat!")
      quit()
    elif P1 < 2:
      DEF2 = random.randint(10,20)
      time.sleep(0.25)
      print(Choice3, "used", C5)
      time.sleep(0.25)
      HP2 = HP2 + DEF2
      print(Choice3,"'s HP is now", HP2)

#^^^ Character 1 ^^^
#VVV Character 2 VVV

#Ballerson selected
if Choice.lower() == "ballerson":
  while HP > 0 and HP2 > 0:
      print("Select a move!")
      print("Hurricane or Dewdrop!")
      Choice2 = input()
      time.sleep(0.25)
      print(Choice, "used", Choice2)
      if Choice2.lower() == "hurricane":
        DMG = random.randint(20,35)
        HP2 = HP2 - DMG
        print(Choice3,"'s HP is now", HP2)
      elif Choice2.lower() == "dewdrop":
        DEF = random.randint(12,24)
        HP = HP + DEF
        print(Choice,"'s HP is now", HP)
      if Choice2.lower() != "hurricane" and Choice2.lower() != "dewdrop":
        print("It did nothing...")
      time.sleep(0.25)
      if HP2 <= 0:
        print(Choice3, "was defeated!")
        time.sleep(0.25)
        print("Victory!")
        quit()
      P1 = random.randint(1,3)
      if P2 == 1:
        DMG2 = random.randint(15,25)
      if P2 == 2:
        DMG2 = random.randint(25,32)
      if P2 == 3:
        DMG2 = random.randint(20,28)
      if P1 > 1:
        time.sleep(0.25)
        print(Choice3, "used", Choice4)
        HP = HP - DMG2
        time.sleep(0.25)
        print(Choice,"'s HP is now", HP)
      if HP <= 0:
        print(Choice, "was defeated!")
        time.sleep(0.25)
        print("Defeat!")
        quit()
      elif P1 < 2:
        DEF2 = random.randint(10,20)
        time.sleep(0.25)
        print(Choice3, "used", C5)
        time.sleep(0.25)
        HP2 = HP2 + DEF2
        print(Choice3,"'s HP is now", HP2)

#^^^ Character 2 ^^^
#VVV Character 3 VVV

#Sausage selected
if Choice.lower() == "sausage":
  while HP > 0 and HP2 > 0:
    print("Select a move!")
    print("Scratch or Rest!")
    Choice2 = input()
    time.sleep(0.25)
    print(Choice, "used", Choice2)
    if Choice2.lower() == "scratch":
      DMG = random.randint(12,28)
      HP2 = HP2 - DMG
      print(Choice3,"'s HP is now", HP2)
    elif Choice2.lower() == "rest":
      DEF = random.randint(20,30)
      HP = HP + DEF
      print(Choice,"'s HP is now", HP)
    if Choice2.lower() != "scratch" and Choice2.lower() != "rest":
      print("It did nothing...")
    time.sleep(0.25)
    if HP2 <= 0:
      print(Choice3, "was defeated!")
      time.sleep(0.25)
      print("Victory!")
      quit()
    P1 = random.randint(1,3)
    if P2 == 1:
      DMG2 = random.randint(15,25)
    if P2 == 2:
      DMG2 = random.randint(25,32)
    if P2 == 3:
      DMG2 = random.randint(20,28)
    if P1 > 1:
      time.sleep(0.25)
      print(Choice3, "used", Choice4)
      HP = HP - DMG2
      time.sleep(0.25)
      print(Choice,"'s HP is now", HP)
    if HP <= 0:
      print(Choice, "was defeated!")
      time.sleep(0.25)
      print("Defeat!")
      quit()
    elif P1 < 2:
      DEF2 = random.randint(10,20)
      time.sleep(0.25)
      print(Choice3, "used", C5)
      time.sleep(0.25)
      HP2 = HP2 + DEF2
      print(Choice3,"'s HP is now", HP2)