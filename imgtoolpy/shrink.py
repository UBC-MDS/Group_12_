import numpy as np


def shrink(image, width, height):
    """
    This function shrink image to desired width and height by
    removing pixels from border.

      Arguments
      ---------

          image : numpy.ndarray
              An image as a 3D numpy array
          width : int
              Desired width of shrinked image
          height : int
              Desired height of shirnked image
      Returns
      -------
          numpy array
              Shrinked image as 3D array

      Examples
      -------
      >>> imgtoolpy.shrink(image, width = 20, height = 20)

      """
    # checking if input is valid
    if (type(image) != np.ndarray) or (len(image.shape) != 3):
        raise TypeError('Invalid Type: input type for image must be 3D array')
    if (width % 1 != 0) or (height % 1 != 0):
        raise TypeError(
            'Invalid Value: Height and width for new image must be integer')
    if (height <= 0 or width <= 0):
        raise ValueError('Desired height and width must be greater than 1')
    if (height > image.shape[0] or width > image.shape[1]):
        raise ValueError(
            'Desired height and width cannot exceeds original height and \
             width')

    # calculate number of rows/columns of pixels to be removed
    crop_row = image.shape[0] - height
    crop_col = image.shape[1] - width

    # When number of rows to crop out is even, remove equal
    # number of rows from top and bottom border
    if crop_row % 2 == 0:
        top_row = int(crop_row/2)
        bottom_row = int(image.shape[0] - top_row)

    # When number of rows to crop out is odd, remove 1 more
    # row from top than bottom border
    else:
        top_row = int((crop_row + 1)/2)
        bottom_row = int(image.shape[0] - top_row + 1)

    # When number of columns to crop out is even, remove equal
    # number of columns from left and right border
    if crop_col % 2 == 0:
        left_col = int(crop_col/2)
        right_col = int(image.shape[1] - left_col)

    # When number of columns to crop out is odd, remove 1 more
    # columns from left than right border
    else:
        left_col = int((crop_col + 1)/2)
        right_col = int(image.shape[1] - left_col + 1)

    # Shrink image by cropping rows and columns
    shrinked = image[top_row:bottom_row, left_col:right_col, :]

    return shrinked
