#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

if(os.name == 'nt'):
    os.system("cls");
else:
    os.system("clear")


#path = sys.argv[1] -- En realidad nunca le tenemos que pasar por parámetro la ruta, siempre va a ser "."
path = "."

items = os.listdir(path)

for i in items:
    if len(i.split(".")) > 1:
        for x in i.split((".")[-1]):
            if x == 'java':
                #print("Re/Compiling: " + i)
                try:
                    os.system("javac " + (path+"/"+i))
                    temp=i.split((".")[0])
                    for ex in temp:
                        if ex != "java":
                            print("--------------Done---------------")
                except ValueError:
                    print("Error!")
                    pass
