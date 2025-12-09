import random

word_dict = {
    1: ["a", "b", "c"],
    2: ["k", "l", "m"],
    3: ["x", "y", "z"]
}

list = []

for words in word_dict.values():
    index = random.randint(0,len(words)-1)
    list.append(words[index])

password = "".join(list)

print(password)

with open("password.txt", "w") as file:
    file.write(password)