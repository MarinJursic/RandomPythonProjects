import os
import time

path = r"C:\Users\Korisnik\Desktop\Project Files\Images for converting"

images = os.listdir(path)

new_extension = ".png"

print("Changing extension to --> " + new_extension)

for image in images:

    File  = os.path.join(path,image)
    base = os.path.splitext(File)[0]
    os.rename(File, base + new_extension)

time.sleep(1)
print(images)
print("File extension successfully changed")

