try:
    filepath = input("Podaj ścieżkę do pliku: ")
    with open(filepath, "r") as f:
        content = f.read()

    print(f"Zawartość pliku: {content}")
except PermissionError:
    print("Błąd: Brak dostępu do pliku")
