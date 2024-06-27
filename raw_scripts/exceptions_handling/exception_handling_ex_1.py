a = 7
b = 0

try:
    print(f"Wynik działania {a} / {b} = {a / b}")
except ZeroDivisionError:
    print("Nie można dzielić przez zero!")
