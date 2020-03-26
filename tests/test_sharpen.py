from imgtoolpy.sharpen import sharpen, read_image
from numpy import random
import pytest

img = read_image("img/free-wallpaper.jpg")
img_orig, img_sharpened = sharpen(img)
img3 = random.random((20, 20, 3))
img4 = random.random((60, 60))
img5 = random.random((60, 60, 4))

# class test_sharpen():


def test_read_image():
    assert len(img.shape) == 3
    assert img.shape[0] == 1066
    assert img.shape[1] == 1599
    assert img.shape[2] == 3


def test_sharpen():
    assert img_orig.shape[0] == 1066
    assert img_orig.shape[1] == 1599
    assert len(img_orig.shape) == 2

    assert img_sharpened.shape[0] == 1066
    assert img_sharpened.shape[1] == 1599
    assert len(img_sharpened.shape) == 2


def test_sharpen_error():
    with pytest.raises(ValueError):
        sharpen(img3)
    with pytest.raises(TypeError):
        sharpen(img4)
    with pytest.raises(TypeError):
        sharpen(img5)
