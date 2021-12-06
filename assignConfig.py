import random
from random import randrange
import json
import os
imagesPath = './result'
configPath = './config'
imageFiles = os.listdir(imagesPath)
configFiles = os.listdir(configPath)

random.shuffle(imageFiles)
lastConfig = len(configFiles)

class Config:
    id = 0
    name = ''
    image = ''
    gen = 0
    description = 'Nokai, creatures born from the dark energy stocked in the heart of a BlackHole.'
    def __init__(self, id, name, image):
        self.id = id
        self.name = name
        self.image = image
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

def configFromJson(data):
     return json.loads(data, object_hook=lambda d: Config(**d))

configs = []
god = ["god1","Thedyo", "Ranthshee", "Fophu","Boro", "Daldro", "Terchell", "Rimonn", "Banya", "god9"]


def configExist(file):
    for config in configs:
        if config.file == file:
            return True
    return False

for index, file in enumerate(configFiles):
    with open(f'{configPath}/{file}', 'r', encoding="utf8") as my_file:
        configs.append(configFromJson(my_file.read()))

## Create config for Gods
position = 1
for name in god:
    file = name + ".png"
    if configExist(file) == False:
        config = Config(position, file.replace('.png', ''), file)
        with open(f'config/{position}.json', 'w', encoding="utf8") as my_file:
            my_file.write(config.toJson())
            position += 1
    else :
        print(f'Config already exist for {file}')


## Create config for Nokai
position = lastConfig if lastConfig > 10 else 11
for index, file in enumerate(imageFiles):
    if configExist(file) == False:
        config = Config(position, file.replace('.png', ''), file)
        with open(f'config/{position}.json', 'w', encoding="utf8") as my_file:
            my_file.write(config.toJson())
            position += 1
    else :
        print(f'Config already exist for {file}')


