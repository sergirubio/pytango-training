# Introduction to PyTango

Materials used in this training thanks to : 

* [Vincent Michel](https://github.com/vxgmichel)
* [Tiago Coutinho](https://github.com/tiagocoutinho)
* [Antoine Dupré](https://github.com/AntoineDupre)
* [Anton Joubert](https://github.com/ajoubertza)

https://pytango.readthedocs.io/

https://pytango.readthedocs.io/en/stable/quicktour.html

**PyTango** is a python module that exposes to Python the complete Tango C++ API. This means that you can write not only tango applications (scripts, CLIs, GUIs) that access tango device servers but also tango device servers themselves, all of this in pure python.

PyTango wraps Tango C++ libraries using **Boost:Python**. A new version is currently under development using **pybind11**. It will provide a lighter wrapper and a more modern approach.

Using a Python wrapper on top of Tango C++ libraries helps to standardize the behaviour of the two development APIs. 

Documentation and feature examples are valid for both languages and it allows to mix Tango Device Servers written in both languages in a single Device Server launcher.

But, using a wrapper on top of C++ force us to use an API that is not pythonic. To solve this issue the **Python HL API** is provided, allowing the development of fully-pythonic devices.

----

## PyTango API

https://pytango.readthedocs.io/en/stable/server_api/

* API is almost identical than for C++ (all methods available, all documentation and examples are valid)
* It's not pythonic (method names and workflow may feel not natural in python)
* Coding overhead (it's needed to declare many methods that may not be used at all).

## PyTango High Level API (HL)

https://pytango.readthedocs.io/en/stable/server_api/server.html

* Use of python primitives like decorators and properties reduce the number of lines of code to implement 
to less than a half.
* Pythonic, simpler, shorter and clearer code
* Due to API simplification, many functionalities become "hidden" (to use all features, fallback to old API is needed).

## Pythonic

Pythonic is an adjective that describes an approach to computer programming that agrees with the founding philosophy of the Python programming language. There are many ways to accomplish the same task in Python, but there is usually one preferred way to do it. This preferred way is called "pythonic."

* Python philosophy of writing code
* Beautiful is better than ugly.
* Explicit is better than implicit.
* Simple is better than complex.
* Complex is better than complicated.
* Flat is better than nested.
* Sparse is better than dense.
* Readability counts.

----

## Topics not covered on the training

 * Jupyter notebooks
 * Unit Testing
 * TGQL
 * Green modes (asyncio)
 ...
