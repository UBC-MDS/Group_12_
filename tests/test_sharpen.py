from group_12.sharpen import sharpen, read_image
import matplotlib.pyplot as plt
from numpy import random
import pytest

img = read_image("img/milad_cropped.png")
img2 = sharpen(img)
img3 = random.random((20,20,3))
img4 = random.random((60,60))

# class test_sharpen():
def test_read_image():
    assert len(img.shape) == 3
    assert img.shape[0] == 372
    assert img.shape[1] == 372
    assert img.shape[2] == 4

def test_sharpen():
    assert img2.shape[0] == 372
    assert img2.shape[1] == 372
    assert len(img2.shape) == 2

def test_sharpen_error():
    with pytest.raises(ValueError):
        sharpen(img3)
    with pytest.raises(TypeError):
        sharpen(img4)
