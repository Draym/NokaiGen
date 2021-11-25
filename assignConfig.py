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
    def __init__(self, id, name, image):
        self.id = id
        self.name = name
        self.image = image
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

def configFromJson(data):
     return json.loads(data, object_hook=lambda d: Config(**d))

configs = []

def configExist(file):
    for config in configs:
        if config.id == id:
            return True
    return False

for index, file in enumerate(configFiles):
    with open(f'{configPath}/{file}', 'r', encoding="utf8") as my_file:
        configs.append(configFromJson(my_file.read()))

position = lastConfig
for index, file in enumerate(imageFiles):
    if configExist(file) == False:
        config = Config(position, file.replace('.png', ''), file)
        with open(f'config/{position}.json', 'w', encoding="utf8") as my_file:
            my_file.write(config.toJson())
            position += 1
    else :
        print(f'Config already exist for {file}')


