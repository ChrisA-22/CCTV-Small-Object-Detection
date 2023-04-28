import xmleditor as xml
import PIL, os
from PIL import Image, ImageEnhance
from pathlib import Path

currentpath = os.getcwd()

imagedir = Path(currentpath + r'\images')
validimagedir = Path(r'validation\images')
newimagedir = Path(r'Comp\images')
newvalidimagedir = Path(r'Comp\validation\images')

if(os.path.exists(imagedir) == False):
    #image path does not exist
    print("no image folder found")
    quit()
if(os.path.exists(validimagedir) == False):
    os.makedirs(validimagedir)
if(os.path.exists(newimagedir) == False):
    os.makedirs(newimagedir)
if(os.path.exists(newvalidimagedir) == False):
    os.makedirs(newvalidimagedir)


def compress(imagename):
    #Check compressed image doesn't exist alreadys
    for file in os.listdir(newimagedir):
        if (file == imagename):
            print("Already exists")
            return -1
    #Compress image and save to newimagedir under same name.
    originalpath = Path(str(imagedir) + imagename)
    original = Image.open(originalpath)
    newpath = Path(str(newimagedir) + imagename)
    original.save(newpath, quality=10, optimize=True)
    return 0

def validcompress(imagename):
    #Check compressed image doesn't exist alreadys
    for file in os.listdir(newvalidimagedir):
        if (file == imagename):
            print("Already exists")
            return -1
    #Compress image and save to newimagedir under same name.
    originalpath = Path(str(validimagedir) + imagename)
    original = Image.open(originalpath)
    newpath = Path(str(newvalidimagedir) + imagename)
    original.save(newpath, quality=10, optimize=True)
    return 0

imagelist = []
validimagelist = []

for file in os.listdir(imagedir):
    imagelist.append(file)

for i in range(0, len(imagelist)):
    print(imagelist[i])
    #compress("\\" + imagelist[i])

for file in os.listdir(validimagedir):
    validimagelist.append(file)
   
for i in range(0, len(validimagelist)):
    print(validimagelist[i])
    #validcompress("\\" + validimagelist[i])





