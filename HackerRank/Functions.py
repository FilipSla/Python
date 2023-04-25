import random as random


def is_leap(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)


# year = int(input("Zadej rok:"))
year = random.randrange(1000, 10**5 + 1)
print(year, is_leap(year))


def print_full_name(first, last):
    return print(f"Hello {first} {last}! You just delved into python!")


# first_name = input("Zadej křestní jméno:")
# last_name = input("Zadej příjmení:")
# print_full_name(first_name, last_name)


def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1 :]


newString = mutate_string("testing", 2, "k")
print(newString)


def count_substring(string, sub_string):
    ct = 0
    while sub_string in string:
        ct += 1
        string = string[string.find(sub_string) + 1 :]
    return ct


print(count_substring("ABCDCDC", "CDC"))
