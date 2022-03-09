# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 18:21:34 2021

@author: rathn
"""

from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter
from PIL import ImageOps as ipo
import os

#code to add brightness to batch of jpgs

#loop to go through all original Tango Images
for f in os.listdir('.'):
      if f.endswith('.JPG') or f.endswith('.jpg'):
          i = Image.open(f)
          fn, fext = os.path.splitext(f)
          #creates ImageEnhance type of og img to increase brightness of img
          brightness = ImageEnhance.Brightness(i)
          #create new img ('final') to display before and after side by side
          x,y = i.size
          newx = 2*x
          new_image = Image.new('RGBA', size=(newx,y))
          #increase brightness of original image and save as jpg
          #if no before and after required, below line can be edited
          #so that it is saved as the edited img - use line below :
          #brightness.enhance(1.5).save('Contrast+Blur/{}_edited.jpg'.format(fn))
          #otherwise enhance brightness of img and save separately to use later
          brightness.enhance(1.5).save('Contrast/contrast.jpg')
          ##test code lines 25-26
          #contrast_image = Image.new('RGBA', size=(x,y))
          #contrast_image = contrast
          #paste original image or before img onto final on the right side
          new_image.paste(i,(0,0))
          #open the edited image with increased brightness
          contrast_img = Image.open('Contrast/contrast.jpg')
          # #line below is test - to blur edited img further
          #contrast_img = contrast_img.filter(ImageFilter.GaussianBlur(2))
          #add the edited img as the after side onto final img left side
          new_image.paste(contrast_img,(x,0))
          #save final (with the before and after sides) as jpg
          #trouble with modes so save as png, convert RGB, then save as jpg
          new_image.save('Contrast+Blur/{}_Bright1-5.png'.format(fn))
          image1 = Image.open('Contrast+Blur/{}_Bright1-5.png'.format(fn))
          image1 = image1.convert('RGB') #need to make RGB for png to jpg
          image1.save('Contrast+Blur/{}_Bright1-5.jpg'.format(fn))
          os.remove('Contrast+Blur/{}_Bright1-5.png'.format(fn))
          os.remove('Contrast/contrast.jpg')

##TEST---------------------------------------
# brightness = ImageEnhance.Brightness(image)
# brightness.enhance(1.5).save('brightness.jpg')
