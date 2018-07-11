Installation
============

<<<<<<< HEAD
Requirements
------------

- QGIS 3
- Python 3
- pip3
- Git

Compile QGIS
------------

Refer to the QGIS `docs
<https://github.com/qgis/QGIS/blob/master/INSTALL/>`_ if this overview is too succint. 

.. code-block:: bash

   # After you've installed the dependencies they list ...  

   cd /usr/local/bin
   sudo ln -s /usr/bin/ccache gcc
   sudo ln -s /usr/bin/ccache g++

   mkdir YOURDIR
   cd YOURDIR && git clone https://github.com/qgis/qgis.it  
   cd QGIS
   git fetch origin && git checkout release-3_2
   mkdir build && cd build
   ccmake .. # Hit the [c] key and the [g] at the menu to generate the defaults.
   make -jX #Where X is your CPU core count
   # It will be easier to run "make install" too. 
   ./output/bin/qgis

Build Marvis
--------------

Run:

.. code-block:: bash

   pip install -r requirements.txt
   pb_tool deploy
=======
Dependencies
-------------

Make sure you install all of the following

Use the general instructions for you OS to install:

- ``python`` Our programming language
- ``pip`` Our python package manager.
- ``git`` Our version control system.
- ``QGIS 2.x`` Our GIS software (or try 3.x and report your findings)
- ``QtCreator`` The GUI design tool for our GUI framework of choice (Qt)

Install the following using Python's ``pip`` package manager:

- ``PyQT5`` Bindings to use Qt5 with Python
- ``sphinx`` How we create these pretty docs 
- ``pb_tool`` Our tool for turning Python code into a QGIS plugin



Obtaining the Source Code
-------------------------

Ensuring you have ``git`` installed, on a command line, and in the directory you want to store the marvis code, run:

``git clone https://github.com/ranguli/marvis``

Then enter the marvis directory:

``cd ./marvis``

With no errors, move on to the next section.

**Note:** once you are ready to starting contributing to the code, you will need to switch to a different *branch.* This is outside the scope of the documentation.

Compilation
------------

Compilation is perhaps a bit of a misnomer seen as how we're using an interpreted language, but there
are certain files that do need to be collected or converted from another format into Python when
one is developing plugins for QGIS. The equivalent of a "compiler" for us will be ``pb_tool`` which
you should have installed with ``pip`` earlier.


To only **compile** the plugin, run:

``pb_tool compile``

To **compile and copy** the plugin to the QGIS plugins directory, run:

``pb_tool deploy`` 

Or, in shorthand: 

``pb_tool de`` 

The tool is told exactly what to do using a config file, ``pg_tool.cfg`` in the project root directory. If you need
to troubleshoot the behavior of ``pb_tool`` confirming that the config file is properly set up may be helpful.

The tool also comes with various other helpful features, such as ``clean``
>>>>>>> 26129d2513ad43386c8f9067ef46dd00a9c9af86
