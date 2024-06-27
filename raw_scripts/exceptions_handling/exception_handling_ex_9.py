try:
    filepath = input("Podaj ścieżkę do pliku: ")
    encoding = input("Wprowadź kodowanie: ")
    with open(filepath, "r", encoding=encoding) as f:
        content = f.read()

    print(f"Zawartość pliku: {content}")
except UnicodeDecodeError:
    print("Błąd: Problem z kodowaniem podczas odczytywania pliku")
