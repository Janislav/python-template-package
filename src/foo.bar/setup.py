# -*- coding: utf-8 -*-
from setuptools import setup
setup(
    name='foo.bar',
    version='0.1.0',
    author='J. Random Hacker',
    author_email='jrh@example.com',
    packages=['foo', 'foo.bar'],
    description='A template python package.',
    long_description=open('../../README.rst').read(),
    entry_points={'console_scripts': ["myCommand = foo.bar:main"]},
)
