import os
from pathlib import Path

#import xmleditor.py as xml so commands are like xml.getx()

def getx(filename):
    #Get x values from xml file
    xmin = []
    xmax = []
    with open(filename, 'r') as file:
        for line in file:
            if ("xmin" in line):
                xmin.append(int(''.join(filter(str.isdigit, line))))
            elif("xmax" in line):
                xmax.append(int(''.join(filter(str.isdigit, line))))
    return xmin, xmax


def setx(filename, xmin, xmax):
    #Set x values from xml file
    count = 0
    xminlines = []
    xmaxlines = []
    with open(filename, 'r') as file:
        data = file.readlines()
        for line in data:
            if ("xmin" in line):
                xminlines.append(count)
            elif("xmax" in line):
                xmaxlines.append(count)
            count = count + 1
    for i in range(0, len(xminlines)):
        data[xminlines[i]] = "      <xmin>" + str(xmin[i]) + "</xmin>\n"
        data[xmaxlines[i]] = "      <xmax>" + str(xmax[i]) + "</xmax>\n"
    with open(filename, 'w') as file:
        file.writelines(data)
    return 0

def gety(filename):
    #Get y values from xml file
    ymin = []
    ymax = []
    with open(filename, 'r') as file:
        for line in file:
            if ("ymin" in line):
                ymin.append(int(''.join(filter(str.isdigit, line))))
            elif("ymax" in line):
                ymax.append(int(''.join(filter(str.isdigit, line))))
    return ymin, ymax

def sety(filename, ymin, ymax):
    #Set y values from xml file
    count = 0
    yminlines = []
    ymaxlines = []
    with open(filename, 'r') as file:
        data = file.readlines()
        for line in data:
            if ("ymin" in line):
                yminlines.append(count)
            elif("ymax" in line):
                ymaxlines.append(count)
            count = count + 1
    for i in range(0, len(yminlines)):
        data[yminlines[i]] = "      <ymin>" + str(ymin[i]) + "</ymin>\n"
        data[ymaxlines[i]] = "      <ymax>" + str(ymax[i]) + "</ymax>\n"
    with open(filename, 'w') as file:
        file.writelines(data)
    return 0

def getwidth(filename):
    #Get width of file
    with open(filename, 'r') as file:
        for line in file:
            if ("width" in line):
                width = int(''.join(filter(str.isdigit, line)))
    return width

def getheight(filename):
    #get height of file
    with open(filename, 'r') as file:
        for line in file:
            if ("height" in line):
                height = int(''.join(filter(str.isdigit, line)))
    return height



