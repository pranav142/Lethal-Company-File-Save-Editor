from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import argparse
import os


def decrypt_aes(input_path, password, buffer_size=65536):
    with open(input_path, "rb") as f:
        iv = f.read(16)

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA1(),
        length=16,
        salt=iv,
        iterations=100,
        backend=default_backend(),
    )
    key = kdf.derive(password.encode())

    decryptor = Cipher(
        algorithms.AES(key), modes.CBC(iv), backend=default_backend()
    ).decryptor()

    decrypted_data = b""

    with open(input_path, "rb") as fin:
        fin.seek(16)
        while True:
            data = fin.read(buffer_size)
            if not data:
                break
            decrypted_data += decryptor.update(data)

        decrypted_data += decryptor.finalize()

    return decrypted_data


def encrypt_aes(data, output_path, password, buffer_size=65536):
    iv = os.urandom(16)

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA1(),
        length=16,
        salt=iv,
        iterations=100,
        backend=default_backend(),
    )
    key = kdf.derive(password.encode())

    encryptor = Cipher(
        algorithms.AES(key), modes.CBC(iv), backend=default_backend()
    ).encryptor()

    padder = padding.PKCS7(algorithms.AES.block_size).padder()

    try:
        encrypted_data = b""

        encrypted_data += iv

        index = 0
        while index < len(data):
            chunk = data[index : index + buffer_size]
            if not chunk:
                break
            padded_chunk = padder.update(chunk)
            encrypted_data += encryptor.update(padded_chunk)
            index += buffer_size

        encrypted_data += encryptor.update(padder.finalize())
        encrypted_data += encryptor.finalize()

        with open(output_path, "wb") as fout:
            fout.write(encrypted_data)

    except Exception as e:
        print(f"An error occurred: {e}")
