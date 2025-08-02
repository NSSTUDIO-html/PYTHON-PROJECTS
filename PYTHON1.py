name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Hello {name}, you are {age} years old.")

a = int(input("Enter a: "))
b = int(input("Enter b: "))
a, b = b, a
print("After swapping:", "a =", a, "b =", b)

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")

num = int(input("Enter a number: "))
print("Even" if num % 2 == 0 else "Odd")

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
print("Largest:", max(a, b, c))

num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")

n = int(input("Enter number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

n = int(input("How many terms? "))
a, b = 0, 1
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b

n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial:", fact)
