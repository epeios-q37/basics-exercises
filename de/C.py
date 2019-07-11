# coding: utf-8

import sys
sys.path.append(".")
from workshop.de.c import *

def meineFunktion(name):
  anzeige("Hallo, " + name + " !")
  anzeige("Einen schönen Tag noch, " + name )


go(meineFunktion)
