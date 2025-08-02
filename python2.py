# Task 1: Print your name and favorite programming language
print("\n--- Task 1: Name and Favorite Language ---")
name = input("Enter your name: ")
language = input("Enter your favorite programming language: ")
print(f"Hello {name}, you love {language}!")

# Task 2: Add two numbers
print("\n--- Task 2: Add Two Numbers ---")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", a + b)

# Task 3: Even or Odd
print("\n--- Task 3: Even or Odd ---")
num = int(input("Enter a number: "))
print("Even" if num % 2 == 0 else "Odd")

# Task 4: Largest of Two Numbers
print("\n--- Task 4: Largest of Two Numbers ---")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Largest number is", a if a > b else b)

# Task 5: Print Numbers from 1 to 10
print("\n--- Task 5: Numbers from 1 to 10 ---")
for i in range(1, 11):
    print(i, end=" ")
print()

# Task 6: Reverse a String
print("\n--- Task 6: Reverse a String ---")
s = input("Enter a string: ")
print("Reversed string:", s[::-1])

# Task 7: Square of a Number
print("\n--- Task 7: Square of a Number ---")
num = int(input("Enter a number: "))
print("Square:", num ** 2)

# Task 8: Greet Based on Time
print("\n--- Task 8: Greet Based on Time ---")
hour = int(input("Enter current hour (0-23): "))
if 5 <= hour < 12:
    print("Good Morning!")
elif 12 <= hour < 17:
    print("Good Afternoon!")
elif 17 <= hour < 21:
    print("Good Evening!")
else:
    print("Good Night!")

# Task 9: Check Positive, Negative, or Zero
print("\n--- Task 9: Positive, Negative or Zero ---")
num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Task 10: Count Characters in a String
print("\n--- Task 10: Count Characters in a String ---")
s = input("Enter a string: ")
print("Length of string:", len(s))
