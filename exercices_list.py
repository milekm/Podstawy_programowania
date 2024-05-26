# Zad. 1
numbers_list = [4, 3, 1, 7, 3, 1, 64, 13, 1]
print(sum(numbers_list))

# Zad. 2
numbers_list = [7, 21, 4, 1, 6, 8]
result = numbers_list.pop(0)
for number in numbers_list:
    result *= number
print(result)

# Zad. 3
numbers_list = [17, 3, 1, 6, 7, 1, 54, 2, 3, 77, 5, 21]
largest_number = numbers_list.pop(0)
for number in numbers_list:
    if number > largest_number:
        largest_number = number
print(largest_number)


# Zad. 4
numbers_list = [4, 1, 56, 4, 6, 2, 1, 6, 7, -3, 56, 3, 1, 0]
smallest_number = numbers_list.pop(0)
for number in numbers_list:
    if number < smallest_number:
        smallest_number = number
print(smallest_number)

# Zad. 5
letters_list = ["e", "x", "a", "m", "p", "l", "e"]
string = "".join(letters_list)
print(string)

# Zad. 6
numbers_list = [5, 3, 1, 7, 8, 10]
print(numbers_list.index(7))

# Zad. 7
a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)
print(dup_items)

# Zad. 8
l = []
if not l:
    print("Lista jest pusta")

# Zad. 9
def clone_list_function(o_list: list):
    cloned_list = o_list.copy()
    return cloned_list
example_list = [3, 56, 2, 1, 5, 7, 2, 1, 6, 9]
print(clone_list_function(example_list))

# Zad. 10
strings_list = ["słoń", "niedźwiedź", "niebieski", "czerwony", "warszawiak"]
words_list = []
min_word_length = 8
for word in strings_list:
    word_length = len(word)
    if word_length > min_word_length:
        words_list.append(word)
print(words_list)

# Zad. 11
def common_data(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
    return result
print(common_data([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))
print(common_data([1, 2, 3, 4, 5], [6, 7, 8, 9]))

# Zad. 12
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i, x) in enumerate(color) if i not in (0, 4, 5)]
print(color)

# Zad. 13
array = [[['*' for col in range(6)] for col in range(4)] for row in range(3)]
print(array)

# Zad. 14
numbers_list = [4, 21, 5, 67, 2, 5, 8, 5, 1]
numbers_without_even = []
for number in numbers_list:
    if number % 2 != 0:
        numbers_without_even.append(number)
print(numbers_without_even)

# Zad. 15
from random import shuffle
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
shuffle(color)
print(color)

# Zad. 16
numbers_squares = []
for i in range(1, 31):
    numbers_squares.append(i ** 2)
first_five_numbers = numbers_squares[:5]
last_five_numbers = numbers_squares[-5:]
print("Pierwsze pięć liczb: {}".format(first_five_numbers))
print("Ostatnie pięć liczb: {}".format(last_five_numbers))

# Zad. 17
from random import choice
fruits_list = ["apple", "banana", "pineapple", "coconut", "cucumber"]
print(choice(fruits_list))

# Zad. 18
from itertools import permutations
numbers_list = [6, 2, 1, 8, 9, 10]
print(list(permutations(numbers_list)))

# Zad. 19
nums = [5, 15, 35, 8, 98]
for num_index, num_val in enumerate(nums):
    print(num_index, num_val)

# Zad. 20
list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]
print('Compare list1 and list2')
print(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))
print('Compare list1 and list3')
print(' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2)))