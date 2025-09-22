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


