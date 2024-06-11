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
HP2 = 100
time.sleep(0.25)
print("Select a move!", "Attack or Defend!")
Choice2 = input()
time.sleep(0.25)
print(Choice, "used", Choice2)
if Choice2 == "Attack":
  DMG = random.randint(15,30)
  HP2 = HP2 - DMG
  print("Willow's HP is now", HP2)
elif Choice2 == "Defend":
  DEF = random.randint(10,20)
  HP = HP + DEF
  print(Choice,"'s HP is now", HP)
time.sleep(0.25)
P1 = random.randint(1,2)
DMG2 = random.randint(15,30)
if P1 > 1:
  time.sleep(0.25)
  print("Willow used Attack")
  HP = HP - DMG2
  time.sleep(0.25)
  print(Choice,"'s HP is now", HP)
elif P1 < 2:
  DEF2 = random.randint(10,20)
  time.sleep(0.25)
  print("Willow used Defend")
  time.sleep(0.25)
  HP2 = HP2 + DEF2
  print("Willows's HP is now", HP2)
if HP <= 0:
  print(Choice, "was defeated!")
  time.sleep(0.25)
  print("Defeat!")
if HP2 <= 0:
  print("Willow was defeated!")
  time.sleep(0.25)
  print("Victory!")