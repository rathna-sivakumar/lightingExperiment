# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 22:04:12 2022

@author: rathn
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
from PIL import ImageOps as ipo
import os
import math
import random
import numpy as np

from matplotlib import pyplot as plt

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
            
            #to add randomized glare blurs - get random starting point
            xNew = int(x/4)
            yNew = int(y/4)
            xNew = random.randint(xNew, 3*xNew)
            yNew = random.randint(yNew, 3*yNew)
            
            #determine glare circle radius
            #circleDiameter = min((x/20),(y/20))
            circleDiameter = min((x/17),(y/17))
            circR = circleDiameter/2
            
            #currently adds 5 circles
            for l in range (0,5) :
                dist = random.randint(20,60)
                xNew = xNew + dist*(l)
                yNew = yNew + dist*(l)
                glareCircle1 = Image.new("RGBA",(x,y), (0,0,0,0))
                glareCircle2 = ImageDraw.Draw(glareCircle1, "RGBA")
                for k in range (0,3) :
                    glareCircle2 = ImageDraw.Draw(glareCircle1, "RGBA")
                    glareCircle2.ellipse([(xNew-(3*circR),yNew-(3*circR)), (xNew+(3*circR),yNew+(3*circR))], fill=(255,255,255))
                    glareCircle1 = glareCircle1.filter(ImageFilter.GaussianBlur(20))
                img6 = ImageEnhance.Brightness(glareCircle1)
                img6.enhance(3).save('testSelfBlur.png')
                glareCircle1 = Image.open('testSelfBlur.png')
                
                
                for j in range (15,5,-3) :
                    glareCircle2 = ImageDraw.Draw(glareCircle1, "RGBA")
                    glareCircle2.ellipse([(xNew-(circR/2),yNew-(circR/2)), (xNew+(circR/2),yNew+(circR/2))], fill=(255,255,255))
                    glareCircle1 = glareCircle1.filter(ImageFilter.GaussianBlur(j))
               
                s = 20
                t = 10
                r = random.randint(0,int(t*circR))
               
                glareCircle3 = Image.new('L', (int(s*circR),int(s*circR)))
                z = random.randint(-int(t*circR),int(t*circR))
                w = math.sqrt((t*circR*t*circR)-(z*z))
                w = int(w)
                for m in range (0,6):
                        glareCircle4 = ImageDraw.Draw(glareCircle3, "L")
                        w = int(t*circR)
                        v = int(2*w)
                        glareCircle4.polygon(((w,r), (w,w), (w,w)), fill=(255)) #can extend if want
                        q = random.randint(50,70)
                        glareCircle3 = glareCircle3.rotate(q)
                    
                #glareCircle3 = glareCircle3.putalpha(127)
                glareCircle1.paste(glareCircle3,(int(xNew-(t*circR)), int(yNew-(t*circR))), glareCircle3)
                
                glareCircle2 = ImageDraw.Draw(glareCircle1, "RGBA")
                glareCircle2.ellipse([(xNew-(circR/4),yNew-(circR/4)), (xNew+(circR/4),yNew+(circR/4))], fill=(255,255,255), outline=(255,255,255), width=1)
                glareCircle1 = glareCircle1.filter(ImageFilter.GaussianBlur(3))
                glareCircle1 = glareCircle1.convert('L')
                img1.paste(glareCircle1, (0,0), glareCircle1)
            
                        
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
            # new_image.save('glareCircle1/{}_0.png'.format(fn))
            # image1 = Image.open('glareCircle1/{}_0.png'.format(fn))
            # image1 = image1.convert('RGB') #need to make RGB for png to jpg
            # image1.save('glareCircle1/{}_0.jpg'.format(fn))
            # os.remove('glareCircle1/{}_0.png'.format(fn))
            
            new_image.save('SunCircle/{}_5.png'.format(fn))
            image1 = Image.open('SunCircle/{}_5.png'.format(fn))
            image1 = image1.convert('RGB') #need to make RGB for png to jpg
            image1.save('SunCircle/{}_5.jpg'.format(fn))
            os.remove('SunCircle/{}_5.png'.format(fn))
            
            #new_image.show()
            
