"""Fonts for DoehlerDashboard.py"""

from PyQt5.QtGui import QFont

class Font(QFont):
    def __init__(self, setFamily=None,
                 setPixelSize=12,
                 setBold=False,
                 setWeight=50,
                 SetKerning=False):
        super(Font, self).__init__()
        """Add all possible args, if not put in either have it on False or on None.
        Purpose is so that in the interface class we dont have to write 3-5 lines of font details,
        but rather we can put it all in 1 line as arguments"""
        self.setFamily(setFamily)
        self.setPixelSize(setPixelSize)
        self.setBold(setBold)
        self.setWeight(setWeight)
        self.setKerning(SetKerning)

