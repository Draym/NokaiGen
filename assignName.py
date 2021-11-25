import random
from random import randrange

import os
path = './generator/generated'
files = os.listdir(path)

names = []

with open('names.txt', 'r', encoding="utf8") as my_file:
    names = my_file.read().splitlines()

names = list(set(names))
random.shuffle(names)

def getNameAndSave(file):
    try :
        namesLength = len(names)
        if namesLength > 0:
            nameIndex = randrange(namesLength)
            name = names[nameIndex]
            del names[nameIndex]
            os.rename(os.path.join(path, file), os.path.join('result', f'{name}.png'))
            return True
        else :
            print('No more names available')
            return False
    except :
        return getNameAndSave(file)

for index, file in enumerate(files):
    result = getNameAndSave(file)
    if result == False:
        break

with open('names.txt', 'w', encoding="utf8") as my_file:
    max = len(names)
    for i in range(max):
        if i == max - 1:
            my_file.write(f"{names[i]}")
        else:
            my_file.write(f"{names[i]}\n")