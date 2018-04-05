# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 08:28:51 2018

@author: user
"""

from sklearn.preprocessing import normalize
from sklearn.decomposition import PCA
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mimage
import numpy as np

url = "D:\\Online\\Doc\\4-1\\4-5\\timg.jpg"

img = mimage.imread(url)

img = img - img.mean()
#plt.imshow(img)

component = [10]

for i in range(len(component)):
    
    model = PCA(n_components=component[i])
    temp = model.fit(img)
    t = model.transform(img)
    plt.imshow(t)

