a = float(input("Wprowadź dzielną: "))
b = float(input("Wprowadź dzielnik: "))

try:
    print(f"Wynik działania {a} / {b} = {a / b}")
except ArithmeticError:
    print("BŁĄD: Wystąpił problem arytmetyczny")
