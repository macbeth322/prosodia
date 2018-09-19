#!/usr/bin/env python3

from setuptools import setup, find_packages

test_requirements = [
    'pytest-cov',
    'pytest'
]

setup(
    name='prosodia',
    version='0.2.5',
    author='macbeth322',
    author_email='chrisp533@gmail.com',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
        'typing'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    extras_require=dict(test=test_requirements),
    package_data={
        'prosodia': ['py.typed'],
        '': ['*.grammar']
    },
    zip_safe=False
)
