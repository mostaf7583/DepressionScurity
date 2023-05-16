from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

key_size = 16  # 128 bits
key = Fernet.generate_key()
key= key[:key_size]

# Read the contents of the file to be encryptm,n,mn,n,mn,mn,edmk
with open('file.txt', 'rb') as f:
    data = f.read()

# Pad the data to a multiple of 16 bytes
padded_data = data + b"\0" * (16 - len(data) % 16)

# Generate a random 16-byte IV
iv = os.urandom(16)

# Create an AES cipher object with the key and IV
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

# Encrypt the data
encryptor = cipher.encryptor()
encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

# Write the encrypted data to a new file
with open('encrypted_file.txt', 'wb') as f:
    f.write(iv + encrypted_data)

# Write the key to a file for later use
with open('key.key', 'wb') as f:
    f.write(key)





