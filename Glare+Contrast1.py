# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 18:30:41 2021

@author: rathn
"""

from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter
from PIL import ImageOps as ipo
import os
import numpy as np

#code to add contrast and glare to batch of jpgs 

mask_im = Image.open('Contrast+Blur+Glare/glare.PNG').convert('L')

#method1 : contrast colors in image to make black stand out more, clearer mask
contrast2 = ImageEnhance.Contrast(mask_im)
contrast2.enhance(1.5).save('Contrast+Blur+Glare/glareTest.png')
mask_im = Image.open('Contrast+Blur+Glare/glareTest.png')

# #method2 : find near black pixels and convert them to black for clearer mask
# mask_im = mask_im.convert('RGBA')
# data = np.array(mask_im)   # "data" is a height x width x 4 numpy array
# red, green, blue, alpha = data.T # Temporarily unpack the bands for readability
# black_areas = ((red <= 50) & (blue <= 50) & (green <= 50))
# data[..., :-1][black_areas.T] = (0, 0, 0) # Transpose back needed
# im2 = Image.fromarray(data)
# mask_im = im2
# mask_im = mask_im.convert('L')

#loop to edit all original tango jpgs
for f in os.listdir('.'):
        if f.endswith('.JPG') or f.endswith('.jpg'):
            i = Image.open(f)                       #open current jpg
            fn, fext = os.path.splitext(f)          #strings of file name/type
            contrast = ImageEnhance.Contrast(i)     #create ImageEnhance type
            
            #create new image ('final') to display before and after photos
            x,y = i.size
            newx = 2*x       
            new_image = Image.new('RGBA', size=(newx,y))
            
            #contrast original jpg by 3.0 and save as a new jpg
            contrast.enhance(3.0).save('Contrast+Blur+Glare/contrast.jpg')
            
            #onto the final image, paste before picture on the right
            new_image.paste(i,(0,0))
            
            #open the contrasted jpg as an Img type
            contrast_img = Image.open('Contrast+Blur+Glare/contrast.jpg')
            
            #add the glare to the contrasted jpg
            x3, y3 = contrast_img.size
            x2, y2 = mask_im.size
            
            #use the glare image itself as mask so it acts like transparent img
            #add the transparent img onto the contrasted img - glare overlay
            contrast_img.paste(mask_im, (x3-x2, 0), mask_im)
            contrast_img.show()
            
            #paste the contrast img as the after picture on the left of final
            new_image.paste(contrast_img,(x,0))
           
            #save final image (with the before and after sides) as jpg
            #trouble with modes so save as png, convert RGB, then save as jpg
            new_image.save('Contrast+Blur+Glare/{}1.png'.format(fn))
            image1 = Image.open('Contrast+Blur+Glare/{}1.png'.format(fn))
            image1 = image1.convert('RGB') #need to make RGB for png to jpg
            image1.save('Contrast+Blur+Glare/{}1.jpg'.format(fn))
            os.remove('Contrast+Blur+Glare/{}1.png'.format(fn))
            
            #delete extra contrast.jpg generated earlier (ie contrasted og img)
            os.remove('Contrast+Blur+Glare/contrast.jpg')

#remove contrasted mask img used to add glare overlay            
os.remove('Contrast+Blur+Glare/glareTest.png')
  

# #TEST--------------------------------------------------------------        
# mask_im = Image.open('Contrast+Blur+Glare/glare.PNG').convert('L')
# im1 = Image.open('TangoImage1.jpg')

# mask_im = mask_im.convert('RGBA')
# data = np.array(mask_im)   # "data" is a height x width x 4 numpy array
# red, green, blue, alpha = data.T # Temporarily unpack the bands for readability
# black_areas = ((red <= 50) & (blue <= 50) & (green <= 50))
# data[..., :-1][black_areas.T] = (0, 0, 0) # Transpose back needed
# im2 = Image.fromarray(data)
# mask_im = im2
# mask_im = mask_im.convert('L')

# contrast = ImageEnhance.Contrast(mask_im)
# contrast.enhance(2.0).save('glareTest.png')
# mask_im = Image.open('glareTest.png')

# #im2 = mask_im.copy()
# #im2 = im2.filter(ImageFilter.GaussianBlur(10))

# x, y = im1.size
# x2, y2 = mask_im.size
# back_im = im1.copy()
# back_im.paste(mask_im, (x-x2, 0), mask_im)
# back_im.show()