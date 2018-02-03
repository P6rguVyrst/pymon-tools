import setuptools

setuptools.setup(
    name="monitoring_exceptions",
    version="0.1.0",
    url=" https://github.com/P6rguVyrst/monitoring/src/exceptions",

    author="Toomas Ormisson",
    author_email="toomas.ormisson@gmail.com",

    description="Exceptions for monitoring namespace packages",
    long_description=open('README.rst').read(),

    packages=[
        'monitoring.exceptions',

    ],

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
