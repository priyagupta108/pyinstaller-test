# -*- mode: python -*-
import os
from inspect import getfile
import PyQt5


# PyInstaller Cipher flag
block_cipher = None

# PyQt5 and dll location, specific to PyQt5 version (valid for version 5.5.1)
pyqt_dir = os.path.dirname(getfile(PyQt5))
pyqt_dlls =  os.path.join(pyqt_dir, 'plugins', 'platforms')

# Add qt.conf to indicate where PyInstaller placed dlls
#data_files += [('qt.conf', '.')]
binary_files = []
#binary_files += [(os.path.join(pyqt_dlls, 'qwindows.dll'), 'platforms')]
#binary_files += [(os.path.join(pyqt_dlls, 'qoffscreen.dll'), 'platforms')]
#binary_files += [(os.path.join(pyqt_dlls, 'qminimal.dll'), 'platforms')]


a = Analysis(['../qtconsole_test.py'],
             pathex=['../', pyqt_dir, pyqt_dlls],
             binaries=binary_files,
             datas=[],
             hiddenimports = ['ipykernel.datapub'],
             hookspath=[],
             runtime_hooks=[],
             # Back ends for qtconsole and matplotlib
             excludes=['PySide', 'PyQt4'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

pyz = PYZ(a.pure,
          a.zipped_data,
          cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='qtconsole_test',
          strip=False,
          # There is an issue with PyQt and UPX compression:
          # https://github.com/pyinstaller/pyinstaller/issues/2659
          upx=False,
          # False hides the CLI window, useful ON to debug
          console=True,
          debug=True,
          icon=None)

app = BUNDLE(exe,
         name='qtconsole_test.app',
         icon=None,
         bundle_identifier=None,
         info_plist={
            'NSHighResolutionCapable': 'True'})

# For debugging you can uncomment COLLECT and it will package to a folder
# instead of a single executable (also comment out the "a" arguments in EXE)
#coll = COLLECT(exe,
#               a.binaries,
#               a.zipfiles,
#               a.datas,
#               strip=None,
#               upx=False,
#               name='qtconsole_test')
