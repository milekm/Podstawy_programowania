# Zad. 1
import operator
dictionary = {3: 6, 51: 23, 18: 41, 45: 19, 37: 29, 1: 2, 2: 5, 9: 0, 0: 1}
print("Słownik: {}".format(dictionary))
sorted_asc = dict(sorted(dictionary.items(), key=operator.itemgetter(1)))
print("W kolejności rosnącej: {}".format(sorted_asc))
sorted_desc = dict(sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True))
print("W kolejności malejącej: {}".format(sorted_desc))

# Zad. 2
ex_dict = {0: 1, 1: 2}
print("Słownik: {}".format(ex_dict))
ex_dict.update({2: 3})
print("Słownik po dodaniu wartości: {}".format(ex_dict))

# Zad. 3
ex_dict_1 = {1: 23, 64: 25}
ex_dict_2 = {7: 21, 2: 11}
ex_dict_3 = {91: 290, 10: 85}
dict_4 = {}
for dictionary in (ex_dict_1, ex_dict_2, ex_dict_3):
    dict_4.update(dictionary)
print(dict_4)

# Zad. 4
ex_dict = {19: 230, 12: 210, 3: 456}
print("Wpisz klucz:")
key = input()
key = int(key)
if key in ex_dict.keys():
    print("Klucz {} znajduje się w słowniku".format(key))
elif key not in ex_dict.keys():
    print("Klucz {} nie znajduje się w słowniku".format(key))

# Zad. 5
ex_dict = {"a": 68, "b": 1, "c": 4}
for key, value in ex_dict.items():
    print("{0} -> {1}".format(key, value))

# Zad. 6
print("Wpisz liczbę")
n = input()
n = int(n)
dict_n = {}
i = n + 1
for n in range(1, n + 1):
    dict_n[n] = n ** 2
print(dict_n)

# Zad. 7
d = {}
for n in range(1, 16):
    d[n] = n ** 2
print(d)

# Zad. 8
ex_dict_1 = {"x": 1, "y": 2}
ex_dict_2 = {"z": 3, "a": 4}
connected_dict = ex_dict_1.copy()
connected_dict.update(ex_dict_2)
print(connected_dict)

# Zad. 9
d = {"żółty": 5, "brązowy": 7, "pomarańczowy": 1}
for color_key, value in d.items():
    print("{0} odpowiada {1}".format(color_key, d[color_key]))

# Zad. 10
ex_dict = {0: 8, 1: 1, 2: 4}
result = 1
for value in ex_dict.values():
    result *= value
print(result)

# Zad. 11
ex_dict = {"x": 3, "y": 10, "z": 1}
print("Wpisz klucz")
key = input()
print("Słownik: {}".format(ex_dict))
if key in ex_dict.keys():
    del ex_dict[key]
    print("Klucz został usunięty!\n"
          "Słownik po usunięciu klucza: {}".format(ex_dict))
elif key not in ex_dict.keys():
    print("Słownik nie posiada takiego klucza")

# Zad. 12
keys = ["a", "b", "c", "d", "e", "f", "g"]
values = [7, 3, 1, 6, 2, 9, 0]
dictionary = {}
i = 0
while i < len(keys):
    key = keys[i]
    value = values[i]
    dictionary.update({key: value})
    i += 1
print(dictionary)

# Zad. 13
dictionary = {"c": 5, "l": 2, "z": 7, "a": 15, "b": 3}
sorted_dictionary_keys = sorted(dictionary.keys())
sorted_dictionary_values = sorted(dictionary.values())
for key in sorted_dictionary_keys:
    index = sorted_dictionary_keys.index(key)
    value = sorted_dictionary_values[index]
    print("{0}: {1}".format(key, value))

# Zad. 14
dictionary = {0: 6, 1: 1, 2: 9, 3: 3, 4: 2, 5: 1, 6: 98, 7: 24, 8: 1, 9: 28}
max_value = max(dictionary.values())
min_value = min(dictionary.values())
print(
      "Wartość największa: {}\n".format(max_value),
      "Wartość najmniejsza: {}".format(min_value),
)

# Zad. 15
class ExDictionary:
    def __init__(self):
        self.x = "Paweł"
        self.y = "Bożydar"
        self.z = "Adam"
ex_dictionary = ExDictionary()
print(ex_dictionary.__dict__)

# Zad. 16
ex_dictionary = {1: 5, 2: 21, 3: 14, 4: 15, 5: 7, 6: 5, 7: 9, 8: 5}
dictionary = {}
for key, value in ex_dictionary.items():
    if value not in dictionary.values():
        dictionary[key] = value
print("Słownik: {0}\n".format(ex_dictionary),
      "Słownik po wyczyszczeniu: {0}".format(dictionary))

# Zad. 17
dictionary = {}
if not bool(dictionary):
    print("Słownik jest pusty")

# Zad. 18
dictionary_1 = {"a": 1, "b": 2, "c": 3}
dictionary_2 = {"a": 3, "b": 6, "d": 9}
keys = dictionary_1.keys()
values_dictionary_1 = list(dictionary_1.values())
values_dictionary_2 = list(dictionary_2.values())
sum_dictionary = {}
for i, key in enumerate(dictionary_1.keys()):
    sum_dictionary[key] = values_dictionary_1[i] + values_dictionary_2[i]
print(sum_dictionary)

# Zad. 19
dict_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
print("Lista: ", dict_list)
u_value = set(val for dic in dict_list for val in dic.values())
print("Unikalne wartości: ", u_value)

# Zad. 20
import itertools
d = {'1': ['a', 'b'], '2': ['c', 'd']}
for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    print(''.join(combo))