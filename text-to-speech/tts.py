from gtts import gTTS

print("------ TEXT TO SPEECH CONVERTER ------")

text = input("Enter text to convert to speech: ")
filename = input("Enter output file name (e.g., output.mp3): ")

try:
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    print(f"\nAudio saved successfully as {filename}")

except Exception as e:
    print("Error:", str(e))
