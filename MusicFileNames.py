import os

f = open("MusicFiles1.txt", "a")
for root, dirs, files in os.walk("C:/Users/Khalil/Music/"):
    for file in files:
        if file.endswith(".mp3"):
            print(file)
            s = str(file)
            f.write(s+"\n")
f.close()
