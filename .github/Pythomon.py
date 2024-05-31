import math
import time
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
  
  print("Willow's HP is now", HP2 - 20)