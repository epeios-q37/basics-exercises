# coding: utf-8
""" 
MIT License

Copyright (c) 2019 Claude SIMON (https://q37.info/s/rmnmqd49)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
 
import workshop._.z_3 as workshop
import workshop.fr._ as _
from workshop.fr.display import *


class _Core(workshop.Core):
  i18n = {
    "Restart": "Recommencer"
  }

P_VISAGE = workshop.F_FACE
P_TETE = workshop.F_HEAD
P_CORPS = workshop.F_BODY
P_BRAS_GAUCHE = workshop.F_LEFT_ARM
P_BRAS_DROIT = workshop.F_RIGHT_ARM
P_PIED_GAUCHE = workshop.F_LEFT_LEG
P_PIED_DROIT = workshop.F_RIGHT_LEG

def redessine():
  workshop.redraw()


def dessinePendu(partie):
  workshop.drawFigure(partie)


def go(globals):
  workshop.main(globals, lambda dom: _Core(dom), _.LABELS, _.DEFAULT_TITLE)
