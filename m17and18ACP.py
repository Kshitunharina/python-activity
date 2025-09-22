
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