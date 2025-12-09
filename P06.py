word_dict = {
    1: ["a", "b", "c"],
    2: ["k", "l", "m"],
    3: ["x", "y", "z"]
}

with open("password.txt", "r") as file:
    saved_password = file.read().strip()

attempts = 0
found = False

for p in word_dict[1]:
    for q in word_dict[2]:
        for r in word_dict[3]:
            guess = p+q+r
            attempts += 1
            if guess == saved_password:
                print("Password cracked", guess)
                print("attempts:", attempts)
                found = True
                break
            if found:
                break
        if found:
            break

if found == False:
    print("nomath found")
