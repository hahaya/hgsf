#! /usr/bin/env python
#! coding:utf-8

from setuptools import setup
from hgsf import version

setup(
    name='hgsf',
    version=version.RELEASE_VERSION,
    description='hgsf',
    author='hahaya',
    url='https://github.com/hahaya/hgsf',
    packages=['hgsf',],
    scripts=['bin/hgsf',],
)
