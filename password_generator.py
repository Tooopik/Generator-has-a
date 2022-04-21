# %%
import random

# Wspólczynik występowania  dodatkowych znaków (im wyższy tym mniej znaków)
specCharFactor = 4
numberFactor = 6
upperCharFactor = 5


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
specChars = ['!', '@', '#', '$', '%', '^', '&', '*']
passwordlist = []
password = ''
letterPos = []
pos = 0
factor = 0

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
    passwordlist.append(letters[random.randrange(0, len(letters))])

# Dodaje znaki specjalne
if specChar == 'y':
    idx = 0
    pos = 0
    letterPos = []
    for char in passwordlist:
        idx += 1
        if char in letters:
            letterPos.append(idx - 1)

    factor = int(len(letterPos)/specCharFactor)
    if factor == 0:
        factor = 1

    for char in range(0, factor):
        passwordlist[random.randrange(
            0, len(passwordlist))] = specChars[random.randrange(0, len(specChars))]

# Dodaje cyfry
if number == 'y':
    idx = 0
    pos = 0
    letterPos = []
    for char in passwordlist:
        idx += 1
        if char in letters:
            letterPos.append(idx - 1)

    factor = int(len(letterPos)/numberFactor)
    if factor == 0:
        factor = 1

    for char in range(0, factor):
        pos = letterPos[random.randrange(0, len(letterPos))]
        passwordlist[pos] = str(numbers[random.randrange(0, len(numbers))])

# Zmienia litery na wielkie
if upperChar == 'y':
    idx = 0
    pos = 0
    letterPos = []
    for char in passwordlist:
        idx += 1
        if char in letters:
            letterPos.append(idx - 1)

    factor = int(len(letterPos)/upperCharFactor)
    if factor == 0:
        factor = 1

    for char in range(0, factor):
        pos = letterPos[random.randrange(0, len(letterPos))]
        passwordlist[pos] = passwordlist[pos].upper()


for char in passwordlist:
    password += str(char)
print('\n')
print(f'Your new password: {password}')
print('\n')

# %%
