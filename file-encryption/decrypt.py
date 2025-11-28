from cryptography.fernet import Fernet

print("------ FILE DECRYPTION TOOL ------")

def load_key():
    return open("key.key", "rb").read()

key = load_key()
fernet = Fernet(key)

encrypted_path = input("Enter encrypted file path: ")
output_path = input("Enter output file name: ")

try:
    with open(encrypted_path, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    with open(output_path, "wb") as dec_file:
        dec_file.write(decrypted_data)

    print("\nFile decrypted successfully!")

except Exception as e:
    print("Error:", e)
