PyIpopt
=======

PyIpopt is a python module that allows you to use [Ipopt](http://www.coin-or.org/Ipopt/) in Python. It is Modified from from [Eric Xu's project](https://github.com/xuy/pyipopt) for Windwos and MSVC compiler

Installation
------------

### Dependencies

PyIpopt depends on the following packages:

1. Visual Studio and C/C++ support
2. [Ipopt](https://projects.coin-or.org/Ipopt)
3. [Numpy](http://numpy.scipy.org/)
4. Python.h (part of the python source code, you can download it from [Python.org](http://python.org))

### Install

First, get the latest source code using:

  $ git clone https://github.com/Behemoth-s/pyipopt.git

In your PyIpopt folder, edit setup.py to reflect the configuration of your system, then do

	$ python setup.py build
	$ python setup.py install

### Test

  $ python hs071.py

You should be able to see the result of solving the toy problem.

Usage
-----
You can use PyIpopt like this:

	import pyipopt
	# define your call back functions
	nlp = pyipopt.create(...)
	nlp.solve(...)
	nlp.close()

You can also check out hs071.py to see how to use PyIpopt.

PyIpopt as a module comes with docstring. You can poke around 
it by using Python's $help()$ command.

Testing
-------

I have included an example 

To see if you have PyIpopt ready, use the following command under the pyipopt's directory. 

		python hs071.py
	
The file "hs071.py" contains a toy optimization problem. If everything is OK, pyipopt will invoke Ipopt to solve it for you. This python file is self-documented and can be used as a template for writing your own optimization problems. 

Pyipopt is a legitimate Python module, you can inspect it by using standard Python commands like "dir" or "help". All functions in pyipopt are documented in details. 

**Hessian Estimation**: since Hessian estimation is usually tedious, Ipopt can solve problems without Hessian estimation. Pyipopt also supports this feature. The file "hs071.py" demonstrates the idea. If you provide the pyipopt.create function with an "eval_h" callback function as well as the "apply_new" callback function, Ipopt will delegate the Hessian matrix calculation to your function (otherwise Ipopt will approximate Hessian for you).




