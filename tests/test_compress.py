from group_12.compress import compress
from numpy import random
import pytest


# test examples
img = random.random((50,50,3))
img_wrong = random.random((50,50))
img_wrong2 = random.random((1))


# test functions
def test_compress():
    '''
    This function test the output image of the compress function,
    checking the shape and type is correct.
    '''
    img2 = compress(img, 3)
    
    # assert img2.shape[0] == img.shape[0]
    assert img2.shape[1] == img.shape[1]
    assert len(img2.shape) == 3 
    assert img2.shape[0] == img.shape[0]

def test_compress_error():
    '''
    This function test the error handling when invalid inputs
    are entered
    '''
    with pytest.raises(TypeError):
        compress(img, 5.1)
    with pytest.raises(TypeError):
        compress(img_wrong, 2)
    with pytest.raises(TypeError):
        compress(img_wrong2, 2)
    with pytest.raises(ValueError):
        compress(img, -3)




