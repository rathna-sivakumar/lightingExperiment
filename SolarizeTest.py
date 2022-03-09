# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 15:44:02 2021

@author: rathn
"""

from PIL import Image, ImageDraw, ImageFont
from PIL import ImageOps as ipo
import os
import numpy as np

from matplotlib import pyplot as plt

##to convert tango imgs to jpgs from pngs
# for f in os.listdir('.'):
#     if f.endswith('.PNG'):
#          i = Image.open(f)
#          fn, fext = os.path.splitext(f)
#          image1 = Image.open('{}.PNG'.format(fn))
#          image1 = image1.convert('RGB') #need to make RGB for png to jpg
#          image1.save('{}.jpg'.format(fn))

font = ImageFont.truetype("times-ro.ttf", size=12)

##code to add grid lines and pixel count on x and y axis, for later use
# for f in os.listdir('.'):
#      if f.endswith('.JPG') or f.endswith('.jpg'):
#             image1 = Image.open(f)
#             fn, fext = os.path.splitext(f)
#             xsize, ysize = image1.size
#             line = ImageDraw.Draw(image1, 'RGBA')
#             for x in range(0,xsize,30):
#                 if x < 100 :
#                     line.text((x-15,7), str(x), (255,0,0), font=font)
#                 elif x < 1000 :
#                     line.text((x-20,7), str(x), (255,0,0), font=font)
#                 else :
#                     line.text((x-25,7), str(x), (255,0,0), font=font)
#                 line.rectangle(((x,0), (x+0.5,ysize)), fill=(255,0,0))
#             for y in range(0,ysize,30):
#                 line.text((5,y-6), str(y), (255,0,0), font=font)
#                 line.rectangle(((0,y), (xsize,y+0.5)), fill=(255,0,0))
#             image1.save('Grid/{}_grid.{}'.format(fn, fext))


#code to solarize img - ie invert all colors above certain threshold
for f in os.listdir('.'):
      if f.endswith('.JPG') or f.endswith('.jpg'):
          i = Image.open(f)
          fn, fext = os.path.splitext(f)
          image_src = i.convert('L')
          image_sol = ipo.solarize(image_src, threshold=130)
          image_sol.save('Solarized/{}_solarized.{}'.format(fn, fext))

