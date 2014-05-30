babeltrace-plugins
==================

Python plugins for Babeltrace enabling Scribe and Zipking logging

The plugins are written in Python 3 because Babeltrace python bindings are only
Python 3 compatible.

Requirements
------------

To use the plugins 2 extra modules are needed

* facebook-scribe 2.0

* thrift>=0.90

Both of them can be found in PyPi. However, to use them they have to be
converted to Python 3. This can be easily done with 2to3 tool.

After that, they should be installed with Python 3. 
