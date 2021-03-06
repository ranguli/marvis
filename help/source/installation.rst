Installation
============

Requirements
------------

- QGIS 3
- Python 3
- pip3
- Git
- PyQt5
- pb_tool
- virtualenv 

(Optional) Compile QGIS 3.x
------------

We are compiling QGIS from source because it's helpful to have access to the API code, but mainly 
because QGIS 3.x is not available in our package manager yet. 

Refer to the QGIS `docs
<https://github.com/qgis/QGIS/blob/master/INSTALL/>`_ if this overview is too succint. 

.. code-block:: bash

   # Important: install the dependencies they mention before proceeding.
   # There are a large number of packages required to compile QGIS. 
   
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

