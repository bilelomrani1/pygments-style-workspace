#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name='pygments-style-workspace',
    version='0.1',
    description='Pygments version of the workspace theme.',
    long_description=open('README.md').read(),
    keywords='pygments style workspace',
    license='MIT',

    author='Bilel Omrani',

    packages=find_packages(),
    install_requires=['pygments >= 1.4'],

    entry_points='''[pygments.styles]
                    workspace=pygments_style_workspace:WorkspaceStyle''',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)