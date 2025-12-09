from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.exceptions import InvalidSignature

# ---------- STEP 1: Generate RSA key pair ----------
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

# Save keys to files (simulating certificate storage)
with open("private_key.pem", "wb") as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ))

with open("public_key.pem", "wb") as f:
    f.write(public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))

print("Keys generated and saved.")

# ---------- STEP 2: Create a document ----------
document_content = b"This is my college practical document."
with open("document.txt", "wb") as f:
    f.write(document_content)

# ---------- STEP 3: Sign the document ----------
signature = private_key.sign(
    document_content,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

with open("signature.bin", "wb") as f:
    f.write(signature)

print("Document signed. Signature saved to signature.bin")

# ---------- STEP 4: Simulate sending ----------
# In real life, you'd send: document.txt + signature.bin + public_key.pem

# ---------- STEP 5: Verify the signature ----------
try:
    public_key.verify(
        signature,
        document_content,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("✅ Signature is valid. Document is authentic.")
except InvalidSignature:
    print("❌ Signature is invalid. Document may have been tampered with.")