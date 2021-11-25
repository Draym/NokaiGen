names = []

with open('names.txt', 'r', encoding="utf8") as my_file:
    names = my_file.read().splitlines()

with open('names.txt', 'w', encoding="utf8") as my_file:
    max = len(names)
    for i in range(max):
        if i == max - 1:
            my_file.write(f"{names[i]}")
        else:
            my_file.write(f"{names[i]}\n")