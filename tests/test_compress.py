from group_12.compress import compress
from numpy import random

#img = random.random((50,50,3))

def test_compress():
    '''
    This function test the output image of the compress function,
    checking the shape and type is correct.
    '''
    img = random.random((50,50,3))
    img2 = compress(img, 3)
    
    # assert img2.shape[0] == img.shape[0]
    assert img2.shape[1] == img.shape[1]
    assert len(img2.shape) == 3
    assert img2.shape[0] == img.shape[0]
