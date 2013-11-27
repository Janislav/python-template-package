# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '0.1dev'

long_description = (
    read('../../README.rst')
    )

setup(name='foo.bar',
      version=version,
      description="foo.bar",
      long_description=long_description,
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
      #keywords='',
      author='John Doe',
      author_email='jd@example.com',
      packages=find_packages('.', exclude=['ez_setup']),
      package_dir={'.': 'foo'},
      namespace_packages=['foo'],
      include_package_data=True,
      zip_safe=True,
      entry_points={'console_scripts': ["myCommand = foo.bar:main"]},
      install_requires=['setuptools',
                        # -*- Extra requirements: -*-
                        ],
      )
