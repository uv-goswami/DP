# Rail Fence Cipher Implementation in Python

def encrypt_rail_fence(text, key):
    """
    Encrypts text using Rail Fence Cipher.
    
    Parameters:
        text (str): The plaintext to encrypt.
        key (int): Number of rails.
    
    Returns:
        str: Encrypted ciphertext.
    """
    # Create an empty matrix for the rails
    rail = [['\n' for _ in range(len(text))] for _ in range(key)]
    
    # Control variables
    dir_down = False
    row, col = 0, 0
    
    # Fill the rail matrix
    for char in text:
        # Change direction at the top or bottom rail
        if row == 0 or row == key - 1:
            dir_down = not dir_down
        
        rail[row][col] = char
        col += 1
        
        # Move up or down
        row += 1 if dir_down else -1
    
    # Read the matrix row by row
    result = []
    for r in rail:
        for c in r:
            if c != '\n':
                result.append(c)
    return "".join(result)


def decrypt_rail_fence(cipher, key):
    """
    Decrypts text encrypted with Rail Fence Cipher.
    
    Parameters:
        cipher (str): The ciphertext to decrypt.
        key (int): Number of rails.
    
    Returns:
        str: Decrypted plaintext.
    """
    # Create an empty matrix for the rails
    rail = [['\n' for _ in range(len(cipher))] for _ in range(key)]
    
    # Mark the positions to fill
    dir_down = None
    row, col = 0, 0
    
    for _ in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        
        rail[row][col] = '*'
        col += 1
        row += 1 if dir_down else -1
    
    # Fill the marked positions with ciphertext
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1
    
    # Read the matrix in zig-zag manner
    result = []
    row, col = 0, 0
    for _ in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        
        if rail[row][col] != '\n':
            result.append(rail[row][col])
            col += 1
        
        row += 1 if dir_down else -1
    
    return "".join(result)


# Example usage
if __name__ == "__main__":
    message = input("Enter your message: ")
    rails = int(input("Enter number of rails: "))
    
    encrypted = encrypt_rail_fence(message, rails)
    print(f"Encrypted: {encrypted}")
    
    decrypted = decrypt_rail_fence(encrypted, rails)
    print(f"Decrypted: {decrypted}")