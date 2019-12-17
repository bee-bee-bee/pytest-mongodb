#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name='pytest-mongodb',
    version='0.0.1',
    author='hongzhen.bi',
    author_email='hzhbee@qq.com',
    maintainer='hongzhen.bi',
    maintainer_email='hzhbee@qq.com',
    description='A simple plugin to use with pytest',
    packages=['pytest_mongodb'],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    install_requires=['pytest>=4.2.0',
                      'PyYAML==5.1',
                      'pymongo==3.7.2',
                      'configparser'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'pytest11': [
            'pytest_mongodb = pytest_mongodb.plugin',
        ],
    },
)
