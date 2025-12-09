import hashlib

def hash_password_sha256(password):
    """
    Returns the SHA-256 hash of the given password as a hexadecimal string.
    
    Parameters:
        password (str): The password to hash.
    
    Returns:
        str: The SHA-256 hash in hexadecimal format.
    """
    # Encode the password to bytes
    password_bytes = password.encode('utf-8')
    
    # Create a SHA-256 hash object
    sha256_hash = hashlib.sha256(password_bytes)
    
    # Return the hexadecimal digest
    return sha256_hash.hexdigest()


# Example usage
if __name__ == "__main__":
    pwd = input("Enter your password: ")
    hashed_pwd = hash_password_sha256(pwd)
    print(f"SHA-256 Hashed Password: {hashed_pwd}")