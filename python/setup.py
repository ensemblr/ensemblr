import os
import sys
from distutils.core import setup

def config_cython():
    try:
        from Cython.Build import cythonize
        from distutils.extension import Extension
        if sys.version_info >= (3, 0):
            subdir = "_cy3"
        else:
            subdir = "_cy2"
        ret = []
        path = "ensemblr/cython"

        for fn in os.listdir(path):
            if not fn.endswith(".pyx"):
                continue
            ret.append(Extension(
                "ensemblr/%s/%s" % (subdir, fn[:-4]),
                ["ensemblr/cython/%s" % fn],
                include_dirs=["../include/"],
                language="c++"))
        return cythonize(ret)
    except:
        print("Cython is not installed, will compile without cython module")
        return []

setup(
    name='ensemblr',
    ext_modules = config_cython()
)
