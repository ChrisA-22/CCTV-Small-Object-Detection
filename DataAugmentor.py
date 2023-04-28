import xmleditor as xml
import PIL, os
from PIL import Image, ImageEnhance
from pathlib import Path

currentpath = os.getcwd()

path = Path(currentpath)
imagedir = Path(currentpath + r'\images')
xmldir = Path(r'\labels')
 
def flipx(imagepath, xmlpath):
    #Flip image horizontally if flipped version of image does not exist. Saves as imagex
    for file in os.listdir(imagedir):
        if (str(path) + '\\Weapons\\' + str(file) == str(imagepath)[:-4] + 'x' + '.jpg' or 'x' in str(imagepath)):
            print("Already exists")
            return -1
    image = Image.open(imagepath)
    flipped = image.transpose(Image.FLIP_LEFT_RIGHT)
    xvalues = xml.getx(xmlpath)
    width = xml.getwidth(xmlpath)
    for i in range(0, len(xvalues)):
        for j in range(0, len(xvalues[i])):
            xvalues[i][j] = width - xvalues[i][j]
    #Flip xvalues lists so that mins and maximums are in the right place.
    #xvalues = list of 2 lists, first was original minimums inverted to maximums and seond is maximums inverted to minimums
    xvalues = [list(value) for value in xvalues]
    temp = xvalues[0]
    xvalues[0] = xvalues[1]
    xvalues[1] = temp
    #Make new xml file
    with open(xmlpath, 'r') as file:
        data = file.readlines()
    newxml = str(xmlpath)[:-4] + 'x' + '.txt'
    newxml = Path(newxml)
    with open(newxml, 'w+') as file:
        file.writelines(data)
    xmins = xvalues[0]
    xmaxs = xvalues[1]
    xml.setx(newxml, xmins, xmaxs)
    newimage = str(imagepath)[:-4] + 'x' + '.jpg'
    newimage = Path(newimage)
    flipped.save(newimage)
    print(str(newimage))
    return 0

def blackwhite(imagepath, xmlpath):
    #Makes a black and white copy of an image and saves it as imageb
    for file in os.listdir(imagedir):
        if ('b' in str(imagepath[-5:])):
            print("Already exists")
            return -1
    image = Image.open(imagepath)
    blackandwhite = image.convert("L")
    newimage = str(imagepath)[:-4] + 'b' + '.png'
    newimage = Path(newimage)
    blackandwhite.save(newimage)
    with open(xmlpath, 'r') as file:
        data = file.readlines()
    newxml = str(xmlpath)[:-4] + 'b' + '.txt'
    newxml = Path(newxml)
    with open(newxml, 'w+') as file:
        file.writelines(data)
    return 0

imagelist = []
xmllist = []
#Flip every file on x axis
for file in os.listdir(imagedir):
    imagelist.append(file)
for file in os.listdir(xmldir):
    xmllist.append(file)

#for i in range(0, len(imagelist)):
    #print(imagelist[i])
    #flipx(Path(str(imagedir) + '\\' + imagelist[i]), Path(str(xmldir) + '\\' + xmllist[i]))
    #blackwhite(Path(str(imagedir) + '\\' + imagelist[i]), Path(str(xmldir) + '\\' + xmllist[i]))
    #darken(Path(str(imagedir) + '\\' + imagelist[i]), Path(str(xmldir) + '\\' + xmllist[i]))
    #brighten(Path(str(imagedir) + '\\' + imagelist[i]), Path(str(xmldir) + '\\' + xmllist[i]))

imagelist = []
xmllist = []
nonelist = []
    
for file in os.listdir(imagedir):
    imagelist.append(file)
for file in os.listdir(xmldir):
    xmllist.append(file)
        

#Yolo torch is a txt in the format:
# class     x_center    y_center    width   height

def fliplabel(imagepath, labelpath):
    #Flip image horizontally if flipped version of image does not exist. Saves as imagex
    #Works with YOLOv7 labels instead of xml files.
    for file in os.listdir(imagedir):
        if ('x' in str(imagepath)):
            print("Already exists")
            return -1
    with open(labelpath, 'r') as file:
        data = file.readlines()
    newdata = ''
    x_center = 0
    y_center = 0
    width = 0
    height = 0
    for line in data:
        line = line.split(' ')
        x_center = float(line[1])
        x_center = 1 - x_center 
        newdata = newdata + ('0 ' + str(x_center) + ' ' + line[2] + ' ' + line[3] + ' ' + line[4])
        newdata = newdata + "\n"
    newlabel = str(labelpath[:-4]) + 'x' + '.txt'
    newlabel = Path(newlabel)
    with open(newlabel, 'w+') as file:
        file.writelines(newdata)
    image = Image.open(imagepath)
    flipped = image.transpose(Image.FLIP_LEFT_RIGHT)
    newimage = str(imagepath)[:-4] + 'x' + '.png'
    newimage = Path(newimage)
    flipped.save(newimage)
    print(str(newimage))
    return 0

removelist = []
print(len(imagelist))
for i in range(0, len(imagelist)):
    if(imagelist[i][:4] == 'none'):
        #fliplabel(str(imagedir) + '\\' + imagelist[i],str(xmldir) + '\\' + xmllist[i])
        #blakwhite(str(imagedir) + '\\' + imagelist[i],str(xmldir) + '\\' + xmllist[i])
        print(imagelist[i])







