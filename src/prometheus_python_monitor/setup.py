#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

requirements = ["prometheus_client"]
setup_requirements = []
test_requirements = [
    'pytest',
]

setup(
    name='prometheeus_python_monitor',
    version='0.1.0',
    description="Monitor Python f(x) performance with Prometheus.",
    author="Toomas Ormisson",
    author_email='Toomas.Ormisson@gmail.com',
    url='https://github.com/p6rguvyrst',
    packages=[
        'prometheus_python_monitor',
    ],
    entry_points={
        'console_scripts': [
            'test-monitor=prometheus_python_monitor.testing_fx:alpha'
        ]
    },
    #include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='python_monitor',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
