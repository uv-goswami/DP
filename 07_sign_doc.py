import rsa
import os

def generate_keys():
    (pubkey, privkey) = rsa.newkeys(512)
    return pubkey, privkey

def sign_file(filename, private_key):
    try:
        with open(filename, 'rb') as file:
            file_data = file.read()
            
        signature = rsa.sign(file_data, private_key, 'SHA-1')
        
        with open(filename + ".sig", 'wb') as sig_file:
            sig_file.write(signature)
            
        return signature
        
    except FileNotFoundError:
        print("File not found.")

def verify_file(filename, public_key):
    try:
        with open(filename, 'rb') as file:
            file_data = file.read()
            
        with open(filename + ".sig", 'rb') as sig_file:
            signature = sig_file.read()
            
        rsa.verify(file_data, signature, public_key)
        print("VALID")
        
    except rsa.VerificationError:
        print("The file has been tampered")
    except FileNotFoundError:
        print("Error: Files missing.")

pub_key, priv_key = generate_keys()

filename = "practical.txt"
with open(filename, "w") as f:
    f.write("Data Privacy Practical")


sign_file(filename, priv_key)
print("Signed: practical.sig")

print("Verifying")
verify_file(filename, pub_key)

with open(filename, "a") as f:
    f.write("LOL")
print("\nTampering")

print("Verifying the tampered file")
verify_file(filename, pub_key)
