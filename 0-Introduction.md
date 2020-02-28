#Introduction to PyTango

https://pytango.readthedocs.io/

PyTango is a python module that exposes to Python the complete Tango C++ API. This means that you can write not only tango applications (scripts, CLIs, GUIs) that access tango device servers but also tango device servers themselves, all of this in pure python.

PyTango wraps Tango C++ libraries using Boost:Python. A new version is currently under development using pybind11. It will provide a lighter wrapper and a more modern approach.

Using a Python wrapper on top of Tango C++ libraries helps to standardize the behaviour of the two development APIs. 

Documentation and feature examples are valid for both languages and it allows to mix Tango Device Servers written in both languages in a single Device Server launcher.

But, using a wrapper on top of C++ force us to use an API that is not pythonic. To solve this issue the Python HL API is provided, allowing the development of fully-pythonic devices.
