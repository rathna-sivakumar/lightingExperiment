# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 18:16:14 2021

@author: rathn
"""

from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter
from PIL import ImageOps as ipo
import os

for f in os.listdir('.'):
      if f.endswith('.JPG') or f.endswith('.jpg'):
          i = Image.open(f)
          fn, fext = os.path.splitext(f)
          #image = Image.open('TangoImage1.jpg')
          contrast = ImageEnhance.Contrast(i)
          x,y = i.size
          newx = 2*x
          new_image = Image.new('RGBA', size=(newx,y))
          contrast.enhance(3.0).save('Contrast/contrast.jpg')
          #contrast_image = Image.new('RGBA', size=(x,y))
          #contrast_image = contrast
          new_image.paste(i,(0,0))
          contrast_img = Image.open('Contrast/contrast.jpg')
          contrast_img = contrast_img.filter(ImageFilter.GaussianBlur(2))
          new_image.paste(contrast_img,(x,0))
          new_image.save('Contrast+Blur/{}_Contrast.png'.format(fn))
          image1 = Image.open('Contrast+Blur/{}_Contrast.png'.format(fn))
          image1 = image1.convert('RGB') #need to make RGB for png to jpg
          image1.save('Contrast+Blur/{}_Contrast.jpg'.format(fn))
          os.remove('Contrast+Blur/{}_Contrast.png'.format(fn))