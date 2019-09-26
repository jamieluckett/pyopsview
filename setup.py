#!/usr/bin/env python
# -*- encoding: UTF-8 -*-

from setuptools import setup, find_packages


def file_read(filename):
    with open(filename, 'r') as f:
        return f.read().strip()


def file_readlines(filename):
    with open(filename, 'r') as f:
        return f.readlines()


package = {
    'name': 'pyopsview',
    'version': file_read('VERSION'),
    'description': 'Python client for the Opsview API',
    'long_description': file_read('README.md'),
    'long_description_content_type': 'text/markdown',

    'classifiers': [
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ],

    'keywords': 'pyopsview opsview api',
    'maintainer': 'Joshua Griffiths',
    'maintainer_email': 'joshua.griffiths@opsview.com',
    'url': 'https://github.com/opsview/pyopsview',
    'download_url': 'https://github.com/opsview/pyopsview',
    'project_urls': {
        'Bug Reports': 'https://github.com/opsview/pyopsview/issues',
        'Source Code': 'https://github.com/opsview/pyopsview',
        'Opsview Homepage': 'https://www.opsview.com'
    },

    'packages': find_packages(),
    'package_dir': {
        'pyopsview': 'pyopsview',
    },
    'package_data': {
        'pyopsview': ['VERSION', 'README.md', 'schemas/*.json'],
    },
    'include_package_data': True,
    'install_requires': file_readlines('requirements.txt'),
}

setup(**package)
