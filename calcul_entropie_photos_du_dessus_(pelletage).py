# -*- coding: utf-8 -*-
"""calcul entropie  photos du dessus (pelletage)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mGrkdzZZu5cMVEZjIGn2mNTf1PZHCvOd
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

mypath='/content/drive/Shareddrives/ph/photos dessus pelletage ' #Chemin d'acces vers le fichier dans le drive 
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
numberI=len(onlyfiles)
images = np.empty((numberI,4024,6048,3), dtype=np.uint8)  #Il est important de preciser la taille des images dans ce cas image.shape = (6048,4024,3)
for n in range(0, numberI):
  images[n] = cv.imread( join(mypath,onlyfiles[n]) )

def imadjust(x,a,b,c,d,gamma=1):  #fonction imadjust redéfinie en python
    y = (((x - a) / (b - a)) ** gamma) * (d - c) + c
    return y

i=5 
r= np.array([61,39,24,15,10,6,4,2,1])
results=np.zeros((numberI,18))

for j in range (0,numberI):
    #mise en forme de l'image
    imgGray = color.rgb2gray(np.asarray(images[j])) #convertir en niveaux de gris
    imgCropped = imgGray[1:1280, 1:520]
    imgTemp=imadjust(imgCropped,imgCropped.min(),imgCropped.max(),0,1)
    imgTemp=(imgTemp.astype(float))/2*i 

    imgTemp= np.floor(imgTemp)
    imgTemp=imgTemp.astype(np.uint8)
    resultsTemp = np.zeros(18)
    #calcul de la moyenne et de l'ecart type de l'entropie pour chaque image par rapport aux filtres
    for k in range(9):
        print("Image {0} taille de filtre r = {1}".format(j ,r[k]))
        entropyTemp =  entropy(imgTemp, disk(r[k]))
        resultsTemp[k] =np.mean(entropyTemp)
        resultsTemp[8+k] = np.std(entropyTemp)
        results[j] = resultsTemp

print(results)
np.savetxt('results.txt', results, fmt='%f') #Sauvegarde de la matrice EntropieLocale dans un fichier text