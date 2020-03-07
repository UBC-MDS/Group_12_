## imgtoolPy 

![](https://github.com/rita-ni/imgtoolPy/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/rita-ni/imgtoolPy/branch/master/graph/badge.svg)](https://codecov.io/gh/rita-ni/imgtoolPy) ![Release](https://github.com/rita-ni/imgtoolPy/workflows/Release/badge.svg)

[![Documentation Status](https://readthedocs.org/projects/imgtoolPy/badge/?version=latest)](https://imgtoolPy.readthedocs.io/en/latest/?badge=latest)

### Package Overview

`imgtoolPy` is a Python package that is intended to allow users to compress, sharpen and shrink an input image. 
Our package only allows the input image to be a 3D numpy array and output the manipulated image as a 3D numpy array. It contains three functions: `compress()`, `sharpen()`, and `shrink()`. 


### Feature Description

- `compress`:
  - This function quantizes an image by restricting each pixel to only take on one of the desired colour values
  and return a version of the image (the same size as the original) where each pixel's original colour is replaced with the nearest prototype colour.
  

- `sharpen`:
  - This function enhances the edges in the image and returns a sharper-looking image.  At this moment, this function is restricted to gray-scale images only 
  
- `shrink`:
  - A function that shrink image size by removing border pixels until desired height and width are reached. This function take image input in the form of a 3D array.



### Installation:

```
pip install -i https://test.pypi.org/simple/imgtoolPy
```

### Related Packages

  There are a few existing Python packages that perform content-aware image resizing, such as `pyCAIR` (available on [PyPI](https://pypi.org/project/pyCAIR/)), and [seam-carver](https://pypi.org/project/seam-carver/). Currently, there is no package available on CRAN to resize images based on the same mechanism, however, there is a package available on Github to [seam carve image](https://github.com/vgorte/SC-Package-R). These packages use the seam carving process to increase or decrease the size of the image by finding the seam with the lowest energy values from the energy map. Our implementation of image resizing is a less sophisticated version of seam carving, which focuses on downsizing images by removing low-energy vertical seams. Also, there are similar packages for image manipulation such as [scikit-image](https://github.com/scikit-image/scikit-image), which could be used for filtering and transforming images. 

### Dependencies

- TODO

### Usage

- TODO

### Documentation
The official documentation is hosted on Read the Docs: <https://imgtoolPy.readthedocs.io/en/latest/>

### Credits
This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
# test-rename
# test-rename
