# -*- coding: utf-8 -*-

# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Marvis class from file Marvis.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .marvis import Marvis
    return Marvis(iface)
