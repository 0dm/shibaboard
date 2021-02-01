# py2exe setup
from shutil import copy
from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

setup(
    options = {'py2exe': {'bundle_files': 3}},
    windows = [{'script': "shibaboard.py", 'icon_resources': [(1, "ico.ico")]}],
    zipfile = None,
)
copy("ico.ico", "dist")
