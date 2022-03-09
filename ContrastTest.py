# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 17:34:05 2021

@author: rathn
"""

from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from PIL import ImageOps as ipo
import os


# image = Image.open('TangoImage1.jpg')
# contrast = ImageEnhance.Contrast(image)
# x,y = image.size
# newx = 2*x
# new_image = Image.new('RGBA', size=(newx,y))
# contrast.enhance(3.0).save('contrast.jpg')
# #contrast_image = Image.new('RGBA', size=(x,y))
# #contrast_image = contrast
# new_image.paste(image,(0,0))
# contrast_img = Image.open('contrast.jpg')
# new_image.paste(contrast_img,(x,0))
# new_image.show()
# new_image.convert(mode='RGB')
# new_image.save('contrast2.png')
# image1 = Image.open('contrast2.png')
# image1 = image1.convert('RGB') #need to make RGB for png to jpg
# image1.save('contrast2.jpg')
# os.remove('contrast2.png')

for f in os.listdir('.'):
      if f.endswith('.JPG') or f.endswith('.jpg'):
          i = Image.open(f)
          fn, fext = os.path.splitext(f)
          #image = Image.open('TangoImage1.jpg')
          contrast = ImageEnhance.Contrast(i)
          x,y = i.size
          newx = 2*x
          new_image = Image.new('RGBA', size=(newx,y))
          contrast.enhance(0.5).save('Contrast/contrast.jpg')
          #contrast_image = Image.new('RGBA', size=(x,y))
          #contrast_image = contrast
          new_image.paste(i,(0,0))
          contrast_img = Image.open('Contrast/contrast.jpg')
          new_image.paste(contrast_img,(x,0))
          new_image.save('Contrast/{}_Contrast2.png'.format(fn))
          image1 = Image.open('Contrast/{}_Contrast2.png'.format(fn))
          image1 = image1.convert('RGB') #need to make RGB for png to jpg
          image1.save('Contrast/{}_Contrast2.jpg'.format(fn))
          os.remove('Contrast/{}_Contrast2.png'.format(fn))