from group_12 import sharpen
import matplotlib.pyplot as plt

def test_read_image():
    img = sharpen.read_image("img/milad_cropped.png")
    assert len(img.shape) == 3
    assert img.shape[0] == 372
    assert img.shape[1] == 372
    assert img.shape[2] == 4

def test_sharpen():
    img = sharpen.read_image("img/milad_cropped.png")
    img2 = sharpen.sharpen(img)
    assert img2.shape[0] == 372
    assert img2.shape[1] == 372
    assert len(img2.shape) == 2
