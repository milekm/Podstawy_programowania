try:
    number = int(input("Podaj liczbę całkowitą: "))
    print(f"Wprowadzona wartość: {number}")
except ValueError:
    print("Nieprawidłowa wartość. Prawidłową wartością jest liczba całkowita")
