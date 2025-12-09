def encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, 26 - shift)

text = input("Enter Text: ")
s = int(input("Enter Shift Key: "))

cipher = encrypt(text, s)
print("Encrypted:", cipher)

original = decrypt(cipher, s)
print("Decrypted:", original)
