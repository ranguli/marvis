Installation
============

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
   cd QGIS && mkdir build
   cd build && ccmake .. # Hit the [c] key and the [g] at the menu to generate the defaults.
   make -jX #Where X is your CPU core count
   ./output/bin/qgis
Build Marvis
--------------

Run:

.. code-block:: bash

   pip install -r reqruiements.txt
   pb_tool deploy
