from imgtoolpy.shrink import shrink
from numpy import random
import pytest
from imgtoolpy.toy_img import img as image

image_wrong_type = [1, 2, 3]
image_wrong_dim = random.random((50, 50))


def test_crop_output():
    '''
    This function test the output image of the shrink function,
    checking the shape and type is correct.
    '''
    assert shrink(image, 20, 20).shape[0:2] == (20, 20)

    assert shrink(image, 15, 15).shape[0:2] == (15, 15)

    assert shrink(image, 20, 20).shape[0:2] == (20, 20)

    assert shrink(image, 20, 20).shape[2] == 3

    assert len(shrink(image, 20, 20).shape) == 3


def test_shrink_error():
    '''
    This function test the error handling when invalid inputs
    are entered
    '''
    with pytest.raises(TypeError):
        shrink(image, 5.1, 5)
    with pytest.raises(ValueError):
        shrink(image, -1, 1)
    with pytest.raises(ValueError):
        shrink(image, 2000, 2000)
    with pytest.raises(TypeError):
        shrink(image_wrong_type, 10, 10)
    with pytest.raises(TypeError):
        shrink(image_wrong_dim, 10, 10)
