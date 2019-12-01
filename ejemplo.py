import subprocess, sys

"""opener ="open" if sys.platform == "darwin" else "xdg-open"
subprocess.call([opener, "zill.pdf"])"""


def AbrirAyuda():

    if sys.platform == 'linux':
        #Linux detectado
        subprocess.call(["xdg-open", "ayuda.pdf"])
    elif sys.platform == 'darwin':
        #MacOSx detectado
        subprocess.call(["open", "ayuda.pdf"])
    elif sys.platform.startswith('win'):
        #Windows detectado
        subprocess.call(["start", "ayuda.pdf"])

AbrirAyuda()

"""
AIX
'aix'
Linux
'linux'
Windows
'win32'
Windows/Cygwin
'cygwin'
macOS
'darwin'
"""
