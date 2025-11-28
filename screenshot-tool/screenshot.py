import pyautogui
import datetime

print("------ SCREENSHOT TOOL ------")

filename = input("Enter output file name (e.g., screenshot.png): ")

try:
    # Capture screenshot
    image = pyautogui.screenshot()

    # Save
    image.save(filename)

    print(f"\nScreenshot saved as {filename}")

except Exception as e:
    print("Error:", e)
