from PIL import Image

print("------ IMAGE RESIZER ------")

input_path = input("Enter path of the image to resize: ")
width = int(input("Enter new width: "))
height = int(input("Enter new height: "))
output_path = input("Enter output file name (e.g., resized.jpg): ")

try:
    img = Image.open(input_path)
    resized_img = img.resize((width, height))
    resized_img.save(output_path)

    print(f"\nImage resized and saved as {output_path}")

except Exception as e:
    print("Error:", e)
