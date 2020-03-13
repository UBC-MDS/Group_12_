import numpy as np
from sklearn.cluster import KMeans


def compress(img, b):
    """
    Quantizes an image into 2^b clusters and
    return a version of the image (the same size as the original)
    where each pixel's original colour is replaced with the nearest
    prototype colour.

    Parameters
    ----------
    img : a (H,W,3) numpy array
      the image to be processed
    b   : int
      the desired number of bits

    Returns
    --------
    img : a (H,W,3) numpy array, returns the compressed image

    """

    # inpute tests
    if type(b) != int:
        raise TypeError("b should be an integer!")
    if b <= 0:
        raise ValueError("b should be positive!")
    if (img.ndim != 3) or (type(img) != np.ndarray):
        raise TypeError("The dimension of the input image must be 3D array")

    # the function
    H, W, _ = img.shape
    # use KMeans for compression
    model = KMeans(n_clusters=2**b)
    # reshape the image
    image_array = np.reshape(img, (H * W, 3))
    # fit the model using KMeans
    model.fit(image_array)
    # reshape labels
    quantized_img = model.labels_.reshape(H, W)
    # find the cluster centers
    colours = model.cluster_centers_.astype('uint8')
    # dequantized where the original color is replaced
    # with the nearest prototype colour
    img_quan = colours[quantized_img]

    return img_quan
