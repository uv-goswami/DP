import hashlib

def get_sha256_hash(password):
    encoded_password = password.encode('utf-8')
    sha256_hash = hashlib.sha256(encoded_password)
    return sha256_hash.hexdigest()

password = input("Enter Password: ")
hashed_output = get_sha256_hash(password)

print("SHA-256 Hash:", hashed_output)
