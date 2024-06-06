import math
import time
import random
print("Welcome to Pythomon!")
time.sleep(0.5)
print("Choose your Pythomon!")
time.sleep(0.25)
print("1. Chonkers")
time.sleep(0.25)
Choice = input("Type here ")
print("Go,", Choice,"!")
time.sleep(0.25)
print("Opponent sent out Willow!")
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