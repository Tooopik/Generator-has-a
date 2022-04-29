# %%
from random import randrange


def letter_position(passwordList, lettersList):
    idx = 0
    letterPos = []
    for char in passwordList:
        idx += 1
        if char in lettersList:
            letterPos.append(idx - 1)
    return letterPos


def char_factor(letterPos, chatFactor):
    factor = int(len(letterPos)/chatFactor)
    if factor == 0:
        factor = 1
    return factor


def final_message(passwordList):
    password = ""
    for char in passwordList:
        password += str(char)
    print('\n')
    print(f'Your new password: {password}')
    print('\n')


# Wspólczynik występowania  dodatkowych znaków (im wyższy tym mniej znaków)
specCharFactor = 4
numberFactor = 6
upperCharFactor = 5


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
specChars = ['!', '@', '#', '$', '%', '^', '&', '*']
passwordlist = []


print('How long should the password be?')
long = int(input('>>> '))
print('Do you want big letters? (y/N)')
upperChar = input('>>> ')
print('Do you want numbers? (y/N)')
number = input('>>> ')
print('Do you want special characters? (y/N)')
specChar = input('>>> ')

# Buduje hasło z zadanej ilości znaków
for i in range(0, long):
    passwordlist.append(letters[randrange(0, len(letters))])

# Dodaje znaki specjalne
if specChar == 'y':
    factor = char_factor(letter_position(
        passwordlist, letters), specCharFactor)

    for char in range(0, factor):
        passwordlist[randrange(0, len(passwordlist))
                     ] = specChars[randrange(0, len(specChars))]

# Dodaje cyfry
if number == 'y':
    pos = 0
    letterPos = letter_position(passwordlist, letters)
    factor = char_factor(letterPos, numberFactor)

    for char in range(0, factor):
        pos = letterPos[randrange(0, len(letterPos))]
        passwordlist[pos] = str(numbers[randrange(0, len(numbers))])

# Zmienia litery na wielkie
if upperChar == 'y':
    pos = 0
    letterPos = letter_position(passwordlist, letters)
    factor = char_factor(letterPos, upperCharFactor)

    for char in range(0, factor):
        pos = letterPos[randrange(0, len(letterPos))]
        passwordlist[pos] = passwordlist[pos].upper()

final_message(passwordlist)


# %%
