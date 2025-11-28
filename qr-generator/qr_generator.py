import qrcode

print("------ QR CODE GENERATOR ------")

data = input("Enter text or URL to convert into QR code: ")
filename = input("Enter output file name (e.g., my_qr.png): ")

# Generate QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save(filename)

print(f"\nQR Code created successfully and saved as {filename}")
