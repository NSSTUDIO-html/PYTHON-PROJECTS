import math

print(math.sqrt(16))        # 4.0
print(math.factorial(5))    # 120
print(math.pi)              # 3.141592653589793

import random

print(random.randint(1, 10))          # Random int between 1 and 10
print(random.choice(['A', 'B', 'C'])) # Random choice from list

import datetime

now = datetime.datetime.now()
print(now)                            # Current date and time
print(now.strftime("%Y-%m-%d"))       # Format date

import os

print(os.getcwd())      # Get current working directory
print(os.listdir())     # List files and folders

import sys

print(sys.version)       # Python version
print(sys.platform)      # Platform name

import time
for _ in range(10):
 print("Start")
 time.sleep(2)            # Wait for 2 seconds
print