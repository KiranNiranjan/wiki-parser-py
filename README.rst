Wikipedia Parser                                          |wikiparser logo|
===========================================================================

Simple and best tool to parse wikipedia

.. image:: https://travis-ci.org/KiranNiranjan/wiki-parser-py.svg?branch=master
    :target: https://travis-ci.org/KiranNiranjan/wiki-parser-py


Installing
----------

.. code:: bash

    pip install wikiparser

Getting Started
---------------

These instructions will get you a copy of the project up and running on
your local machine for development and testing purposes. See deployment
for notes on how to deploy the project on a live system.

Dependency
~~~~~~~~~~

-  Python 3
-  wikiparser

Import
~~~~~~

.. code:: python

    from wikiparser import *

Importing specific methods
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    from wikiparser import infoBox, getMainImage, getParagraph

Methods
~~~~~~~

-  infoBox()

   .. code:: python

       ''' To get info_box table from wikipedia as json '''
       infoBox = infoBox("https://en.wikipedia.org/wiki/Methane")

Running the tests
-----------------

Explain how to run the automated tests for this system

.. code:: bash

    python tests/test.py

Authors
-------

`KiKe`_

Javasctipt (npm)
----------------

`wikiparser`_ `KiKe`_

License
-------

This project is licensed under the MIT License - see the `LICENSE.md`_
file for details

.. _KiKe: http://kike.co.in
.. _wikiparser: https://www.npmjs.com/package/wikiparser
.. _LICENSE.md: ./LICENSE.md

.. |wikiparser logo| image:: https://raw.githubusercontent.com/KiranNiranjan/wiki-parser-js/master/images/wiki_parser_logo.png