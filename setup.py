# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import sys
sys.path.append('./src')
sys.path.append('./tests')

setup(name='othelloi',
    version='0.1',
    author='Suguru Kato',
    packages=find_packages(),
    test_suite='tests')
