def compress(img, b):
    """
    Quantizes an image into 2^b clusters and
    return a version of the image (the same size as the original)
    where each pixel's original colour is replaced with the nearest prototype colour.

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


def shrink(img, width, height):
    """ A function that performs vertical seam carve for image shrinking.
    Given the a image matrix as input and specified height and width,
    this function will shrink the input image to the specified height and
    width, then return the shrinked image matrix.

    Args:
        img (matrix): An image in matrix form.
        width (int): Width of the output image.
        height (int): Height of the output image.

    Returns:
        matrix: Shrinked image matrix of the input image.

    """
