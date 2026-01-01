from setuptools import setup, Extension
from Cython.Build import cythonize

# 📦 Define a Cython extension module
# - name: module name used in Python imports
# - sources: .pyx file that contains Cython/C++ code
# - language: tells the compiler to use C++
ext = Extension(
    name='solution',
    sources=['solution.pyx'],
    language='c++'
)

# ⚙️ Build configuration using Cython
# - cythonize converts .pyx → C/C++ code
# - language_level=3 ensures Python 3 semantics
setup(
    ext_modules=cythonize(
        ext,
        language_level=3
    )
)