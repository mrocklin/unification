#!/usr/bin/env python

from os.path import exists, join
import re
from setuptools import setup

version = re.findall(
    r'__version__ = \'([.0-9]+)\'',
    open(join('unification', '__init__.py'), 'r').read())[0]

setup(name='unification',
      version=version,
      description='Unification',
      url='http://github.com/mrocklin/unification/',
      author='https://raw.github.com/mrocklin/unification/master/AUTHORS.md',
      maintainer='Matthew Rocklin',
      maintainer_email='mrocklin@gmail.com',
      license='BSD',
      keywords='unification logic-programming dispatch',
      packages=['unification'],
      install_requires=open('dependencies.txt').read().split('\n'),
      long_description=(open('README.rst').read() if exists('README.rst')
                        else ''),
      zip_safe=False)
