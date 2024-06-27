try:
    filepath = input("Podaj ścieżkę do pliku: ")
    with open(filepath, "r") as f:
        content = f.read()

    print(f"Zawartość pliku: {content}")
except FileNotFoundError:
    print("Błąd: Plik nieznaleziony")
