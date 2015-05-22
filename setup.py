import os, sys, string, re
from glob import glob
import numpy

import distutils
from distutils.core import setup, Extension

headers = glob (os.path.join ("Include","*.h") )
#header = headers + glob (os.path.join ("Include/numpy","*.h") )

setup ( name = "Shadow",
        version = "0.1.0",
        author_email = 'srio@esrf.eu',
        author = 'Franco Cerrina, Chris Welnak, G.J. Chen and M. Sanchez del Rio',
        url = 'http://ftp.esrf.eu/pub/scisoft/shadow3/',
	packages=["Shadow"],
        package_dir={"Shadow":"."},
        ext_modules = [Extension('Shadow.ShadowLib',
                                 ['shadow_bind_python.c'],
                                 include_dirs  = ['.', numpy.get_include()],
                                 library_dirs  = ['.'],
                                 libraries     = ['shadow3','shadow3c', 'gfortran'],
                                 extra_compile_args = ['-msse','-msse2'],
                                 extra_link_args = ['-msse','-msse2']
                                ),
                      ]
        )
