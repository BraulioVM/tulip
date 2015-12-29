#!/usr/bin/env python

from setuptools import setup

setup(
    name='tulip',
    version='0.1',
    description='Display simple images in your terminal',
    author='Braulio Valdivielso',
    author_email='yosoy@braulio.me',
    packages=['tulip'], 
    install_requires=[
        'Pillow>=3.0.0',
        'click>=6.2'
    ],
    entry_points={
        'console_scripts': [
            'tulip=tulip:tulip'
        ]
    },
    classifiers=[
            'Programming Language :: Python :: 3',
    ]
)
