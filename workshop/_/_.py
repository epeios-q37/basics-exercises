import sys, os

sys.path.append("./EduTK.zip")
sys.path.append("../EduTK.zip")

if ('Q37_XPP' in os.environ):
  sys.path.append(os.path.join(os.environ["HOME"],"epeios/other/libs/edutk/PYH/edutk"))

import edutk as _

from edutk import Atlas, Core, core, dom, recall, store

F_SALUTE = "Salute"
F_RESOLVE = "Resolve"
F_DRAW = "Draw"
F_CONNECT = "Connect"
F_SUBMIT = "Submit"
F_RESTART = "Restart"
C_HANGMAN = "Hangman"

_.defineUserItems(globals(), "uf", (
  F_SALUTE,
  F_RESOLVE,
  F_DRAW,
  F_CONNECT,
  F_SUBMIT,
  F_RESTART))

_.defineUserItem(globals(), "uc", C_HANGMAN)

def readBody(folder,i18n=None):
  return _.read(os.path.join("workshop","assets",folder,"Body.html"), i18n)

def mainBase(folder, callback, callbacks, ids, globals, userFunctionLabels, title):
# Uncomment for exceptions behaving normally again,
# instead of being displayed in a alert box.
  #_.useRegularExceptions()
  if ids:
    _.assignUserItems(ids, globals, userFunctionLabels)
  _.main(os.path.join("workshop", "assets", folder, "Head.html"), callback, callbacks, title)
