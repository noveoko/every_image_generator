from PIL import Image
import numpy as np
import random

max_color = 100
width = 10
height = 10

allimages = []

def getcolor():
    color = random.choice([255,0])
    color = [color for a in range(0,3)]
    return color

def setcolor(d=3):
    colors = [getcolor() for a in range(0,width)]
    return colors

def makeimage():
    rgbArray = [setcolor(a) for a in range(0,height)]
    picid = np.sum(rgbArray)

    newimage = Image.new('RGB', (len(rgbArray[0]), len(rgbArray)))  # type, size
    newimage.putdata([tuple(p) for row in rgbArray for p in row])

    if picid not in allimages:
        allimages.append(picid)
        newimage.save("images/{}.png".format(picid))  # takes type from filename extension
        print('just saved image {}'.format(picid))
    else:
        pass


while len(allimages) < 1000:
    makeimage()
