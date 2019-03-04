import os
import shutil
import sys
from PIL import Image

path = sys.argv[1].replace("\\", "/").replace("\"", "")
list = os.listdir(path)

nr = 0

for x in list:
    for y in list:
        try:
            if x != y:
                nr=nr+1
                if Image.open(path+"/"+x) == Image.open(path+"/"+y):
                    print(f"{x} y {y} son iguales.")
                    os.remove(path+"/"+x)
                #else:
                    #print(f"{nr}: {x} != {y}")
        except IOError:
            pass