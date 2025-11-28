from cryptography.fernet import Fernet

print("------ FILE ENCRYPTION TOOL ------")

# Generate key
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Load key
def load_key():
    return open("key.key", "rb").read()

# Generate key if not exists
try:
    key = load_key()
except:
    print("Key not found — generating new key...")
    write_key()
    key = load_key()

fernet = Fernet(key)

file_path = input("Enter file path to encrypt: ")

try:
    with open(file_path, "rb") as file:
        data = file.read()

    encrypted_data = fernet.encrypt(data)

    with open(file_path + ".encrypted", "wb") as enc_file:
        enc_file.write(encrypted_data)

    print(f"\nFile encrypted successfully! Saved as: {file_path}.encrypted")

except Exception as e:
    print("Error:", e)
