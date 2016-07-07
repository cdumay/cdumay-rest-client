# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. codeauthor:: Cédric Dumay <cedric.dumay@gmail.com>

"""

from setuptools import setup

setup(
    name='cdumay-rest-client',
    version=open('VERSION', 'r').read().strip(),
    description="HTTP client",
    long_description=open('README.md', 'r').read().strip(),
    classifiers=["Programming Language :: Python"],
    keywords='',
    author='Cedric DUMAY',
    author_email='cedric.dumay@gmail.com',
    url='https://github.com/cdumay/cdumay-rest-client',
    license='Apache License',
    py_modules=['cdumay_rest_client'],
    include_package_data=True,
    zip_safe=True,
    install_requires=open('requirements.txt', 'r').readlines(),
)
