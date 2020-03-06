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
    if (type(img) != np.ndarray) or (len(img.shape) != 3):
        raise TypeError('Invalid Type: input type for image must be 3D array')
    # make sure the input image is at least 10x of the filter
    if (img.shape[0] < 50 or img.shape[1] < 50):
        raise ValueError('Input image should have height and width greater than 50 x 50')
    if (np.min(img) < 0 or np.max(img) > 1):
        raise ValueError('Input image should have values between 0 and 1')

    img2 = rgb2gray(img)

    # Create a 2-D array with 1 in the center and negative otherwise to highlight the edge
    flt = -np.ones((3,3))/22
    flt[1,1] = 1

    I_filt = convolve2d(img2, flt, boundary='symm', mode='same')
    I_filt = np.maximum(0, I_filt) # set negative values to 0, for visualization purposes
    I_filt = np.minimum(1, I_filt) # set values greater than 1 to 1, for visualization purposes

    return (I_filt - np.min(I_filt)) / (np.max(I_filt) - np.min(I_filt))
