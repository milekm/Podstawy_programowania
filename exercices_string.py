# Zad. 1
print("Podaj wyraz\n")
string = input()
string_length = len(string)
print(string_length)

# Zad. 2
def char_frequency(str1):
    dictionary = {}
    for n in str1:
        keys = dictionary.keys()
        if n in keys:
            dictionary[n] += 1
        else:
            dictionary[n] = 1
    return dictionary
print(char_frequency('google.com'))

# Zad. 3
def string_both_ends(str):
    if len(str) < 2:
        return ''
    return str[0:2] + str[-2:]
print(string_both_ends('w3resource'))
print(string_both_ends('w3'))
print(string_both_ends('w'))

# Zad. 4
def change_char(str1):
    char = str1[0]
    str1 = str1.replace(char, '$')
    str1 = char + str1[1:]
    return str1
print(change_char('restart'))

# Zad. 5
print("Podaj wyraz\n")
str_1 = input()
print("Podaj wyraz\n")
str_2 = input()
two_first_letters_str_1 = str_1[:2]
two_first_letters_str_2 = str_2[:2]
rest_of_the_str_1 = str_1[2:]
rest_of_the_str_2 = str_2[2:]
combined_string = "{}{} {}{}".format(two_first_letters_str_2, rest_of_the_str_1, two_first_letters_str_1,
                                     rest_of_the_str_2)
print(combined_string)

# Zad. 6
print("Podaj wyraz")
string = input()
string_length = len(string)
if string_length >= 3:
    last_three_letters = string[-3:0]
    if last_three_letters == "ing":
        string += "ly"
    else:
        string += "ing"
print(string)

# Zad. 7
def not_poor(str1):
    snot = str1.find('not')
    spoor = str1.find('poor')
    if spoor > snot and snot > 0 and spoor > 0:
        str1 = str1.replace(str1[snot:(spoor + 4)], 'good')
        return str1
    else:
        return str1
print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))

# Zad. 8
print("Podaj listę wyrazów\n")
words = input()
def the_longest_word_function(words: str):
    the_longest_word = ""
    words_list = words.split(",")
    for word in words_list:
        if the_longest_word == "":
            the_longest_word = word
        else:
            if len(word) > len(the_longest_word):
                the_longest_word = word
    return the_longest_word
the_longest_word = the_longest_word_function(words)
print("Najdłuższe słowo: {}\n".format(the_longest_word),
      "Liczba znaków najdłuższego słowa: {}".format(len(the_longest_word)))

# Zad. 9
print("Podaj wyraz")
word = input()
print("Podaj indeks litery w celu usunięcia ze słowa")
index = input()
index = int(index)
if len(word) != 0:
    word = list(word)
    del word[index]
    word = "".join(word)
else:
    print("Proszę wpisać słowo")
print(word)

# Zad. 10
def change_string(str1):
    return str1[-1:] + str1[1:-1] + str1[:1]
print(change_string('abcd'))
print(change_string('12345'))

# Zad. 11
print("Podaj wyraz")
word = input()
changed_word = ""
for i, letter in enumerate(word):
    if i % 2 == 0:
        changed_word += letter
print(changed_word)

# Zad. 12
def word_count(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
print(word_count('the quick brown fox jumps over the lazy dog.'))

# Zad. 13
print("Napisz wyraz")
word = input()
word_upper = word.upper()
word_lower = word.lower()
print("Słowo wielkimi literami: {}\n".format(word_upper),
      "Słowo małymi literami: {}".format(word_lower)
)

# Zad. 14
items = input("Input comma-separated sequence of words")
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))

# Zad. 15
x = 3.1415926
y = -12.9999
print()
print("Original Number: ", x)
print("Formatted Number with no decimal places: "+"{:.0f}".format(x))
print("Original Number: ", y)
print("Formatted Number with no decimal places: "+"{:.0f}".format(y))
print()

# Zad. 16
import string
alphabet_lowercase = string.ascii_lowercase
def encrypt(text: str, shift: int):
    result = ""
    text = text.lower()
    for char in text:
        try:
            char_index = alphabet_lowercase.index(char)
            result += alphabet_lowercase[(char_index + shift) % 26]
        except ValueError:
            result += " "
    return result
def decrypt(text: str, shift: int):
    return encrypt(text, -shift)
if __name__ == "__main__":
    def main_menu():
        while True:
            decision = input("SZYFR CEZARA\n"
                             "1 - Zaszyfruj wiadomość\n"
                             "2 - Odszyfruj wiadomość\n"
                             "3 - Odszyfruj wiadomość wszystkimi możliwymi kluczami\n"
                             "> ")
            if decision == "1":
                text = input("Podaj wiadomość (bez polskich znaków):\n")
                key = int(input("Podaj długość klucza: "))
                print("Wiadomość:\n" + encrypt(text, key))
            elif decision == "2":
                text = input("Podaj wiadomość (bez polskich znaków):\n")
                key = int(input("Podaj długość klucza: "))
                print("Wiadomość:\n" + decrypt(text, key))
            elif decision == "3":
                text = input("Podaj wiadomość (bez polskich znaków):\n")
                for key in range(0, 25):
                    print("Wiadomość:\n" + decrypt(text, key))
            else:
                print("Nieprawidłowa operacja!")
    main_menu()

# Zad. 17
def reverse_string_words(text):
    for line in text.split('\n'):
        return(' '.join(line.split()[::-1]))
print(reverse_string_words("The quick brown fox jumps over the lazy dog."))
print(reverse_string_words("Python Exercises."))

# Zad. 18
word = input("Podaj wyraz: ")
if len(word) >= 3:
    word = word[:3]
    print(word)
else:
    print("Słowo za krótkie. Minimalna długość to 3 znaki")

# Zad. 19
import collections
str1 = 'thequickbrownfoxjumpsoverthelazydog'
d = collections.defaultdict(int)
for c in str1:
    d[c] += 1
for c in sorted(d, key=d.get, reverse=True):
    if d[c] > 1:
        print('%s %d' % (c, d[c]))

# Zad. 20
print("Podaj wyraz")
word = input()
word_length = len(word)
if word_length % 4 == 0:
    word = "".join(reversed(word))
print(word)