import numpy as np
import pandas as pd
# import os
from scipy.signal import convolve2d
from skimage.color import rgb2gray

import matplotlib.pyplot as plt
# %matplotlib inline

def read_image(filename):
    return plt.imread(filename)

def sharpen(img):
    """
    Detects and enhances the edges in the image and
    returns a sharpened and monotoned version (the same size as the original).

    Parameters
    ----------
    img : a (H,W,3) numpy array
      the image to be processed

    Returns
    --------
    img : a (H,W) numpy array, returns the sharpened and monotoned image

    """
    img2 = rgb2gray(img)
    flt = -np.ones((3,3))/22
    flt[1,1] = 1

    I_filt = convolve2d(img2, flt, boundary='symm', mode='same')
    I_filt = np.maximum(0, I_filt) # set negative values to 0, for visualization purposes
    I_filt = np.minimum(1, I_filt) # set values greater than 1 to 1, for visualization purposes

    return (I_filt - np.min(I_filt)) / (np.max(I_filt) - np.min(I_filt))
