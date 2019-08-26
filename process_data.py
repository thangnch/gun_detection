
import glob
import numpy as np
import cv2, os
import random
from random import seed
from random import randint



def edit_class_id():

    for filepath in glob.iglob('data/labels/*.txt'):

        fn = os.path.basename(filepath)

        fr = open(filepath, "r")
        contents = fr.readlines()
        for idx in range(len(contents)):
            contents[idx] = "0" + contents[idx][2:]
            print(contents[idx])

        fw = open(filepath.replace(".txt",".txo"),"w")
        fw.writelines(contents)
        fw.close()
        fr.close()

        #for idx in range(1):
        #print(filepath)
        #f = open(filepath, "w+")
        #f.write("0 0 0 1 1\n")
        #f.close()

def split_train_val():

    valno = 100
    valarr = []
    seed(2210)

    ft = open("train.txt", "w")
    fv = open("val.txt", "w")


    for idx in range(valno):
        valarr.append(randint(0,3000))
        fv.write("data/images/armas (" + str(valarr[-1]) + ").jpg\n")

    fv.close()

    for idx in range(3000):
        if (idx not in valarr):
            ft.write("data/images/armas (" + str(idx) + ").jpg\n")
    ft.close()









split_train_val()