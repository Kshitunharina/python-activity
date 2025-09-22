# “Algorithm” basically means a step‑by‑step set of instructions to solve a problem or do a task.
# 1. Flowchart
# Definition:
# A flowchart is a picture or diagram which shows steps of a process or logic using symbols (like boxes, diamonds) and arrows. It helps us plan the program.

# 2. Platform Introduction
# Definition:
# “Platform” means the place where we write and run code: for example VSCode, Python interpreter, the computer/operating system.

# 3. Welcome to the world of Coding
# Definition:
# Coding is writing instructions (in a programming language) that tell computers what to do. We learn about logic, data, decisions, etc.

# 4. Understanding the variables
# Definition:
# A variable is a container that holds a value. You can store something in it (like a number or text) and later change it.

# 5. Keywords
# Definition:
# Keywords are special reserved words in a programming language that already have a meaning. You cannot use them as variable names.

# 6. Data Types
# Definition:
# Data type means what kind of data we store. Examples: integer (whole numbers), float (decimal numbers), string (text), boolean (True or False).

# 7. Typecasting
# Definition:
# Changing data from one type to another. For example, converting a number stored as text into an integer, or integer to float, etc.

# 8. String Operation
# Definition:
# Operations or actions we do on text (strings), like joining, slicing, getting length, finding a part, etc.

# 9. String Concatenation
# Definition:
# Joining two or more strings (text) together. Example: "Hello" + "World" gives "HelloWorld".

# 10. Average
# Code:
a = 10
b = 20
c = 30
average = (a + b + c) / 3
print("Average of", a, b, c, "is", average)

# 11. Count the Notes
# Code (assuming currency notes of 100, 50, 20, 10, 5, 1):
amount = 237
notes_100 = amount // 100
amount = amount - notes_100 * 100
notes_50 = amount // 50
amount = amount - notes_50 * 50
notes_20 = amount // 20
amount = amount - notes_20 * 20
notes_10 = amount // 10
amount = amount - notes_10 * 10
notes_5 = amount // 5
amount = amount - notes_5 * 5
notes_1 = amount  
print("100‑notes:", notes_100, "50‑notes:", notes_50, "20‑notes:", notes_20, "10‑notes:", notes_10, "5‑notes:", notes_5, "1‑notes:", notes_1)

# 12. Percentage Calculation
# Code:
obtained_marks = 45
total_marks = 50
percentage = (obtained_marks / total_marks) * 100
print("Percentage:", percentage, "%")

# 13. Convert These Days
# Code (convert days into years, months, days. assume 1 year = 365 days, 1 month = 30 days):
days = 400
years = days // 365
days = days - years * 365
months = days // 30
days = days - months * 30
print("400 days is", years, "year(s),", months, "month(s),", days, "day(s)")

# 14. Conditional Statements
# Definition:
# Conditional statements are used to make decisions in code. If something is true, do something. else, do something else.

# 15. Profit Loss
# Code:
cost_price = 100
selling_price = 120
if selling_price > cost_price:
    print("Profit")
elif selling_price < cost_price:
    print("Loss")
else:
    print("No profit, no loss")

# 16. Checking the number greater or smaller
# Code:
x = 15
y = 20
if x > y:
    print(x, "is greater than", y)
elif x < y:
    print(x, "is smaller than", y)
else:
    print(x, "is equal to", y)

# 17. Odd Even
# Code:
n = 7
if n % 2 == 0:
    print(n, "is Even")
else:
    print(n, "is Odd")

# 18. And ‑ Or Operator
# Definition:
# and and or are logical operators.  
# and means both conditions must be true.  
# or means at least one of the conditions is true.

# example code:
age = 18
has_id = True
if age >= 18 and has_id:
    print("Allowed")
if age >= 18 or has_id:
    print("One of conditions true")

# 19. Not Equal Operator
# Definition:
# != is used to check if two values are not equal. If they are different, it is true; if same, it is false.

# Code example:
a = 10
b = 20
if a != b:
    print(a, "is not equal to", b)
else:
    print(a, "is equal to", b)

# 20. BMI Checker
# Code:
weight_kg = 70
height_m = 1.75
# BMI formula: weight / (height * height)
bmi = weight_kg / (height_m * height_m)
print("BMI is", bmi)
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")

# 21. Leap Year
# Code:
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

# 22. Fire Brigade
# Definition:
# Suppose we have smoke level and temperature readings. if either is too high, we alert for fire brigade.

# Code example:
smoke_level = 6   # scale maybe 1‑10
temperature = 70  # in degree (whatever unit we choose)
if smoke_level > 5 or temperature > 60:
    print("Alert! Call Fire Brigade")
else:
    print("All clear, no alert")


# Module - 18 activities


print("--- Exam Eligibility Check ---")
attended = 80
total_classes = 100
percentage = (attended / total_classes) * 100
if percentage >= 75:
    print("Eligible for Exam")
else:
    print("Not Eligible for Exam")

print("\n--- Electricity Bill ---")
units = 250
bill = 0
if units <= 100:
    bill = units * 1.5
elif units <= 200:
    bill = 100 * 1.5 + (units - 100) * 2.5
else:
    bill = 100 * 1.5 + 100 * 2.5 + (units - 200) * 4
print("Electricity Bill:", bill)

print("\n--- Customize Your Ride ---")
choice = 2
if choice == 1:
    print("You chose Bike")
elif choice == 2:
    print("You chose Car")
elif choice == 3:
    print("You chose Scooter")
else:
    print("Invalid Choice")

print("\n--- Check the Character ---")
ch = 'A'
if ch.isalpha():
    print("Alphabet")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Character")

print("\n--- Older One ---")
age1 = 25
age2 = 30
if age1 > age2:
    print("First person is older")
else:
    print("Second person is older")

print("\n--- Sum of Whole Numbers ---")
n = 10
sum_whole = 0
for i in range(n + 1):
    sum_whole += i
print("Sum of 0 to", n, "is", sum_whole)

print("\n--- Reverse a String ---")
s = "Hello"
rev_s = ""
for i in range(len(s)-1, -1, -1):
    rev_s += s[i]
print("Reversed String:", rev_s)

print("\n--- Reverse Order ---")
numbers = [1, 2, 3, 4, 5]
rev_numbers = []
for i in range(len(numbers)-1, -1, -1):
    rev_numbers.append(numbers[i])
print("Reversed List:", rev_numbers)

print("\n--- Prominent Word ---")
sentence = "apple banana apple orange banana apple"
words = sentence.split()
freq = {}
for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1
max_count = 0
prominent = ''
for w in freq:
    if freq[w] > max_count:
        max_count = freq[w]
        prominent = w
print("Most frequent word:", prominent)

print("\n--- Number of Words ---")
sentence2 = "This is a simple sentence"
count_words = 0
for w in sentence2.split():
    count_words += 1
print("Number of words:", count_words)

print("\n--- Sum of Natural Numbers ---")
nat_n = 10
sum_nat = 0
for i in range(1, nat_n + 1):
    sum_nat += i
print("Sum of natural numbers:", sum_nat)

print("\n--- Infinity (First 20 numbers as example) ---")
i = 0
while i < 20:
    print(i, end=" ")
    i += 1
print()

print("\n--- Armstrong Number ---")
num = 153
sum_arm = 0
for digit in str(num):
    sum_arm += int(digit) ** len(str(num))
if sum_arm == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

print("\n--- HCF ---")
a = 36
b = 60
while b != 0:
    temp = b
    b = a % b
    a = temp
print("HCF is", a)

print("\n--- Palindrome Number ---")
num_pal = 121
rev = 0
temp = num_pal
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10
if rev == num_pal:
    print(num_pal, "is Palindrome")
else:
    print(num_pal, "is not Palindrome")

print("\n--- Character Occurrence ---")
text = "hello world"
ch_occ = 'l'
count_ch = 0
for c in text:
    if c == ch_occ:
        count_ch += 1
print("Character", ch_occ, "occurs", count_ch, "times")

print("\n--- Is this a Prime Number ---")
prime_check = 29
is_prime = True
if prime_check < 2:
    is_prime = False
else:
    for i in range(2, int(prime_check ** 0.5) + 1):
        if prime_check % i == 0:
            is_prime = False
            break
if is_prime:
    print(prime_check, "is Prime")
else:
    print(prime_check, "is not Prime")

print("\n--- Mid Product ---")
a = 10
b = 20
print("Mid product:", (a * b) // 2)

print("\n--- Strong Number ---")
import math
strong_num = 145
sum_fact = 0
for d in str(strong_num):
    sum_fact += math.factorial(int(d))
if sum_fact == strong_num:
    print(strong_num, "is a Strong number")
else:
    print(strong_num, "is not a Strong number")

print("\n--- Decimal to Binary ---")
dec = 25
bin_str = ''
temp = dec
while temp > 0:
    bin_str = str(temp % 2) + bin_str
    temp //= 2
print("Binary:", bin_str)

print("\n--- Right Angle Triangle ---")
n = 5
for i in range(1, n+1):
    for j in range(i):
        print('*', end=' ')
    print()

print("\n--- Floyd's Triangle ---")
rows = 5
num = 1
for i in range(1, rows+1):
    for j in range(i):
        print(num, end=' ')
        num += 1
    print()

print("\n--- Diamond Pattern ---")
n = 5
for i in range(n):
    print(' '*(n-i-1) + '*'*(2*i+1))
for i in range(n-2, -1, -1):
    print(' '*(n-i-1) + '*'*(2*i+1))

print("\n--- Designer Doormat ---")
n = 7
m = n*3
for i in range(1, n, 2):
    print(('.|.'*i).center(m, '-'))
print('WELCOME'.center(m, '-'))
for i in range(n-2, 0, -2):
    print(('.|.'*i).center(m, '-'))

print("\n--- Polygon (Square) ---")
n = 5
for i in range(n):
    for j in range(n):
        print('*', end=' ')
    print()

print("\n--- Star Pattern ---")
n = 5
for i in range(1, n+1):
    print('*'*i)

print("\n--- Spiral Pattern (3x3) ---")
n = 3
matrix = [[0]*n for _ in range(n)]
left, right, top, bottom = 0, n-1, 0, n-1
num = 1
while left <= right and top <= bottom:
    for i in range(left, right+1):
        matrix[top][i] = num
        num += 1
    top += 1
    for i in range(top, bottom+1):
        matrix[i][right] = num
        num += 1
    right -= 1
    for i in range(right, left-1, -1):
        matrix[bottom][i] = num
        num += 1
    bottom -= 1
    for i in range(bottom, top-1, -1):
        matrix[i][left] = num
        num += 1
    left += 1
for row in matrix:
    print(' '.join(map(str,row)))