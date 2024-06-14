# Zad. 1
print("Podaj pierwsza liczbę\n")
a = input()
a = float(a)
print("Podaj drugą liczbę\n")
b = input()
b = float(b)
average = (a + b) / 2
print("Średnia: {}".format(average))

# Zad. 2
print("Podaj długość boku\n")
a = input()
a = float(a)
square_area = a * a
print("Pole kwadratu wynosi: {}".format(square_area))

# Zad. 3
import random


dice = random.randint(1, 6)
print("Wynik rzutu: {}".format(dice))

# Zad. 4
counter = 0
for i in range(1, 10):
    print("Podaj liczbę\n")
    number = input()
    number = int(number)
    if number % 2 == 0:
        counter += 1

print("Licznik liczb parzystych: {}".format(counter))

# Zad. 5
numbers_counter = 0
numbers_sum = 0
while numbers_sum < 100:
    print("Podaj liczbę\n")
    number = input()
    number = int(number)
    numbers_sum += number
    numbers_counter += 1

print("Wprowadzono {} liczb".format(numbers_counter))

# Zad. 6
counter = 0
num_list = []
for i in range(1, 10):
    print("Podaj liczbę\n")
    number = input()
    number = int(number)
    if number % 2 == 0:
        counter += 1
    num_list.append(number)

print("Licznik liczb parzystych: {}\n"
      "{}".format(counter, num_list))

# Zad. 7
import random

print("Wprowadź liczbę\n")
n = input()
n = int(n)
i = 0
num_list = []
while i < n:
    number = random.randint(1, 50)
    if not 11 < number < 21:
        num_list.append(number)
    i += 1

print(num_list)
