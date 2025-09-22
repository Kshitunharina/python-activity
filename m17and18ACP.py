
print("--- Odd or Even Flowchart ---")
num = 15
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

print("\n--- Storing Birthdays ---")
birthdays = {"Alice": "01-01", "Bob": "12-12", "Charlie": "05-07"}
for name in birthdays:
    print(name, "birthday is on", birthdays[name])

print("\n--- Congratulations Message ---")
students = ["Alice", "Bob", "Charlie"]
scores = [95, 80, 70]
for i in range(len(students)):
    if scores[i] >= 90:
        print("Congratulations", students[i], "on scoring", scores[i])
    else:
        print("Good effort", students[i], "- score:", scores[i])

print("\n--- Square Root ---")
numbers = [4, 16, 25, 10]
for num in numbers:
    sqrt = 0
    i = 1
    while i*i <= num:
        sqrt = i
        i += 1
    print("Approximate square root of", num, "is", sqrt)

print("\n--- Summer Times (Sum of 1 to N) ---")
n = 10
sum_total = 0
for i in range(1, n+1):
    sum_total += i
print("Sum of 1 to", n, "is", sum_total)

print("\n--- Checking Alphabets ---")
chars = ['a', 'G', '1', '#']
for ch in chars:
    if ch.isalpha():
        print(ch, "is an Alphabet")
    elif ch.isdigit():
        print(ch, "is a Digit")
    else:
        print(ch, "is a Special Character")



print("--- Check Age ---")
age = 20
if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")

print("\n--- Power Calculator ---")
base = 2
exponent = 5
result = 1
for i in range(exponent):
    result *= base
print(base, "raised to the power", exponent, "is", result)

print("\n--- Reverse Order ---")
numbers = [10, 20, 30, 40, 50]
for i in range(len(numbers)-1, -1, -1):
    print(numbers[i], end=' ')
print()

print("\n--- Binary Conversion ---")
dec = 19
binary = ''
temp = dec
while temp > 0:
    binary = str(temp % 2) + binary
    temp //= 2
print("Binary of", dec, "is", binary)

print("\n--- Mirrored Triangle ---")
n = 5
for i in range(1, n+1):
    for j in range(n-i):
        print(' ', end='')
    for k in range(i):
        print('*', end='')
    print()

print("\n--- Square Pattern ---")
n = 5
for i in range(n):
    for j in range(n):
        print('*', end=' ')
    print()
        