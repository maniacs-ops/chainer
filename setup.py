#!/usr/bin/env python

import sys

from setuptools import setup

import cupy_setup_build


setup_requires = []
install_requires = [
    'filelock',
    'nose',
    'numpy>=1.9.0',
    'protobuf',
    'six>=1.9.0',
]


# Hack for Read the Docs
on_rtd = cupy_setup_build.check_readthedocs_environment()
if on_rtd:
    print('Add develop command for Read the Docs')
    sys.argv.insert(1, 'develop')
    setup_requires = ['Cython>=0.23'] + setup_requires

cupy_setup_build.parse_args()

setup(
    name='cupy',
    version='1.0.0',
    description=('CuPy: NumPy-like API accelerated with CUDA'),
    author='Seiya Tokui',
    author_email='tokui@preferred.jp',
    url='http://cupy-ndarray.org/',
    license='MIT License',
    packages=['cupy',
              'cupy.binary',
              'cupy.core',
              'cupy.creation',
              'cupy.cuda',
              'cupy.indexing',
              'cupy.io',
              'cupy.linalg',
              'cupy.logic',
              'cupy.manipulation',
              'cupy.math',
              'cupy.padding',
              'cupy.random',
              'cupy.sorting',
              'cupy.statistics',
              'cupy.testing'],
    package_data={
        'cupy': ['core/carray.cuh'],
    },
    zip_safe=False,
    setup_requires=setup_requires,
    install_requires=install_requires,
    tests_require=['mock',
                   'nose'],
    # To trick build into running build_ext
    ext_modules=[cupy_setup_build.dummy_extension],
    cmdclass={
        'build_ext': cupy_setup_build.cupy_build_ext,
    },
)
