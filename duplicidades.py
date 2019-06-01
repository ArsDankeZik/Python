import os
import sys
import time
import shutil
import threading

from PIL import Image
Image.LOAD_TRUNCATED_IMAGES = True


def th():
    path = sys.argv[1].replace("\\", "/").replace("\"", "")
    list = os.listdir(path)

    originalPath = path

    try:
        os.stat(path+"/thu")
    except:
        os.mkdir(path+"/thu")

    size = 5, 5
    for cx in list:
        #print(cx)
        try:
            if cx != "thu":    
                im = Image.open(path+"/"+cx)
                im.thumbnail(size)
                im.save(path+"/thu/"+cx)
            else:
                os.remove(originalPath+"/"+cx)
                os.remove(path+"/"+cx)
        except IOError:
            pass


    path += "/thu"
    #os.system("pause")


    thuList = os.listdir(path)
    time_estimation = len(thuList) * float(0.055)
    print("\n\nTime Estimation: {:.2f} seconds".format(time_estimation))
    time.sleep(2)

    start_time = time.clock()

    nr = 0 
    cutoff = 5
    equal = []

    os.system('cls')
    print('Please wait...')

    for x in thuList:
        for y in thuList:
            try:
                if x != y:
                    nr=nr+1
                    if Image.open(path+"/"+x) == Image.open(path+"/"+y):
                        #print(f"{x} y {y} son iguales.")
                        equal.append(x)
                        os.remove(originalPath+"/"+x)
                        os.remove(path+"/"+x)
            except IOError:
                pass

    print("----------------------------------------------")
    shutil.rmtree(path)
    for app in equal:
        print(f"Igual: {app}")

    print("\n\nTime Estimation: {:.2f} seconds".format(time_estimation))
    #print("\n\nReal duration: "+str(time.clock() - start_time), "seconds")
    print("Real duration: {:.2f} seconds".format(time.clock() - start_time))

threading.Thread(target=th).start()