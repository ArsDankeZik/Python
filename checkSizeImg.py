import os
import sys
import time
import shutil
import threading

from PIL import Image
Image.LOAD_TRUNCATED_IMAGES = True

#Get input path and parse it
path = sys.argv[1].replace("\\", "/").replace("\"", "")
list = os.listdir(path)

#Create the lists for good and bad images to later process it
validIMG = []
toDeleteIMG = []

#Check size and append data to a list or another
for img in list:
        try:
            imgOpened =Image.open(path+"/"+img)
            w, h = imgOpened.size
            if w >= 600 and h >= 900:    
                validIMG.append(path+"/"+img)
            else:
                toDeleteIMG.append(path+"/"+img)
        except IOError:
            pass

for fileToDelete in toDeleteIMG:
    try:
        print("Delete: " + fileToDelete)
        os.remove(fileToDelete)
    except:
        pass
        

print("----------------------------------------------")

#Show how much images are in a list or another
print(f"Images < 600x900: {len(toDeleteIMG)}")
print(f"Images >= 600x900: {len(validIMG)}")