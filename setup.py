#!/usr/bin/env python

import os
from setuptools import find_packages, setup

execfile('pynsot/version.py')

with open('requirements.txt') as requirements:
    required = requirements.read().splitlines()

kwargs = {
    'name': 'pynsot',
    'version': str(__version__),
    'packages': find_packages(exclude=['tests']),
    #'scripts': ['bin/nsot-server', 'bin/nsot-ctl'],
    'description': 'Python interface for Network Source of Truth (nsot)',
    'author': 'Jathan McCollum',
    'maintainer': 'Jathan McCollum',
    'author_email': 'jathan@dropbox.com',
    'maintainer_email': 'jathan@dropbox.com',
    'license': 'Apache',
    'install_requires': required,
    'url': 'https://github.com/dropbox/pynsot',
    #'download_url': 'https://github.com/dropbox/pynsot/archive/master.tar.gz',
    'classifiers': [
        'Programming Language :: Python',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
}

setup(**kwargs)