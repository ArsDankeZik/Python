from __future__ import print_function

import os
import shutil
import sys

from PIL import Image


"""
1 (1-bit pixels, black and white, stored with one pixel per byte)
L (8-bit pixels, black and white)
P (8-bit pixels, mapped to any other mode using a color palette)
RGB (3x8-bit pixels, true color)
RGBA (4x8-bit pixels, true color with transparency mask)
CMYK (4x8-bit pixels, color separation)
YCbCr (3x8-bit pixels, color video format)
LAB (3x8-bit pixels, the L*a*b color space)
HSV (3x8-bit pixels, Hue, Saturation, Value color space)
I (32-bit signed integer pixels)
F (32-bit floating point pixels)
"""

def main():
    nrArgs = len(sys.argv)
    
    if nrArgs == 3 or nrArgs == 4: 
        copyTypeOn(nrArgs)
    else:
        print("\nUSAGE: python name.py type(L, P, RGB) \"origin\" \"destination\" ")


def copyTypeOn(numberArgs):
    args = sys.argv
    
    default = str(args[1])
    origin = ""
    destination = ""

    if numberArgs == 3:
        default = "L"
        origin = args[1].replace("\\", "/").replace("\"", "")
        destination = args[2].replace("\\", "/").replace("\"", "")
    elif numberArgs == 4:
        origin = args[2].replace("\\", "/").replace("\"", "")
        destination = args[3].replace("\\", "/").replace("\"", "") + "/"

    list = os.listdir(origin)

    for element in list:
        try:
            with Image.open(origin+"/"+element) as im:
                if(im.mode[-3:] == default):
                    src = origin + "/" + element
                    shutil.copy2(src, destination)
        except IOError:
            pass
    print("Done!")


if __name__ == "__main__":
    main()     
