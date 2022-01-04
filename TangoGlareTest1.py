# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 12:17:12 2021

@author: rathna-sivakumar
"""

from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter
from PIL import ImageOps as ipo
import os
import numpy as np

# code to add contrast and glare to batch of jpgs 

#loop to edit all original tango jpgs, located in folder named Original
for f in os.listdir('Original'):
        if f.endswith('.JPG') or f.endswith('.jpg'):
            
            
            i = Image.open(f)                       #open current jpg
            fn, fext = os.path.splitext(f)          #strings of file name/type
            
            #convert image to black and white and get size
            img1 = i
            img1 = img1.convert('L')
            x, y = img1.size
            
            #create copies
            img2 = img1.copy()
            
            
            og_img = img1.copy()
            og_img = og_img.convert('L')
            
            #create blank image (black background) of the same size
            img3 = Image.new('L', (x,y))
            
            #blur the image
            img2 = img2.filter(ImageFilter.GaussianBlur(15))
            img2 = img2.convert('L')
            
            #use the original image as a mask and place it over the blurred img
            img2.paste(og_img, (0,0), og_img)
            #img2.paste(img1, (0,0), img1)
            
            #enhance brightness of edited image, save it, and convert to B/W
            img5 = ImageEnhance.Brightness(img2)
            img5.enhance(3).save('testSelfBlur.jpg')
            img2 = Image.open('testSelfBlur.jpg')
            img2 = img2.convert('L')
            
            #use enhanced image as a mask and place over the original image
            img1.paste(img2, (0,0), img2)
            
            #create new image ('final') to display before and after photos
            x,y = i.size
            newx = 2*x       
            new_image = Image.new('RGBA', size=(newx,y))
            
            #onto the final image, paste before picture on the right
            new_image.paste(i,(0,0))
            
            #paste the contrast img as the after picture on the left of final
            new_image.paste(img1,(x,0))
           
            #save final image (with the before and after sides) as jpg
            #trouble with modes so save as png, convert RGB, then save as jpg
            new_image.save('ExtraBlur/{}_3.png'.format(fn))
            image1 = Image.open('ExtraBlur/{}_3.png'.format(fn))
            image1 = image1.convert('RGB') #need to make RGB for png to jpg
            image1.save('ExtraBlur/{}_3.jpg'.format(fn))
            os.remove('ExtraBlur/{}_3.png'.format(fn))
            
#------------------------------------------------------------------------

# #TEST
# img1 = Image.open('Original/TangoImage2.jpg')
# x, y = img1.size
# img2 = img1.copy()
# img2.thumbnail((x-20,y-20))
# img3 = Image.new('L', (x,y))
# img2 = img2.filter(ImageFilter.GaussianBlur(2))
# #img2.show()
# img2 = img2.convert('L')
# img3.paste(img2, (10,10), img2)
# img4 = Image.new('L', (x,y))
# img4.paste(img1, (10,10), img3)
# img5 = ImageEnhance.Contrast(img4)
# img5.enhance(2.5).save('testSelfBlur.jpg')
# img5 = Image.open('testSelfBlur.jpg')
# img5 = ImageEnhance.Brightness(img5)
# img5.enhance(2.5).show()
# os.remove('testSelfBlur.jpg')
# #img4.show()

# #TEST2
# img1 = Image.open('Original/TangoImage2.jpg')
# x, y = img1.size
# img2 = img1.copy()
# og_img = img1.copy()
# og_img = og_img.convert('L')
# img2.thumbnail((x-20,y-20))
# img3 = Image.new('L', (x,y))
# img2 = img2.filter(ImageFilter.GaussianBlur(2))
# #img2.show()
# img2 = img2.convert('L')
# img3.paste(img2, (10,10), img2)
# img4 = Image.new('L', (x,y))

# img5 = ImageEnhance.Contrast(img1)
# img5.enhance(2.5).save('testSelfBlur.jpg')
# img5 = Image.open('testSelfBlur.jpg')
# img5 = ImageEnhance.Brightness(img5)
# img5.enhance(2.5).save('testSelfBlur.jpg')
# img1 = Image.open('testSelfBlur.jpg')
# img1 = img1.convert('L')
# img1.show()

# img4.paste(img1, (0,0), img3)
# img4.show()
# # img7 = og_img.copy()
# # img7 = img7.filter(ImageFilter.GaussianBlur(4))
# img4.paste(og_img, (0,0), og_img)
# #os.remove('testSelfBlur.jpg')
# img4.show()

# #TEST3
# img1 = Image.open('Original/TangoImage2.jpg')
# x, y = img1.size
# img2 = img1.copy()
# og_img = img1.copy()
# og_img = og_img.convert('L')
# img2.thumbnail((x-20,y-20))
# img3 = Image.new('L', (x,y))

# img5 = ImageEnhance.Contrast(img2)
# img5.enhance(2.5).save('testSelfBlur.jpg')
# img5 = Image.open('testSelfBlur.jpg')
# # img5 = ImageEnhance.Brightness(img5)
# # img5.enhance(2.5).save('testSelfBlur.jpg')
# img2 = Image.open('testSelfBlur.jpg')
# img2 = img2.convert('L')

# img2 = img2.filter(ImageFilter.GaussianBlur(0.25))
# #img2.show()
# img2 = img2.convert('L')
# img3.paste(img2, (10,10), img2)
# img3 = img3.convert('L')
# img3.show()
# img4 = Image.new('L', (x,y), color=0)
# img4Rectangle = ImageDraw.Draw(img4, "L")
# img4Rectangle.rectangle(((45,30), (x-45,y-30)), fill=255)
# img4 = img4.filter(ImageFilter.GaussianBlur(30))
# img5 = ImageEnhance.Contrast(img4)
# img5.enhance(1.5).save('testSelfBlur.jpg')
# img4 = Image.open('testSelfBlur.jpg')
# img4.show()
# img5 = Image.new('L', (x,y))
# img5.paste(img3, (0,0), img4)
# #img4.show()
# img5.show()


# # img5 = ImageEnhance.Contrast(img1)
# # img5.enhance(2.5).save('testSelfBlur.jpg')
# # img5 = Image.open('testSelfBlur.jpg')
# # img5 = ImageEnhance.Brightness(img5)
# # img5.enhance(2.5).save('testSelfBlur.jpg')
# # img1 = Image.open('testSelfBlur.jpg')
# # img1 = img1.convert('L')
# # img1.show()

# img4 = Image.new('L', (x,y), color=0)
# img4.paste(img1, (0,0), img5)
# # img7 = og_img.copy()
# # img7 = img7.filter(ImageFilter.GaussianBlur(4))
# #img4.paste(og_img, (0,0), og_img)
# #os.remove('testSelfBlur.jpg')
# img4.show()

# #TEST4
# img1 = Image.open('Original/TangoImage2.jpg')
# img1 = img1.convert('L')
# x, y = img1.size
# img2 = img1.copy()
# og_img = img1.copy()
# og_img = og_img.convert('L')
# #og_img.show()
# #image_sol = ipo.solarize(og_img, threshold=130)
# #img1.show()

# # img5 = ImageEnhance.Contrast(img1)
# # img5.enhance(1.4).save('testSelfBlur.jpg')
# # img1 = Image.open('testSelfBlur.jpg')
# # img1 = img1.convert('L')
# # img1.putalpha(50)
# # img1.show()

# #img2.thumbnail((x-20,y-20))
# img3 = Image.new('L', (x,y))
# img2 = img2.filter(ImageFilter.GaussianBlur(15))
# #img2.show()
# img2 = img2.convert('L')
# img2.paste(og_img, (0,0), og_img)
# #img2.paste(img1, (0,0), img1)

# # img5 = ImageEnhance.Brightness(img2)
# # img5.enhance(1.10).save('testSelfBlur.jpg')
# # img2 = Image.open('testSelfBlur.jpg')
# # img2 = img2.convert('L')

# #img2.show()
# #img2.show()
# # img1 = img1.convert('L')
# img1.paste(img2, (0,0), img2)
# img1.show()
# # img4 = Image.new('L', (x,y))

# # img5 = ImageEnhance.Contrast(img1)
# # img5.enhance(2.5).save('testSelfBlur.jpg')
# # img5 = Image.open('testSelfBlur.jpg')
# # img5 = ImageEnhance.Brightness(img5)
# # img5.enhance(2.5).save('testSelfBlur.jpg')
# # img1 = Image.open('testSelfBlur.jpg')
# # img1 = img1.convert('L')
# # img1.show()


# #TEST5
# img1 = Image.open('Original/TangoImage3.jpg')
# img1 = img1.convert('L')
# x, y = img1.size
# img2 = img1.copy()
# og_img = img1.copy()
# og_img = og_img.convert('L')
# #og_img.show()
# #image_sol = ipo.solarize(og_img, threshold=130)
# #img1.show()

# # img5 = ImageEnhance.Contrast(img1)
# # img5.enhance(1.4).save('testSelfBlur.jpg')
# # img1 = Image.open('testSelfBlur.jpg')
# # img1 = img1.convert('L')
# # img1.putalpha(50)
# # img1.show()

# #img2.thumbnail((x-20,y-20))
# img3 = Image.new('L', (x,y))
# img2 = img2.filter(ImageFilter.GaussianBlur(15))
# #img2.show()
# img2 = img2.convert('L')
# img2.paste(og_img, (0,0), og_img)
# img2.show()
# #img2.paste(img1, (0,0), img1)

# img5 = ImageEnhance.Brightness(img2)
# img5.enhance(3.0).save('testSelfBlur.jpg')
# img2 = Image.open('testSelfBlur.jpg')
# img2 = img2.convert('L')

# img2.show()
# #img2.show()
# # img1 = img1.convert('L')
# img1.paste(img2, (0,0), img2)
# img1.show()
# # img4 = Image.new('L', (x,y))

# # img5 = ImageEnhance.Contrast(img1)
# # img5.enhance(2.5).save('testSelfBlur.jpg')
# # img5 = Image.open('testSelfBlur.jpg')
# # img5 = ImageEnhance.Brightness(img5)
# # img5.enhance(2.5).save('testSelfBlur.jpg')
# # img1 = Image.open('testSelfBlur.jpg')
# # img1 = img1.convert('L')
# # img1.show()

