#!/usr/bin/env python

from os.path import exists
from setuptools import setup
import unification

setup(name='unification',
      version=unification.__version__,
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
