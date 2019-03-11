#!/usr/bin/env python

from distutils.core import setup

setup(
    name='taxbit-cexio-python',
    version='0.1.4',
    packages=['taxbit_cexio'],
    description='Python wrapper for CEX.IO',
    url='https://github.com/taxbit-open-source/python-cexio/',
    author='SERKAN BIRCAN',
    author_email='serkan@siniradam.net',
    maintainer='Chris Gunnels',
    maintainer_email='chris@taxbit.com',
    license='MIT',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',
        'Topic :: Office/Business :: Financial',
    ],
    include_package_data=True,
    zip_safe=False
)
