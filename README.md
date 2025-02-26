# PyVisiLibity
Python binding of [VisiLibity 1](https://karlobermeyer.github.io/VisiLibity1/). 

Support both Python 2.7 and  Python >= 3


## Installtion 


`swig` is required to build C++ extension. 
Check [here](https://github.com/swig/swig/wiki/Getting-Started) for the instruction.


To install the Python package:

`pip install visilibity`

### On Windows

Make sure you have the buildtools installed:
1. Download [Buildtools für Visual Studio 2022](https://aka.ms/vs/17/release/vs_BuildTools.exe)
2. Select `C++ Tools for Linux Development` and install

After that you need to install the `swig` and `cython`. When using conda just run 
```
conda install swig boost cython
```

Now you can install the package with
```
pip install .
```

## Run test with example

After installation, it would possible to run the test example `visilibity_test.py`.

Get a copy of test file from this [repository](https://github.com/tsaoyu/PyVisiLibity) and run 

`python visilibity_test.py`

The test script is self-explanatory. If anything wrong make sure you have `matplotlib` installed and configured.

## Issue

Please file me any issue related to the installtion and usage of PyVisiLibity in this repository. 
However any issue concerned about the core function of PyVisiLibity such as add new feature, bug report need to be raised at original VisiLibity [repository](https://github.com/karlobermeyer/VisiLibity1).
