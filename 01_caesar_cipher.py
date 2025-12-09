# Caesar Cipher Implementation in Python

def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypts or decrypts a text using Caesar Cipher.
    
    Parameters:
        text (str): The input text to encrypt or decrypt.
        shift (int): The number of positions to shift.
        mode (str): 'encrypt' or 'decrypt'.
    
    Returns:
        str: The resulting encrypted or decrypted text.
    """
    result = ""
    
    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():  # Only shift letters
            # Determine ASCII base (uppercase or lowercase)
            base = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around using modulo
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            # Keep non-alphabet characters unchanged
            result += char
    
    return result


# Example usage
if __name__ == "__main__":
    message = input("Enter your message: ")
    shift_value = int(input("Enter shift value (e.g., 3): "))
    
    encrypted_text = caesar_cipher(message, shift_value, mode='encrypt')
    print(f"Encrypted: {encrypted_text}")
    
    decrypted_text = caesar_cipher(encrypted_text, shift_value, mode='decrypt')
    print(f"Decrypted: {decrypted_text}")