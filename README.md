## group_12

![](https://github.com/rita-ni/group_12/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/rita-ni/group_12/branch/master/graph/badge.svg)](https://codecov.io/gh/rita-ni/group_12) ![Release](https://github.com/rita-ni/group_12/workflows/Release/badge.svg)

[![Documentation Status](https://readthedocs.org/projects/group_12/badge/?version=latest)](https://group_12.readthedocs.io/en/latest/?badge=latest)

Python Boilerplate contains all the boilerplate you need to create a Python package.

### Installation:

```
pip install -i https://test.pypi.org/simple/ group_12
```

### Features
- `sharpen`:
  - This function enhances the edges in the image and returns a sharper-looking image.  At this moment, this function is restricted to gray-scale images only 
  
- `shrink`:
  - A function that performs vertical seam carve for image shrinking. This function take image input in the form of a matrix.
  - There are a few existing Python packages that perform content-aware image resizing, such as `pyCAIR` (available on PyPI https://pypi.org/project/pyCAIR/), and `seam-carver` (https://pypi.org/project/seam-carver/). Currently, there is no package available on CRAN to resize images based on the same mechanism, however, there is a package available on Github to seam carve image (https://github.com/vgorte/SC-Package-R). These packages use the seam carving process to increase or decrease the size of the image by finding the seam with the lowest energy values from the energy map. Our implementation of image resizing is a less sophisticated version of seam carving, which focuses on downsizing images by removing low-energy vertical seams.

### Dependencies

- TODO

### Usage

- TODO

### Documentation
The official documentation is hosted on Read the Docs: <https://group_12.readthedocs.io/en/latest/>

### Credits
This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
