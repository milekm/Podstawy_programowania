# Zad. 1
nl = []
for x in range(1500, 2701):
    if (x % 7 == 0) and (x % 5 == 0):
        nl.append(str(x))
print(','.join(nl))

# Zad. 2
temp = input("Input the temperature you like to convert? (e.g., 45F, 102C etc.) : ")
degree = int(temp[:-1])
i_convention = temp[-1]
if i_convention.upper() == "C":
    result = int(round((9 * degree) / 5 + 32))
    o_convention = "Fahrenheit"  # Set the output convention as Fahrenheit
elif i_convention.upper() == "F":
    result = int(round((degree - 32) * 5 / 9))
    o_convention = "Celsius"
else:
    print("Input proper convention.")
    quit()
print("The temperature in", o_convention, "is", result, "degrees.")

# Zad. 3
import random
generated_number = random.randint(1, 10)
i = 0
while i == 0:
    print("Podaj cyfrę od 1 do 9: ")
    number = input()
    number = int(number)
    if number == generated_number:
        print("Gratulacje, odgadnąłeś cyfrę")
        break

# Zad. 4
print("Podaj słowo")
word = input()
print("Słowo na odwrót: {}".format(''.join(reversed(word))))

# Zad. 5
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
count_odd = 0
count_even = 0
for x in numbers:
    if not x % 2:
        count_even += 1
    else:
        count_odd += 1
print("Number of even numbers:", count_even)
print("Number of odd numbers:", count_odd)

# Zad. 6
different_types_values_list = ["145", 6, (1, 5), [5, 7], {2: 4}, 4.5]
for item in different_types_values_list:
    print("{} jest typu {}".format(item, type(item)))

# Zad. 7
for x in range(6):
    if (x == 3 or x == 6):
        continue
    print(x, end=' ')
print("\n")

# Zad. 8
x = 0
y = 1
while y < 50:
    print(y)
    z = x + y
    x = y
    y = z

# Zad. 9
for fizzbuzz in range(51):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)

# Zad. 10
n = 5
for i in range(n):
    for j in range(i):
        print('* ', end="")
    print('')
for i in range(n, 0, -1):
    for j in range(i):
        print('* ', end="")
    print('')

# Zad. 11
row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]
for row in range(row_num):
    for col in range(col_num):
        multi_list[row][col] = row * col
print(multi_list)

# Zad. 12
import re

p = input("Input your password")
x = True
while x:
    if len(p) < 6 or len(p) > 12:
        break
    elif not re.search("[a-z]", p):
        break
    elif not re.search("[0-9]", p):
        break
    elif not re.search("[A-Z]", p):
        break
    elif not re.search("[$#@]", p):
        break
    elif re.search("\s", p):
        break
    else:
        print("Valid Password")
        x = False
        break
if x:
    print("Not a Valid Password")

# Zad. 13
string = input("Podaj zdanie: ")
chars = 0
digits = 0
for char in string:
    if char.isdigit():
        digits += 1
    elif char.isalpha():
        chars += 1
print("Chars: {}".format(chars))
print("Digits: {}".format(digits))

# Zad. 14
result_str = ""
for row in range(0, 7):
    for column in range(0, 7):
        if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):
            result_str = result_str + "*"
        else:
            result_str = result_str + " "
    result_str = result_str + "\n"
print(result_str)

# Zad. 15
year = int(input("Input your birth year: "))
if (year - 2000) % 12 == 0:
    sign = 'Dragon'
elif (year - 2000) % 12 == 1:
    sign = 'Snake'
elif (year - 2000) % 12 == 2:
    sign = 'Horse'
elif (year - 2000) % 12 == 3:
    sign = 'Sheep'
elif (year - 2000) % 12 == 4:
    sign = 'Monkey'
elif (year - 2000) % 12 == 5:
    sign = 'Rooster'
elif (year - 2000) % 12 == 6:
    sign = 'Dog'
elif (year - 2000) % 12 == 7:
    sign = 'Pig'
elif (year - 2000) % 12 == 8:
    sign = 'Rat'
elif (year - 2000) % 12 == 9:
    sign = 'Ox'
elif (year - 2000) % 12 == 10:
    sign = 'Tiger'
else:
    sign = 'Hare'
print("Your Zodiac sign :", sign)

# Zad. 16
a = float(input("Input first number: "))
b = float(input("Input second number: "))
c = float(input("Input third number: "))
if a > b:
    if a < c:
        median = a
    elif b > c:
        median = b
    else:
        median = c
else:
    if a > c:
        median = a
    elif b < c:
        median = b
    else:
        median = c
print("The median is", median)

# Zad. 17
print("Napisz literę")
letter = input()
if letter in ("a", "e", "i", "o", "u"):
    print("{} jest samogłoską".format(letter))
else:
    print("{} jest spółgłoską".format(letter))

# Zad. 18
import calendar
months_list = "Lista miesięcy: "
for month in calendar.month_name:
    months_list += "{} ".format(month)
print(months_list)
print("Wprowadź nazwę miesiąca spośród podanych ")
months_with_31_days = ("January", "March", "May", "July", "August", "October", "December")
months_with_30_days = ("April", "June", "September", "November")
month_name = input()
if month_name == "February":
    print("Liczba dni: 28/29")
elif month_name in months_with_31_days:
    print("Liczba dni: 31")
elif month_name in months_with_30_days:
    print("Liczba dni: 30")
else:
    print("Nieprawidłowa nazwa miesiąca")

# Zad. 19
x = input("Podaj pierwszą liczbę: ")
x = int(x)
y = input("Podaj drugą liczbę: ")
y = int(y)
result = x + y
if result in range(15, 20):
    result = 20
print(result)

# Zad. 20
for i in range(10):
    print(str(i) * i)