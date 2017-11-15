from PIL import Image
import numpy as np
import random
import os.path

max_color = 100
width = 2560
height = 1440
allimages = []

def getcolor():
    color = random.choice([255,0])
    color = [color,color,color]
    return color

def setcolor(d=3):
    colors = [getcolor() for a in range(0,width)]
    return colors

allids = []
def makeimage():
    rgbArray = [setcolor(a) for a in range(0,height)]
    picid = np.sum(rgbArray)
    if picid not in allids:
        newimage = Image.new('RGB', (len(rgbArray[0]), len(rgbArray)))  # type, size
        newimage.putdata([tuple(p) for row in rgbArray for p in row])
        newimage.save("images/{}.png".format(picid))  # takes type from filename extension
        allids.append(picid)
        print('just saved image {}\ttotal attempts:{}'.format(picid, count))
    else:
        pass


count = 0
while len(allimages) < 1000:
    count += 1
    print(count)
    makeimage()
