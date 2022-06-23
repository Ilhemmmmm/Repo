# -*- coding: utf-8 -*-
"""Calcul entropie (R ph)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bGajq5VUcRfmi-Hro7_DNkk8v6KLg4-k
"""

import numpy as np 
import cv2 as cv
import matplotlib.pyplot as plt
from skimage.filters.rank import entropy
from skimage.morphology import disk
from skimage import color
from google.colab import drive
drive.mount('/content/drive')
from os import listdir
from os.path import isfile, join

mypath='/content/drive/folders/1IlCEWEwo55IKQdSHUvuv7bZM25YdBAdQ' #Chemin d'acces vers le fichier dans le drive 
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
numberI=len(onlyfiles)
images = np.empty((512,2560,1040,3), dtype=np.uint8) #Il est important de preciser la taille des images dans ce cas image.shape = (2560,1040,3)
for n in range(0, 512):
  images[n] = cv.imread( join(mypath,onlyfiles[n]) )

def imadjust(x,a,b,c,d,gamma=1):  #fonction imadjust redéfinie en python
    y = (((x - a) / (b - a)) ** gamma) * (d - c) + c
    return y

i = 5 #To have 8 bins, best number in Javad's paper
resultsD1 = np.zeros ((20.2*np.size(r),np.size(pathTemp) )) # Result variable initialization
pathTemp = ["E1(1).JPG","E1(2).JPG","E1(3).JPG"]
r = np.array ([61,39,24,15,10,6,4,2,1]) #radius of the entropy filters
#Feature calculation for each directory
for j in range (0,512):
   listingTemp =  dir {pathTemp(h)}    
# Feature calculation for each image in the directory
for j in range (20) :   #loop on all images 
    print("Image {E1(1)} taille de filtre r = {1}".format(j ,r[k]))
    imgGray = color.rgb2gray(np.asarray(images[j])) #convertir en niveaux de gris
    imgCropped = imgGray[1:1280, 1:520]
    imgTemp=(imgTemp.astype(float))/2*i 
    imgTemp= np.floor(imgTemp)
    imgTemp=imgTemp.astype(np.uint8)
    
    #calcul de la moyenne et de l'ecart type de l'entropie pour chaque image par rapport aux filtres
    
    featuresTemp= np.zeros(1.2*np.size(r))
    for k in range (0,np.size(r)):
        print("Image {E1(1)} taille de filtre r = {1}".format(j ,r[k]))
        entropyTemp =  entropy(imgTemp, disk(r[k]))
        featuresTemp[k] =np.mean(entropyTemp)
        featuresTemp[np.size(r)+k] = np.std(entropyTemp)
        resultsD1[j,:,h] = featuresTemp

print(resultsD1)
np.savetxt('resultsD1.txt', resultsD1, fmt='%f') #Sauvegarde de la matrice EntropieLocale dans un fichier text