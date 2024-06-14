# Zad. 1
def get_the_highest_value(numbers: list):
    return max(numbers)


print(get_the_highest_value([3, 6, 2]))

# Zad. 2
def sum_list(numbers: list):
    return sum(numbers)


print(sum_list([8, 2, 3, 0, 7]))

# Zad. 3
def multiply_list(numbers: list):
    result = 1
    for number in numbers:
        result *= number

    return result


print(multiply_list([8, 2, 3, -1, 7]))

# Zad. 4
def reverse_string(string: str):
    reverse_str = ""
    for char in string:
        reverse_str = char + reverse_str

    return reverse_str

string = "Abecadło"
print("Oryginalne słowo {}".format(string))
print("Odwrócone słowo {}". format(reverse_string(string)))

# Zad. 5
def factorial(number: int):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


number = int(input("Podaj liczbę, aby wyliczyć silnię: "))
print(factorial(number))

# Zad. 6
def check_is_number_in_range(number: int):
    if number in range(2, 5):
        return True
    else:
        return False


number = 4
if check_is_number_in_range(number):
    print("Liczba {} znajduje się w przedziale".format(number))
else:
    print("Liczba {} nie znajduje się w przedziale".format(number))

# Zad. 7
def count_upper_and_lower_letters(string: str):
    counters = {
        "lower_case": 0,
        "upper_case": 0
    }

    for char in string:
        if char.islower():
            counters["lower_case"] += 1
        elif char.isupper():
            counters["upper_case"] += 1

    print(f"Podany ciąg znaków: {string}")
    print(f"Ilość małych znaków: {counters["lower_case"]}")
    print(f"Ilość dużych znaków: {counters["upper_case"]}")


count_upper_and_lower_letters("The quick Brown Fox")

# Zad. 8
# Define a function named 'unique_list' that takes a list 'l' as input and returns a list of unique elements
def unique_list(l):
    # Create an empty list 'x' to store unique elements
    x = []

    # Iterate through each element 'a' in the input list 'l'
    for a in l:
        # Check if the element 'a' is not already present in the list 'x'
        if a not in x:
            # If 'a' is not in 'x', add it to the list 'x'
            x.append(a)

    # Return the list 'x' containing unique elements
    return x


# Print the result of calling the 'unique_list' function with a list containing duplicate elements
print(unique_list([1, 2, 3, 3, 3, 3, 4, 5]))

# Zad. 9
def test_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2, n):
            if n % x == 0:
                return False
        return True


print(test_prime(9))

# Zad. 10
def get_even_numbers(numbers: list):
    even_list = []
    for number in numbers:
        if number % 2 == 0:
            even_list.append(number)

    return even_list


numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Oryginalna lista: {numbers_list}\n"
      f"Lista liczb parzystych: {get_even_numbers(numbers_list)}")

# Zad. 11
def perfect_number(n):
    sum = 0

    for x in range(1, n):
        if n % x == 0:
            sum += x

    return sum == n


print(perfect_number(6))

# Zad. 12
def is_palindrome(string):
    left_pos = 0
    right_pos = len(string) - 1

    while right_pos >= left_pos:
        if not string[left_pos] == string[right_pos]:
            return False

        left_pos += 1
        right_pos -= 1

    return True


print(is_palindrome('aza'))

# Zad. 13
def pascal_triangle(n):
    trow = [1]

    y = [0]

    for x in range(max(n, 0)):
        print(trow)

        trow = [l + r for l, r in zip(trow + y, y + trow)]

    return n >= 1


pascal_triangle(6)

# Zad. 14
import string


def is_pangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)

    str_set = set(str1.lower())

    return alphaset <= str_set


print(is_pangram('The quick brown fox jumps over the lazy dog'))

# Zad. 15
def sort_list(words_list: list):
    words_list.sort()

    return "-".join(words_list)


string = input("Podaj wyrazy przedzielone myślnikiem: ")
print(sort_list(list(string.split("-"))))

# Zad. 16
def squares_of_numbers():
    num_list = []

    for i in range(1, 31):
        num_list.append(i ** 2)

    return num_list


print(squares_of_numbers())

# Zad. 17
def make_bold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def make_italic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

def make_underline(fn):
    def wrapped():
        return "<u>" + fn() + "</u>"
    return wrapped

@make_bold
@make_italic
@make_underline
def hello():
    return "hello world"


print(hello())

# Zad. 18
mycode = 'print("hello world")'

code = """
def mutiply(x,y):
    return x*y

print('Multiply of 2 and 3 is: ',mutiply(2,3))
"""

exec(mycode)
exec(code)

# Zad. 19
def test(a):
    def add(b):
        nonlocal a

        a += 1

        return a + b

    return add


func = test(4)

print(func(4))

# Zad. 20
def abc():
    x = 1
    y = 2
    str1 = "w3resource"

    print("Python Exercises")


print(abc.__code__.co_nlocals)

# Zad. 21
from time import sleep
import math


def delay(fn, ms, *args):
    sleep(ms / 1000)

    return fn(*args)


print("Square root after specific milliseconds:")

print(delay(lambda x: math.sqrt(x), 100, 16))

print(delay(lambda x: math.sqrt(x), 1000, 100))

print(delay(lambda x: math.sqrt(x), 2000, 25100))
