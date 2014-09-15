#! /usr/bin/env python
#! coding:utf-8

from setuptools import setup
from hgsf import version

setup(
    name                = 'hgsf',
    version             = version.RELEASE_VERSION,
    author              = 'hahaya',
    author_email        = 'hahayacoder@gmail.com',
    license             = 'Apache License',
    description         = 'hgsf',
    url                 = 'https://github.com/hahaya/hgsf',
    packages            = [
        'hgsf',
        'hgsf/db',
        'hgsf/test',
        'hgsf/utils',
    ],
    scripts             = [
        'bin/hgsf',
    ],
    install_requires    = [
        'redis',
    ],
)
