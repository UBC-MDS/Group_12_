import numpy as np
import pandas as pd
import os
from scipy.signal import convolve2d
from skimage.color import rgb2gray

import matplotlib.pyplot as plt
%matplotlib inline

def read_image(filename):
    return plt.imread(filename)

def show_conv(img, filt):

    plt.figure(figsize=(8,16))
    plt.subplot(1,2,1)

    plt.imshow(img, cmap='gray')
    plt.xticks(())
    plt.yticks(())
    plt.title("original")
    I_filt = convolve2d(img,filt, boundary='symm', mode='same')

    I_filt = np.maximum(0, I_filt) # set negative values to 0, for visualization purposes
    I_filt = np.minimum(1, I_filt) # set values greater than 1 to 1, for visualization purposes
    plt.subplot(1,2,2)
    if np.sum(filt) == 0: # a trick to make the images easier to see, not part of the "math"
        I_filt/np.max(I_filt)
    else:
        I_filt

    plt.imshow(I_filt, cmap='gray')
    plt.xticks(())
    plt.yticks(())
    plt.title("filtered")

    return I_filt

def sharpen(img):
    img2 = rgb2gray(img)
    flt = -np.ones((3,3))/22
    flt[1,1] = 1
    return show_conv(img2, flt)
