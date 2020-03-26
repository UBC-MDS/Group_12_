from imgtoolpy.crop import crop
from numpy import random
import pytest


image = random.random((50, 50, 3))
image_wrong_type = [1, 2, 3]
image_wrong_dim = random.random((50, 50))


def test_crop_output():
    '''
    This function test the output image of the crop function,
    checking the shape and type is correct.
    '''
    assert crop(image, 20, 20).shape[0:2] == (20, 20)

    assert crop(image, 15, 15).shape[0:2] == (15, 15)

    assert crop(image, 20, 20).shape[0:2] == (20, 20)

    assert crop(image, 20, 20).shape[2] == 3

    assert len(crop(image, 20, 20).shape) == 3


def test_crop_error():
    '''
    This function test the error handling when invalid inputs
    are entered
    '''
    with pytest.raises(TypeError):
        crop(image, 5.1, 5)
    with pytest.raises(ValueError):
        crop(image, -1, 1)
    with pytest.raises(ValueError):
        crop(image, 80, 80)
    with pytest.raises(TypeError):
        crop(image_wrong_type, 10, 10)
    with pytest.raises(TypeError):
        crop(image_wrong_dim, 10, 10)
