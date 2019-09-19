import sys
from setuptools import setup, find_packages


setup(
    name='chillin-server',
    version='2.1.0',
    description='Chillin AI Game Framework (Python Server)',
    long_description='',
    author='Koala',
    author_email='mdan.hagh@gmail.com',
    url='https://github.com/koala-team/Chillin-PyServer',
    keywords='ai game framework chillin',

    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Application Frameworks'
    ],

    license='AGPL License, Version 3.0',

    install_requires=[
        'circuits==3.2',
        'pydblite==3.0.4',
        'configparser==3.5.0',
        'enum34==1.1.6'
    ],

    extras_require={
        'dev': ['koala-serializer']
    },

    packages=find_packages(),

    package_data={
        'chillin_server': ['default_certs/*']
    }
)
