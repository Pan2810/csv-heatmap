# -*- coding: utf-8 -*-
#import time
from datetime import datetime
import csv
from PIL import Image
import os.path

tempdict = {}
(pix, move, hue) = (1, 4, 0)
# 4*6*24 pixels X 365*4 pixels + 1
# One day, one image per 10minutes = 144 pixels
# times 4 (for picture to be bigger)
im = Image.new('RGBA', (577, 1461), 'black')
pixel = im.load()
# RGB weights
(rl,gl,bl) = (1,0.9,0.7)
# Color magnification constant
ff = 5.2

# default simple color scheme
def color (temperature):
    hue = ff*float(temperature)
    return (int(hue*rl),105-int(hue*gl),135-int((hue*bl)))

# first vasa interpolation
def colorvasa (temperature):
    d = 50
    tmax = 50
    tmin = 0
    hue = int(float(temperature))
    return (int((hue-tmin)*255/d), hue,  int((tmax-hue)*255/d))

#second vasa interpolation
def colorvasa2 (temperature):
    d = 40
    tmax = 46
    tmin = 6
    hue = int(float(temperature))
    if (hue < d/2):
      return (int((hue-tmin)*153/d/2), int((hue-tmin)*255/d/2), 204)
    else:
      return (255-int((tmax-hue)*153/d/2), int((tmax-hue)*255/d/2), int((tmax-hue)*204/d/2))

def temper_print(tempdict):
    counter = 0
    for hh in xrange(0, 24):
        for mm in xrange(0, 60, 10):
            timestring = '%02d:%02d' % (hh, mm)
            if timestring in tempdict:
                temperature = tempdict[timestring]
                if temperature == '':
                    temperature = 0

                (red, green, blue) = color(temperature)
                #(red, green, blue) = colorvasa(temperature)
                #(red, green, blue) = colorvasa2(temperature)
                for p in range(0, move):
                    for l in range(0, move):
                        pixel[counter + p, pix + l] = (red, green, blue, 255)
            counter += move
# END of function  temper_print

with open('2015.csv', 'rb') as cvsfile:
    file = csv.reader(cvsfile, delimiter=',', quotechar='|')
    for row in file:
        (date, unix, temp) = row
        day = date[0:10]
        time = date[11:16]
        if time == '00:00':
            tempdict = {}

        tempdict[time] = temp
        if time == '23:50':
            temper_print(tempdict)
            pix += move
cvsfile.close()

# Displaying and saving the output file
# example: img/2015.10.07-09.04.51.png
if not os.path.isdir("img"):
    print "IMG dir does not exist, create it: mkdir img    Exiting now"
    exit(1)

day = datetime.now()
imfilename = "img/" + day.strftime('%Y.%m.%d-%H.%M.%S') + ".png"
im.show()
im.save(imfilename,"PNG")
#EOF
