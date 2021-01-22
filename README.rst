=======
agldata
=======

|Docs Status|

.. contents::

What is agldata?
----------------
A python library for published data from artificial grammar learning or
statistical learning studies. Data can be efficiently accessed in a
structured way, for example to use them for (meta-) analyses.

You can easily add data sets by entering them in a file in a user-friendly
format (`YAML <https://yaml.org/>`__). See `example here
<https://github.com/gbeckers/agldata/tree/master/agldata/datafiles
/wilsonetal_2013_jneurosci.yaml>`__.

Current version is: 0.1.0

**This library is in aplha stage, is not ready and not fully tested. It should
not be used for research yet.** If you are nevertheless interested in using if
for your research, consider collaborating with the main author of the library
(see contact).

Documentation
-------------
A first attempt to documentation can be found here:
https://agldata.readthedocs.io/

Install
-------
agldata depends on Python 3.6 or higher, and one external library (pyaml).

To install the latest release::

    $ pip install agldata

To use the latest version from GitHub, I recommend working in
Anaconda, in which case you could first create a separate
conda environment, called, e.g. "agl"::

    $ conda create -n agl python=3.8 jupyterlab git pyyaml=5.1

Then install agldata from GitHub::

    $ pip install git+https://github.com/gbeckers//agldata@master


To switch to this new environment in a terminal:

Linux and MacOS::

    $ source activate agltest

Windows::

    $ conda activate agltest


If you want to remove the conda environment later::

    $ conda env remove -n agl


Contributing
------------
To add data from studies, see see https://agldata.readthedocs.io/en/latest/contributing.html
for instructions on how to prepare data files.
To get them merged into the library or to fix bugs/add functionality, it is best to use a the
Github pull request workflow. It is described here:
https://github.com/processing/processing/wiki/Contributing-to-Processing-with-Pull-Requests

Included studies
----------------

See: https://agldata.readthedocs.io/en/latest/studies.html

Copyright and License
---------------------
:copyright: Copyright 2019-2021, Gabriel Beckers, Utrecht University.
:license: 3-Clause Revised BSD License, see LICENSE.txt for details.

Data from original studies has been entered by: Gabriel Beckers, Simon Buil.

Contact
-------
Gabriel Beckers, Utrecht University, https://www.gbeckers.nl

.. |Docs Status| image:: https://readthedocs.org/projects/agldata/badge/?version=latest
   :target: https://agldata.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status