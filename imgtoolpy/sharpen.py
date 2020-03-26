import numpy as np
from scipy.signal import convolve2d
from skimage.color import rgb2gray

import matplotlib.pyplot as plt


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
    (img2, img2_sharpened) : two (H,W) numpy arrays
        the original and sharpened images, both monotoned

    Examples
    --------
    >>> sharpen(image)

    """
    if (type(img) != np.ndarray) or (len(img.shape) != 3) or  \
            (img.shape[2] != 3):
        raise TypeError('Invalid Type: input type for image must be 3D H*W*3 \
            array')
    # make sure the input image is at least 10x of the filter
    if (img.shape[0] < 50 or img.shape[1] < 50):
        raise ValueError(
            'Input image should have height and width greater than 50 x 50')
    if (np.min(img) < 0 or np.max(img) > 1):
        img = (img - np.min(img)) / (np.max(img) - np.min(img))
        print("Image brightness normalized")

    img2 = rgb2gray(img)

    # Create a 2-D array with 1 in the center and negative
    # otherwise to highlight the edge
    n = 3
    N = n * 2 + 1
    flt = -np.ones((N, N)) / (16 * n**2)
    flt[1, 1] = 1

    I_filt = convolve2d(img2, flt, boundary='symm', mode='same')
    # normalize the brightness of the sharpened image
    img2_sharpened = (I_filt - np.min(I_filt)) / \
        (np.max(I_filt) - np.min(I_filt))

    return img2, img2_sharpened
