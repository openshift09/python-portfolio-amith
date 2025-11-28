from pytube import YouTube

print("------ YOUTUBE VIDEO DOWNLOADER ------")

url = input("Enter YouTube video URL: ")

try:
    yt = YouTube(url)

    print("\nVideo Title:", yt.title)
    print("Author:", yt.author)
    print("Length:", round(yt.length / 60, 2), "minutes")

    print("\nAvailable resolutions:")
    for stream in yt.streams.filter(progressive=True, file_extension='mp4'):
        print(" -", stream.resolution)

    resolution = input("\nChoose resolution (e.g., 720p, 360p): ")

    stream = yt.streams.filter(resolution=resolution, progressive=True).first()

    if stream:
        print("\nDownloading... Please wait...")
        stream.download()
        print("Download completed successfully!")
    else:
        print("Resolution not available.")

except Exception as e:
    print("Error:", e)
