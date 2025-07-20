import math

print("Square root of 25:", math.sqrt(25))
print("Ceil of 3.2:", math.ceil(3.2))
print("Factorial of 5:", math.factorial(5))
print("Sin(90°):", math.sin(math.radians(90)))
print("π value:",math.cos( math.pi/3))
print(math.radians(60))

print('==================')
import random

print("Random float 0-1:", random.random())
print("Random int 1-10:", random.randint(1, 10))
print("Random float 1.5–5.5:", random.uniform(1.5, 5.5))
print("Random choice from list:", random.choice(['apple', 'banana', 'cherry']))

items = [10, 20, 30, 40]
random.shuffle(items)
print("Shuffled list:", items)