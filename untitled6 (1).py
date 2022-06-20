# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kZYK5Y896j-jqVJ6b35xZV60ymv9q_1G
"""

import numpy as np 
import cv2 as cv
import matplotlib.pyplot as plt
from skimage.filters.rank import entropy
from skimage.morphology import disk
from IPython.core.display import Image
import statistics
from skimage import data
from skimage.util import img_as_ubyte
from skimage import io
from skimage import color
import scipy.optimize

def imadjust(x,a,b,c,d,gamma=1):
    # Similar to imadjust in MATLAB.
    # Converts an image range from [a,b] to [c,d].
    # The Equation of a line can be used for this transformation:
    #   y=((d-c)/(b-a))*(x-a)+c
    # However, it is better to use a more generalized equation:
    #   y=((x-a)/(b-a))^gamma*(d-c)+c
    # If gamma is equal to 1, then the line equation is used.
    # When gamma is not equal to 1, then the transformation is not linear.

    y = (((x - a) / (b - a)) ** gamma) * (d - c) + c
    return y

from io import BytesIO
from google.colab import files
uploaded = files.upload()
im = Image('E1(1).JPG')

i=5 #To have 8 bins, best number in Javad's paper
results=np.zeros((387,18))
#Feature calculation for each image in the directory
for j in range (1,387): #Parallel for loop on all images.
  print("Image top-{} \n".format[j])
  image_name = 'D2/top-{}.jpeg'.format(j)
  imgTemp = io.imread(image_name)
  imgGray = color.rgb2gray(np.asarray(im))
  imgCropped = imgGray[1:1050, 435:1484] #image cropped to 1050x1050
  imgTemp=imadjust(imgCropped,imgCropped.min(),imgCropped.max(),0,1)
  #The different numbers of bins are obtained by dividing the utin8
  #gray levels by 2, by rounding the resulting number with floor and by
  #converting the resulting numbers to a uint8. Dividing by 2 gives gray
  #levels that vary between 0 and 127, dividing by 4 gives gray levels 
  # that vary between 0 and 63, etc. This has been updated from previous
  #versions. You cannot do directly imgTemp/2^i has the result is
  #automatically rounded and converted to a uint8. This should be
  #corrected elsewhere (e.g. Javad's paper?)
  imgTemp=float (imgTemp)/2*i 
  imgTemp= np.floor(imgTemp)
  imgTemp=imgTemp.astype(np.uint8)
  resultsTemp = np.zeros((1,18))
  r= np.array([61,39,24,15,10,6,4,2,1]) #radius of the entropy filters
for k in range (1,9): #Loop over the 9 radius
     print ("r= {}\n" , r[k])
     #SE_disk = cv2.getStructuringElement(cv2.MORPH_RECT,r(k))
     entropyTemp =  entropy(img, disk(r[k]))
     resultsTemp[k] =np.mean(entropyTemp)
     resultsTemp[9+k] = np.std(entropyTemp)
   #print(resultsTemp)
  results[j] = resultsTemp
print("resultsD2.mat","results")