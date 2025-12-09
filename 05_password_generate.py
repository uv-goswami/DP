import secrets

def generate_passphrase(filename, num_words=4):
    try:
        with open(filename, 'r') as file:
            words = [word.strip() for word in file.readlines()]
            
        if len(words) < num_words:
            return "Error: Not enough words in dictionary file."
            
        passphrase_words = [secrets.choice(words) for i in range(num_words)]
        return "-".join(passphrase_words)
        
    except FileNotFoundError:
        return "Error: File not found."

filename = "dictionary.txt"
try:
    with open(filename, "w") as f:
        f.write("correct\nhorse\nbattery\nstaple\nblue\nsky\nmountain\nriver\ncoffee\ncode\nsecure\nprivate\n")
except:
    pass

password = generate_passphrase(filename)
print("Generated Passphrase:", password)
