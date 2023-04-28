import xmleditor as xml
from pathlib import Path
import os

#Yolo torch is a txt in the format:
# class     x_center    y_center    width   height
#needs to be in one row per pistol
#All are normalized 0-1
#This is ahieved with the following:

# class = 0
# x_center = xmin + xmax / 2 / imagewidth
#y_center = ymin + ymax / 2 / imageheight
#width = xmax - xmin / imagewidth
#height = ymax - ymin / imageheight
currentpath = os.getcwd()

imagepath = Path(currentpath + r'\images')
xmlpath = Path(currentpath + r'\xmls')
labelpath = Path(currentpath + r'\labels')

def xmltolabel(xmlname):
    #Creates a txt file in pytorch yolov7 format for the selected xml file
    #As the file is opened in write mode and no images are involved there is no need to chek for existing files as they will get overwritten
    xmlfile = Path(str(xmlpath) + '\\' + xmlname) 
    xvalues = xml.getx(xmlfile)
    yvalues = xml.gety(xmlfile)
    xmins = xvalues[0]
    xmaxs = xvalues[1]
    ymins = yvalues[0]
    ymaxs = yvalues[1]
    #These are either integers or lists of 2 or more integers depending on the number of pistols in each image.
    imageheight = xml.getheight(xmlfile) 
    imagewidth = xml.getwidth(xmlfile)
    if (len(xmaxs) == 1):
        #1 pistol in image
        x_center = ((xmins[0] + xmaxs[0])/2)/imagewidth
        y_center = ((ymins[0] + ymaxs[0])/2)/imageheight
        width = (xmaxs[0] - xmins[0])/imagewidth
        height = (ymaxs[0] - ymins[0])/imageheight
        data = ("0 " + str(x_center) + " " + str(y_center) + " " + str(width) + " " + str(height))
        txtname = xmlname[:-4] + '.txt'
        savepath = Path(str(labelpath) + '\\' + txtname)
        print(str(savepath))
        with open(savepath, 'w+') as file:
            file.writelines(data)
        return 0
    else:
        print(xmlname)
        # multiple pistols in image
        print(xmins)
        print(xmaxs)
        print(xvalues)
        data = ""
        for i in range(0, len(xmaxs)):
                xmin = xmins[i]
                xmax = xmaxs[i]
                ymin = ymins[i]
                ymax = ymaxs[i]
                x_center = ((xmin + xmax)/2)/imagewidth
                y_center = ((ymin + ymax)/2)/imageheight
                width = (xmax - xmin)/imagewidth
                height = (ymax - ymin)/imageheight
                line = ("0 " + str(x_center) + " " + str(y_center) + " " + str(width) + " " + str(height))
                data = data + line + "\n"
        txtname = xmlname[:-4] + '.txt'
        savepath = Path(str(labelpath) + '\\' + txtname)
        print(str(savepath))
        with open(savepath, 'w+') as file:
            file.writelines(data)
        return 0
    

xmllist = []
for file in os.listdir(xmlpath):
    xmllist.append(file)

for i in range(0, len(xmllist)):
    xmltolabel(xmllist[i])

    
    




