import cv2

print("------ IMAGE TO SKETCH CONVERTER ------")

input_path = input("Enter image file path: ")
output_path = input("Enter output file name (e.g., sketch.png): ")

try:
    # Read image
    img = cv2.imread(input_path)

    if img is None:
        print("Unable to load image. Check file path.")
        exit()

    # Convert to gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Blur it
    blur = cv2.GaussianBlur(gray, (21, 21), 0)

    # Create sketch by dividing grey by blur
    sketch = cv2.divide(gray, blur, scale=256)

    # Save output
    cv2.imwrite(output_path, sketch)

    print(f"\nSketch saved as {output_path}")

except Exception as e:
    print("Error:", e)
